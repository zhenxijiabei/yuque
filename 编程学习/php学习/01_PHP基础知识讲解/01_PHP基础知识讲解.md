# 0x00环境配置

给apache配置虚拟主机

```
<VirtualHost *:80>

	#域名配置，每个虚拟主机都有一个域名对应
	ServerName localhost
	
		#设定网站目录
		DocumentRoot "E:/Program Files (x86)/wamp/www/"
		
		#给目录设定访问权限
		<Directory "E:/Program Files (x86)/wamp/www/">
			Order Deny,Allow
			Allow from all
		</Directory>
		
	#给默认的首页
	Options Indexes FollowSymLinks
</VirtualHost>


<VirtualHost *:80>
	ServerName www.z.com
		DocumentRoot "E:/Program Files (x86)/wamp/www/www.z.com"
		<Directory "E:/Program Files (x86)/wamp/www/www.z.com">
		Order Deny,Allow
		Allow from all
		</Directory>
	#给默认的首页
	Options Indexes FollowSymLinks
</VirtualHost>


<VirtualHost *:80>
	ServerName www.d.com
		DocumentRoot "E:/Program Files (x86)/wamp/www/www.d.com"
		<Directory "E:/Program Files (x86)/wamp/www/www.d.com">
		Order Deny,Allow
		Allow from all
		</Directory>
	#给默认的首页
	Options Indexes FollowSymLinks
</VirtualHost>



<VirtualHost *:80>
	ServerName www.k.com
		DocumentRoot "E:/Program Files (x86)/wamp/www/www.k.com"
		<Directory "E:/Program Files (x86)/wamp/www/www.k.com">
		Order Deny,Allow
		Allow from all
		</Directory>
	#给默认的首页
	Options Indexes FollowSymLinks
</VirtualHost>
```

![image-20230102133536191](./image/image-20230102133536191-1688000689983-79.png)

![image-20230102133547750](./image/image-20230102133547750-1688000689983-80.png)

# 0x01前端知识

html标签

div+css

bootstrap	插件全部依赖jquery

https://v3.bootcss.com/

![image-20221205225627184](./image/image-20221205225627184.png)

使用之前需要导入三个文件

![image-20221205225400072](./image/image-20221205225400072-1688000689983-81.png)



# 0x02PHP基础

## 常用

### 注释

//单行注释	或者使用 #当行注释

/*
多行注释
*/

;分号结尾

### 三个常用函数

- isset()

    范围布尔型结果

- gettype()

    返回变量类型

- var_dump()

    详细输出变量类型

## 变量类型

![image-20221207105706930](./image/image-20221207105706930.png)

## 运算符

i++

	//前++ 先+1，再运算
	//后++ 先运算，后+1

===恒等于	表示数值部分相等，同时满足类型相等

三元运算符	？：

```php
$a = 20;
$b = 10;
echo $a>$b?"a大于b":"a小于b";
```

![image-20221207111817556](./image/image-20221207111817556.png)

![image-20221207111744778](./image/image-20221207111744778.png)

## 三大控制结构

![image-20221207151607152](./image/image-20221207151607152.png)

### if else

```php
$a = 20;

if ($a>0) {
	echo "a>0";
}else{
	echo "a<0";
}
```

```php
if ($a>0) {
	echo "a>0";
}else if($a>1){
	echo "a>1";
}else if ($a>3) {
	echo "a>3";
}else{
	echo "xxx";
}
echo "<hr />";	//换行
```

### switch

![image-20221207150245235](./image/image-20221207150245235-1688000689984-82.png)

![image-20221207150140990](./image/image-20221207150140990.png)

### while

![image-20221207150443345](./image/image-20221207150443345.png)

### for

![image-20221207150730578](./image/image-20221207150730578.png)

### do while

先执行，再判断

![image-20221207151204604](./image/image-20221207151204604.png)

### break

跳出整个循环

![image-20221207151856016](./image/image-20221207151856016.png)

### continue

略过本次循环，继续执行后续循环

![image-20221207151920268](./image/image-20221207151920268.png)

## 字符串详解

### 单引号双引号区别

1、单引号和双引号都可以定义变量

2、单引号' 和双引号" 主要区别：

- 双引号解释变量，单引号不解析

![image-20221207152818584](./image/image-20221207152818584.png)

- 双引号转义，单引号不转义

![image-20221207152609373](./image/image-20221207152609373.png)

### 字符串常用函数

可以参见：PHP7中文手册(2018)

#### strlen

查看字符串长度

![image-20221207153621921](./image/image-20221207153621921.png)

注：一个汉字占用三个字符，英文和数字各占一个字符

#### mb_strlen

计算真实字符个数

![image-20221207154015431](./image/image-20221207154015431.png)

#### strpos

查找字符串首次出现的位置

```php
echo strrpos("www.baidu.com","bai");
```

stripos	对比strpos不区分大小写

strrpos	对比strpos指最后一次出现位置

#### str_replace

字符串替换

![image-20221207155147178](./image/image-20221207155147178.png)

#### strstr

查找字符串的首次出现

![image-20221207155651684](./image/image-20221207155651684-1688000689996-83.png)

#### substr

返回字符串的子串

![image-20221207160408304](./image/image-20221207160408304-1688000689996-84.png)

#### strrchr

查找指定字符在字符串中的最后一次出现

![image-20221207160930109](./image/image-20221207160930109.png)

#### explode

使用一个字符串分割另一个字符串，返回数组

打印数组可以使用var_dump和print_r，推荐使用print_r

![image-20221207164016125](./image/image-20221207164016125.png)

#### implode

将一个一维数组的值转化为字符串

![image-20221207162518598](./image/image-20221207162518598.png)

#### trim

去除字符串首尾处的空白字符（或者其他字符）

![image-20221207181857973](./image/image-20221207181857973-1688000689997-85.png)

ltrim

去除字符串左边空白字符（或者其他字符）

rtrim

去除字符串右边空白字符（或者其他字符）

#### addslashes

使用反斜线引用字符串，防注入

![image-20221207182417172](./image/image-20221207182417172-1688000689997-86.png)

#### mysql_real_escape_string

在以下字符前添加反斜杠: `\x00`, `\n`, `\r`, `\`, `'`, `"` 和 `\x1a`.



#### htmlspecialchars

将特殊字符转换为 HTML 实体，防xss

![image-20221207182632654](./image/image-20221207182632654-1688000689997-87.png)



## 数组

可以使用print_f() 或者var_dump()打印数组

### 索引数组

![image-20221207183234159](./image/image-20221207183234159.png)

### 关联数组

![image-20221207183057437](./image/image-20221207183057437.png)

### 数组遍历

![image-20221207192218187](./image/image-20221207192218187.png)



### 数组增删改查

![image-20221207192508597](./image/image-20221207192508597.png)



## 函数和超全局变量

### php函数

![image-20221207193102215](./image/image-20221207193102215.png)

### GLOBALS

var_dump($GLOBALS);	//超全局数二维数组，打印所有变量信息

### _SERVER

var_dump($_SERVER);	//服务器和客户端信息

![image-20221207194348340](./image/image-20221207194348340.png)

### _GET

![image-20211215171950451](./image/image-20211215171950451-1688000689998-88.png)

```php
<?php 

	function getAdd($a,$b){
		return $a+$b;
	}

	if (empty($_GET)) {
		echo "no get";
	}else{
		$x= $_GET['a1'];
		$y= $_GET["b1"];
		echo getAdd($x,$y);
	}
```

### _POST

![image-20211215172016490](./image/image-20211215172016490.png)

![image-20211215172025872](./image/image-20211215172025872-1688000689998-89.png)

test.php

```php+HTML
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>测试POST</title>
</head>
<body>

<form action="test2.php" method="post">
	表单1:<input type="text" name="a" /><br><br>
	表单2:<input type="text" name="b" /><br><br>	
	<input type="submit" name="提交">

</form>

</body>
</html>
```

test2.php

```php
<?php 

	if(empty($_POST)){
		echo "no POST";
	}else{
		$a = $_POST["a"];
		$b = $_POST["b"];
		echo "$a ---- $b";
	}
```



## 变量和作用域

### 超全局变量

如GLOBALS、_SERVER、_GET、_POST

![image-20221207201717650](./image/image-20221207201717650.png)

### 全局变量和局部变量

函数内外之分

可以使用global调用全局变量

![image-20221207201629648](./image/image-20221207201629648.png)



## 会话技术

cookie

![image-20221207205130109](./image/image-20221207205130109.png)

session

![image-20221207210317530](./image/image-20221207210317530.png)

## 登录测试

![image-20211215172044655](./image/image-20211215172044655.png)

![image-20211215172053915](./image/image-20211215172053915.png)

![image-20211215172106281](./image/image-20211215172106281.png)

## 文件操作

### 	文件包含

![image-20211215171700662](./image/image-20211215171700662-1688000690000-90.png)

require 报错中止执行

include 报错继续执行

![image-20211215172143155](./image/image-20211215172143155-1688000690000-91.png)

![image-20211215172151450](./image/image-20211215172151450-1688000690000-92.png)

### 文件上传

```php
echo __DIR__;	//打印当前文件所在目录
echo dirname(__DIR__);	//打印当前文件所在上一层目录
```

#### 测试文件上传1

![image-20211215172227522](./image/image-20211215172227522.png)

![image-20211215172234703](./image/image-20211215172234703-1688000690000-93.png)

#### 测试文件上传2

![image-20211215172248116](./image/image-20211215172248116-1688000690000-94.png)

![image-20211215172305827](./image/image-20211215172305827.png)

### 文件管理常用函数

#### realpath

效果同

```php
echo __DIR__;	//打印当前文件所在目录
```

![image-20221207230629296](./image/image-20221207230629296-1688000690001-95.png)

同样可以打印上级，或者上上级目录等

```php
echo realpath("..");	//打印上级目录
echo realpath("../../");	//打印上上级目录
```

#### opendir

打开目录路径

#### readdir

读取目录路径

![image-20221207231450000](./image/image-20221207231450000.png)

#### closedir

关闭资源

```php
$fileName = opendir(".");
while ($row = readdir($fileName)) {
	echo $row."<br/>";
}
closedir($fileName);
```

#### is_dir

判断是否是路径

![image-20221207231822961](./image/image-20221207231822961.png)

#### unlink

删除文件

```php
unlink("123.txt")
```

#### file_get_contents

从文件中读取内容

file_get_contents(filename)	#从文件中读取内容

![image-20221207232844623](./image/image-20221207232844623.png)

#### file_put_contents

向文件中写入内容

### 遍历目录

![image-20221207230114484](./image/image-20221207230114484.png)