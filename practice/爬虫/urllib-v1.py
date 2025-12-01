from urllib import request, parse
import json

url = "http://www.baidu.com"
# response = request.urlopen(url, timeout=5)
# print(response.read().decode('utf-8'))


# Get请求
base_url = 'https://httpbin.org/'
params = {'username': 'jay', 'city': '北京'}
params_encode = parse.urlencode(params, encoding='utf-8')

full_url = f'{base_url}/get?{params_encode}'
print('Get 请求地址:{}'.format(full_url))

# try:
	# response = request.urlopen(full_url, timeout=5)
	# decode_result = response.read().decode('utf-8')  # read() 返回是bytes 字节流，decode() 转为字符串
	# response_json = json.dumps(json.loads(decode_result), ensure_ascii=False, indent=4)
	# print(response_json)

# except Exception as e:
# 	print(f'Get 请求失败，报错:{e}')



# Post 请求
post_data = {"song": '一首歌的时间', 'artist': 'Jay',"hobby": ["reading", "coding"]}

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"  # 可选：模拟浏览器请求
}

headers_body = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"  # 可选：模拟浏览器请求
}

base_url_post = f'{base_url}/post'
try:
	# POST 表单形式提交
	param_encode = parse.urlencode(post_data).encode('utf-8')  # 调用 encode() 方法，将字符串转为bytes字节流
	# param_encode =bytes( parse.urlencode(post_data),'utf-8')  # 调用 encode() 方法，将字符串转为bytes字节流
	request_post = request.Request(url=base_url_post, headers=headers, data=param_encode, method="POST")
	response = request.urlopen(request_post, timeout=5)
	print(f'表单形式返回结果：{json.dumps(json.loads(response.read().decode('utf-8')), indent=2, ensure_ascii=False)}')

	# POST body 提交
	json_data = json.dumps(post_data).encode('utf-8')  #将字典转为json字符串，encode转为bytes字节流
	request_post_body = request.Request(url=base_url_post, headers=headers_body, data=json_data, method="POST")
	response_2 = request.urlopen(request_post_body, timeout=5)
	print(f'body形式返回结果：{json.dumps(json.loads(response_2.read().decode('utf-8')), indent=2, ensure_ascii=False)}')

except Exception as e:
	print(f'POST 请求失败，报错：{e}')
