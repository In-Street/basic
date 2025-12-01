"""
pip3 install requests

"""
import requests,shutil

base_url = 'https://httpbin.org/'
params = {'username': 'jay', 'city': '北京'}
get_url = f'{base_url}/get'

# response = requests.get(get_url, params=params)
# print(response.text)


post_url = f'{base_url}/post'
headers_body = {
	"Content-Type": "application/json;charset=utf-8",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"  # 可选：模拟浏览器请求
}
post_data = {"song": '一首歌的时间', 'artist': 'Jay', "hobby": ["reading", "coding"]}
# response = requests.post(post_url, data=post_data, headers=headers_body)
# print(response.json())


# 下载图片
'''
	1. requests 请求参数 stream=True，作用：仅下载响应头，不立即将整个响应体下载到内存，而是分块读取。适合处理大文件、流式数据。
		默认stream=False，会一次性加载响应体到内存中，生产 response.text / response.content
		
	2. 读取方式：
			response.iter_content(chunk_size=1024*1024)):  1M
				用于下载文件，返回字节块
				
			response.iter_lines(decode_unicode=True)):
				用于读取文本流，如日志文件、CVS流，按行返回字符串。 decode_unicode=True 会自动解码为字符串
				
	3. get_response.raw.decode_content = True
			response.raw:  返回未经过处理的字节流（比 response.content 更底层）
			decode_content = True: 
				让原始响应对象自动处理「内容编码」（包括 Transfer-Encoding: chunked 分块编码、Content-Encoding: gzip/deflate 压缩编码），将编码后的字节流解码为「原始文件内容」,确保你从 raw 读取的字节是最终可直接保存 / 使用的内容，而非编码后的二进制数据。
				Http协议为了优化传输会对响应体做出优化：
					分块编码（Transfer-Encoding: chunked）：将大响应体分成多个小块传输，每个块带长度标识；
					压缩编码（Content-Encoding: gzip）：用 gzip 压缩响应体，减少传输体积。
				如果不设置 decode_content = True，直接读取 raw 会拿到「带编码标识的原始字节」（比如分块的头部、gzip 压缩数据），保存后会是损坏的文件（比如打不开的视频、乱码的文档）。
				
			response.iter_content()属于高层API，已内置解码逻辑，无需手动调用decode_content=True		
	
'''
import os

img_url = 'http://imgoss.cnu.cc/2511/21/29bffl0kzqq9lpm4lpg1763716949623.jpg?x-oss-process=style/content'

abs_path = os.path.abspath('.')
file_base_name = os.path.basename(img_url.split('?')[0])

with requests.get(img_url, stream=True) as get_response:
	get_response.raise_for_status()  # 校验状态码，若为4xx\5xx 主动抛异常requests.exceptions.HTTPError。若为200不做任何操作，程序继续往下执行

	content_type = get_response.headers.get('Content-Type', '')  # 文件类型
	file_size = int (get_response.headers.get('Content-length', 0)) # 文件大小
	print(f'文件类型: {content_type} , 文件大小：: {file_size/1024} KB')

	if 'image' in content_type and file_size < 1024 * 1024:  # stream=True仅下载响应头，可从headers中获取信息，来预先判断文件，再决定是否开始下载
		print('开始下载....')
		download_size = 0
		with open(os.path.join(abs_path, file_base_name), 'wb') as f:
			# 方式一： 通过高层API response.iter_content
			iter_result = get_response.iter_content(chunk_size=1024*100) # 每次读取 100kb。 默认1字节
			for chunk in iter_result:
				if chunk:   # 过滤空块，避免写入无效数据
					download_size+=len(chunk)
					f.write(chunk)
					print(f'下载进度：{(download_size / file_size ) * 100 :.2f}%') # .2f 浮点数格式化，f表示格式化类型为浮点数、2表示四舍五入保留2位小数


			# 方式二： 通过底层API raw.read
			# get_response.raw.decode_content = True
			# raw_read_res = get_response.raw.read(1024 * 100)
			# while raw_read_res:
			# 	download_size += len(raw_read_res)
			# 	f.write(raw_read_res)
			# 	print(f'下载进度：{(download_size / file_size) * 100 :.2f}%')
			# 	raw_read_res = get_response.raw.read(1024 * 100)

			# 方式三： 工具类
			# get_response.raw.decode_content = True
			# shutil.copyfileobj(get_response.raw, f)
		print('下载完成')
	else:
		print('文件类型/文件大小不符，取消下载')