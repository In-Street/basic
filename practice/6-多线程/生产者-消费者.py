from threading import Thread, current_thread
import random,queue,time

#线程安全队列
q = queue.Queue(5)


class Producer(Thread):
	def run(self):
		while True:
			num = random.randrange(1,100)
			q.put(num)
			print("生产者：{} , 生产数据：{}".format(current_thread().name,num))
			time_sleep = random.randint(1,3)
			time.sleep(time_sleep)


class Consumer(Thread):
	def run(self):
		while True:
			num = q.get()
			# q.task_done()
			print("消费者：{} , 消费数据：{}".format(current_thread().name, num))
			time_sleep = random.randint(1,3)
			time.sleep(time_sleep)


p1 = Producer(name='P1')

c1 = Consumer(name='C1')
c2 = Consumer(name='C2')

p1.start()
c1.start()
c2.start()
