import requests
from bs4 import BeautifulSoup as bs
import os

#Getting search
search = raw_input('Search : ')
search = search.replace(" ","%20")

#Creating url from search
url = 'https://www.pexels.com/search/'+search+'/'

#Download page
page = requests.get(url)
soup = bs(page.text,'html.parser')

#Locate all elements with image tag
image_tags = soup.findAll('img')

#changing the directory name for better reading
dirName = search.replace('%20',"_")

#Creating new directory if not exists
if not os.path.exists(dirName):
    os.makedirs(dirName)

#Changing the directory
os.chdir(dirName)

x = 0

for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass