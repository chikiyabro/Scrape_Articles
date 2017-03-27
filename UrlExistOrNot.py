import requests

request = requests.head('https://www.thenews.com.pk/latest/category/sports/2015-09-22')
print(request.status_code)
if request.status_code == 307:  ## code for temporary redirect
    print('Web does not site exists')
else:
    print('Web site exist')