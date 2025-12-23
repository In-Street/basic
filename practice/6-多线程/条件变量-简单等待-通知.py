"""

"""
import threading,random,time

condition = threading.Condition()

#共享资源
share_resource = []


#生产者
def produce():

	for _ in range(7):
		time.sleep(2)
		product = random.randint(1,10)

		with condition:   # 获取锁
			print(f'生产数据：{product}')
			share_resource.append(product)
			condition.notify() # 唤醒一个消费者


#消费者
def consume(name):

	for _ in range(7):
		with condition:
			while len(share_resource)==0:
				print(f'暂无共享数据，消费者 {name} 等待')
				condition.wait()  #释放锁并等待

			pop_result = share_resource.pop()
			print(f'消费者 {name} 处理：{pop_result} 数据')


produce_thread = threading.Thread(target=produce)

consumer_threads = [threading.Thread(target=consume,args=(i,)) for i in range(2)]

for t in consumer_threads:
	t.start()

produce_thread.start()


produce_thread.join()
for t in consumer_threads:
	t.join()
