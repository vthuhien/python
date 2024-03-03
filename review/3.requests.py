import requests
# demo1
response = requests.get('https://api.github.com')
# print(response.text)
# print(response.json())
# print(response.json()['current_user_url'])
# print('headers',response.headers['content-type']) 

# demo2 - query string parameters
# response2 = requests.get('https://api.github.com',params={'q':'value'})
# response2 = requests.get('https://api.github.com?q:value')
# print(response2)

# demo3 - thay đổi requests header
# response = requests.get('https://api.github.com',
#                         params={'q':'value'},
#                         headers={'coockie':'test'})
# print(response)

# demo4 - các phương thức http
# 1.GET
requests.get('https://api.github.com')
# 2.POST
requests.post('https://api.github.com',data={'key':'value'})
test = requests.post('https://api.github.com',data={'name':'thuhien','age':'15'})
print(response.text)

test = requests.post('https://api.github.com',json={'name':'thuhien','age':'15'})
print(response.text)