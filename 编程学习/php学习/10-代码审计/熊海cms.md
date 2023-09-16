## 0x01环境

- xhcms_v1.0源码

- windows 10

- phpstudy2016（php 5.2）

- seay源代码审计系统

      

## 0x02漏洞列表

### 1、文件包含

使用seay源代码审计到index.php可能存在文件包含漏洞

![image-20211216163345207](./image/image-20211216163345207.png)

分析index.php文件，传递r变量

![image-20211216164026815](./image/image-20211216164026815.png)

这里顺带说一下**三目运算符**

![image-20211216103245970](./image/image-20211216103245970.png)



> **绕过方法1：%00 截断**
>
> 条件：magic_quotes_gpc = Off，PHP版本<5.3.4
>
> **绕过方法2：路径长度截断**
>
> 条件：windows 下目录路径最大长度为256字节，超出部分将丢弃；linux 下目录最大长度为4096字节，超出长度将丢弃；PHP版本<5.2.8



![image-20211216094418310](./image/image-20211216094418310.png)

在网站根目录写一个1.php的文件，打印echo 111;

![image-20211216164258288](./image/image-20211216164258288.png)

由于这里拼接后缀名是php，此处页可以不加后罪名php，也可以实现

![image-20211216164357253](./image/image-20211216164357253.png)

### 2、XSS跨站

如果是前端js验证，首先输入正确的文件类型或者格式，再通过burpsuite抓包修改成需要的xss

一般是注册位置或者修改资料等，这里在留言处抓包

![image-20211216200444801](./image/image-20211216200444801.png)

通过post提交数据，定位提交到files/submit.php文件，再次定位到message参数

![image-20211216200558082](./image/image-20211216200558082.png)

通过一番查看，未发现过滤，进行xss测试



![image-20211216200928662](./image/image-20211216200928662.png)

环境问题这里未实现弹窗，正常是可以弹窗的。。。



### 3、越权漏洞

通过审计发现checklogin.php存在一个垂直越权漏洞：

![image-20211216165621752](./image/image-20211216165621752.png)

使用firebar新建一个user字段你的cookie

![image-20211216104322549](./image/image-20211216104322549.png)

如访问http://127.0.0.1/xh/admin/?r=newwz ，该页面是登录才可以访问的页面，此时通过添加cookie的user字段，即成功越权登录

![image-20211216165837050](./image/image-20211216165837050.png)





### 4、报错注入

登录位置存在报错注入

![image-20211216193639424](./image/image-20211216193639424.png)

![image-20211216104700438](./image/image-20211216104700438.png)

![image-20211216104820897](./image/image-20211216104820897.png)

![image-20211216104844022](./image/image-20211216104844022.png)



参考：

https://www.cnblogs.com/wkzb/p/12805100.html

https://www.cnblogs.com/richardlee97/p/10600103.html