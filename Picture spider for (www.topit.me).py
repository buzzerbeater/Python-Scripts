# -*- coding: utf-8 -*-	
from BeautifulSoup import BeautifulSoup
import urllib2,re,time,datetime,socket

url_initial = raw_input("请输入第一页的网址:")
#Page=input("请输入页数:")

starttime = datetime.datetime.now()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}#伪装成浏览器



#取出专辑的页数
Page_request_1 = urllib2.Request(url_initial, headers=headers)
try:
	Page_request_2 = urllib2.urlopen(Page_request_1, timeout=10)
except urllib2.HTTPError,e:
	print e.code
	print "first"
#	continue
except socket.timeout, e:  
	print "----------socket timoutwww:"
#	continue
except urllib2.URLError,e:
	print "URLError"
#	continue
try:
	Page_data = Page_request_2.read();
except socket.timeout, e:  
    print("----------socket timoutwww_111")

Page_soup=BeautifulSoup(Page_data)
Page_tag=Page_soup.findAll(attrs={'id':'page-next'})[0]
Page=int(Page_tag.previous)
print "专辑共有："+str(Page)+"页"

#取出专辑的页数
Count=96
Page_1 = range(1,Page+1)
url_a = []
for P in Page_1:	
	url_a.append(url_initial+'?p='+str(P))
	print url_a[P-1]
data_a = []
soup = []




for P in Page_1:
	print 'Page'+str(P)
	data_a_resp_1 = urllib2.Request(url_a[P-1],headers=headers)
	try:              	                        
		data_a_resp_2 = urllib2.urlopen(data_a_resp_1,timeout=10);               
	except urllib2.HTTPError,e:
		print e.code
		print "first"
		continue
	except socket.timeout, e:  
		print "----------socket timoutwww:"
		continue
	except urllib2.URLError,e:
		print "URLError"
		continue
	try:
		data_a_resp = data_a_resp_2.read();
	except socket.timeout, e:  
	    print("----------socket timoutwww_111")
	
	data_a.append(data_a_resp) 
	soup.append(BeautifulSoup(data_a[P-1]))
	alltags = soup[P-1].findAll(attrs={'class':'img'}) 
	url_b = []

	for tag in alltags:
#		print tag.parent    #有的时候要找parent/next
		url_b.append(str(tag.parent.attrMap['href']))
	M = 0
	data_b = []
	url_c = []
	soup_b = []
	
	for x in url_b:
		print "一级网址："+str(M+1)+' '+x
		data_b_resp_1 = urllib2.Request(x,headers=headers)
		try:              	                        
			data_b_resp_2 = urllib2.urlopen(data_b_resp_1,timeout=10)          
		except urllib2.HTTPError,e:
			print e.code
			print "first"
			continue
		except socket.timeout, e:  
			print "----------socket timoutwww:"
			continue
		except urllib2.URLError,e:
			print "URLError"
			continue
			
		try:
			data_b_resp = data_b_resp_2.read();
		except socket.timeout, e:  
		    print("----------socket timoutwww_111")
		data_b.append(data_b_resp)
		soup_b.append(BeautifulSoup(data_b[M]))
		tags_b=soup_b[M].find(attrs={'id':'item-tip'})
		if tags_b==None:
			print "Opps!!!!"
		else:
			tags_b.attrMap
			url_c.append(str(tags_b['href']))
			print '二级网址: '+str(M+1)+' '+url_c[M]
			M=M+1
	N=0	
	for url_d in url_c:
		Count=Count+1                                 #count以前放在下面导致出错后下一张图覆盖掉前一张。放前面就没有这种事儿。
		print str(Count)+' '+url_d                    #A 这里到下面A可以防止页面重定向
		req = urllib2.Request(
		    url = url_d,
		    headers = headers
		)
		try:              	                          #这里使用try和except来处理异常非常重要。有一个图片缺失，导致http404。
			resp = urllib2.urlopen(req, timeout = 10);   #timeout 参数的运用可以防止有些页面请求超时导致图片缺失 
		except urllib2.HTTPError,e:
			print e.code
			print "first"
		except socket.timeout, e:  
	   		print "----------socket timout1:"
		except urllib2.URLError,e:
			print "URLError"
			continue
#		realUrl = resp.geturl();    
#		url = str(realUrl);                          #A 这里可以防止页面重定向
#		req = urllib2.Request(url);
#		try:              	
#			resp = urllib2.urlopen(req, timeout = 10);             #这里使用try和except来处理异常非常重要。若有图片缺失，导致http404。  
#		except urllib2.HTTPError,e:
#			print e.code
#			print "second"
#			continue
#		except socket.timeout, e:  
#		    print "----------socket timout2:"
#		    continue
		try:
			respHtml = resp.read();
		except socket.timeout, e:  
		    print("----------socket timout3:")
		    continue 
		binfile = open('/Users/a/desktop/aaa/少女馆'+str(Count)+'.jpg', "wb");  #文件路径
		binfile.write(respHtml);
		binfile.close();

		
endtime = datetime.datetime.now()

print '抓取完成!用时:'+str((endtime-starttime).seconds)

	
	
