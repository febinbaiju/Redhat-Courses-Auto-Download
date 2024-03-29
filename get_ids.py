from bs4 import BeautifulSoup
import os
import re
from driver import fetch_and_download_raw

datasource = "datasource.txt"
parser = 'html.parser'

fd = os.open(datasource, os.O_RDONLY)
doc = os.read(fd, int(os.path.getsize(datasource)))
soup = BeautifulSoup(doc, parser)

limit = 100
find_li = soup.find_all('li', attrs={'id' : re.compile('0_[a-z0-9]+')})
total = len(find_li)
counter = 0
for element in find_li:
    counter = counter + 1
    if element and counter <= limit:
        _id = str(element.get('id'))
        title_find = element.find('span')
        _title = str(counter)+" "+str(title_find.text)
        fetch_and_download_raw(_id, _title)
        print(_id)
        print(_title)
        print("Downloaded "+str(counter)+" of "+str(total)+" files...")
