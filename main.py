#-*-coding:utf-8-*-

import requests

from bs4 import BeautifulSoup
from time import sleep

pageNum=1;
while True:
	page=requests.get("https://anime-chan.me/page/%s/"%pageNum);
	data=page.text;
	body=BeautifulSoup(data, "lxml");
	for post in body.find("div", {"id":"dle-content"}).findChildren("div", {"class":"ss"}):
		ttlA=post.find("div", {"class":"ss_title_short"}).find("a");
		title=ttlA.text;
		url=ttlA["href"];
		posterA=post.find("b", {"class":"user"}).find("a");
		posterName=posterA.text;
		posterUrl=posterA["href"];
		category=post.find("b", {"class":"category"}).find("a").text;
		id=url[url.rfind(u"/")+1:];
		id=id[:id.find(u"-")];
		contentUrls=[];
		print(id);
		contentContainer=post.find("div", {"id":"news-id-%s"%id});
		for img in contentContainer.findChildren("img"):
			contentUrls.append(img["src"]);
		for iframe in contentContainer.findChildren("iframe"):
			contentUrls.append(iframe["src"]);
	if(not(body.find("div", {"class":"navigation"}).findChildren()[-1].has_attr("href"))):
		break;
	pageNum=pageNum+1;
	sleep(2);
