from bs4 import BeautifulSoup
import os
import re

fd = os.open('datasource.txt',os.O_RDONLY)
doc = os.read(fd, int(os.path.getsize('datasource.txt')))

soup = BeautifulSoup(doc,'html.parser')
find_li = soup.find_all('li', attrs={'id':re.compile('0_[a-z0-9]+')})
print(len(find_li))