import requests

url = 'http://www.baidu.com'
data = requests.get(url).content.decode("utf-8")
print(data)

print('welcome to my world!')