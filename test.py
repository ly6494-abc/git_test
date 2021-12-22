import requests

url = 'http://www.baidu.com'
data = requests.get(url).content.decode("utf-8")
print(data)

print('welcome to my world!')

for i in range(1, 10):
	print(i)


print('bug修复！')

	
print("dev功能测试--100%")

