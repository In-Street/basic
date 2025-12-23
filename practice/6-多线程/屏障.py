import threading
import time
import random


def worker(barrier, worker_id):
	"""工作线程任务"""
	print(f"工人{worker_id} 开始准备工作...")

	# 模拟准备工作耗时
	preparation_time = random.uniform(1.0, 3.0)
	time.sleep(preparation_time)

	print(f"工人{worker_id} 准备完成，耗时 {preparation_time:.2f}秒")

	# 等待所有工人准备就绪
	arrival_index = barrier.wait()  # 返回到达的序号（0到parties-1）

	print(f"工人{worker_id} 通过屏障，到达序号: {arrival_index}")
	print(f"工人{worker_id} 开始正式工作...")


def action_func():
	print(f'都到达屏障，执行回调，线程：{threading.current_thread().name}')

def basic_barrier_example():
	"""基本屏障示例"""
	# 需要3个线程
	barrier = threading.Barrier(parties=3,action=action_func)

	threads = []
	for i in range(3):
		thread = threading.Thread(
			target=worker,
			args=(barrier, i),
			name=f"Worker-{i}",
		)
		threads.append(thread)

	print("启动所有工人...")
	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

	print("所有工人完成工作！")


if __name__ == "__main__":
	basic_barrier_example()