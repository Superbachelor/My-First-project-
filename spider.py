#-*-codeing = utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

def askurl(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def getData(baseurl):
    datelist = []
    x=0
    for i in range(0,10):
        url = baseurl+str(i*25)
        html = askurl(url)
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            item = str(item)
            findlink = re.compile(r'<a href="(.*?)">')
            link = re.findall(findlink, item)[0]
            datelist.append(link)

    return datelist

def datasave(datalist,path) :
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet()


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datelist = getData(baseurl)
    savepath= "豆瓣电影TOP250.xls"
    print(len(datelist))




if __name__ == '__main__':
    main()