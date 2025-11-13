#将抛出异常与类相结合，无需手动捕获异常，可使用with关键字

class TestWith:

	# 在类初始化时被调用
	def __enter__(self):
		print("开始")

	# 在结束时被调用
	def __exit__(self, type, value, traceback):
		if traceback is None:
			print("程序正常执行")
		else:
			print("有异常 %s" % traceback)


with TestWith():
	print("正在执行...")
	# a = 10/0
	# raise NameError("命名错误")

