from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve

html = urlopen("https://www.youtube.com/")
obj = bf(html.read(),'html.parser')
title = obj.head.title
print(title)

pic_info = obj.find_all('img',alt="")
#pic_info = obj.find_all('img')
#for i in pic_info:
 #   print(i)
image_url = "https:"+pic_info[8]['src']
print(image_url)
urlretrieve(image_url, 'imageTest.png')
