API_TOKEN='947a41f7222ad3a385c6998c3739f23368ea6490'
GIT_API_URL='https://api.github.com'

import requests


#url1='https://api.github.com'
username=raw_input("Enter the User Github_User_Name: ")

url='https://api.github.com/users/'+username+'/repos'
#print url
#fields = "id,name,birthday"
fields = "id"
limit=4

url = '%s?access_token=%s' % \
    (url,API_TOKEN,)
#print url
r = requests.get(url).json()
#print r
#print type(r)
for data in r:
	print data["full_name"]
