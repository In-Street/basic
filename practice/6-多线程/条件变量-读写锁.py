"""
	 读写锁：
	    属性： 写优先、读锁条件变量、写锁条件变量、 正在读数量、正在写数量、排队读数量、排队写数量
	    方法：
	            获取读锁 、获取写锁、对外获取读锁、写锁、统计
"""
import threading
from contextlib import contextmanager


class ReadWriteLock:
	def __init__(self, write_priority: bool = True):
		self.write_priority = write_priority  # 默认 写优先

		self.lock = threading.Lock()  # 底层锁
		self.read_condition = threading.Condition(self.lock)  # 读条件
		self.write_condition = threading.Condition(self.lock) # 写条件

		self.reading_count = 0
		self.writing_count = 0
		self.wait_read_count = 0
		self.wait_write_count = 0

	def get_read_lock(self):
		with self.read_condition: # 通过读条件变量获取锁
			self.wait_read_count += 1
			while self.writing_count > 0 or (self.write_priority and self.wait_write_count > 0): #有正在写 或 写优先策略下有等待写的 ，读锁获取要等待
				self.read_condition.wait()

			self.reading_count += 1
			self.wait_read_count -= 1

	def release_read_lock(self):

		with self.read_condition:
			self.reading_count -= 1


			if self.write_priority and self.wait_write_count > 0 and self.reading_count ==0:
				self.write_condition.notify()
			elif self.wait_read_count > 0:
				self.read_condition.notify_all()


	def get_write_lock(self):
		with self.write_condition:
			self.wait_write_count += 1
			while self.reading_count > 0 or self.writing_count > 0:
				self.write_condition.wait()

			self.writing_count += 1
			self.wait_write_count -= 1

	def release_write_lock(self):
		with self.write_condition:
			self.writing_count -= 1

			if self.write_priority and self.wait_write_count > 0:  # 据优先级策略
				self.write_condition.notify()

			elif self.wait_read_count > 0:
				self.read_condition.notify_all()

			elif  self.wait_write_count >0:
				self.write_condition.notify()

	@contextmanager
	def write_lock(self):
		try:
			self.get_write_lock()
			yield
		finally:
			self.release_write_lock()

	@contextmanager
	def read_lock(self):
		try:
			self.get_read_lock()
			yield
		finally:
			self.release_read_lock()