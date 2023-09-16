## 前言

Upload-labs是一个帮你总结所有类型的上传漏洞的靶场，包括常见的文件上传漏洞，项目地址：

`https://github.com/c0ny1/upload-labs`

先看下GitHub上的总结：



**1、靶机包含漏洞类型分类**

![upload-labs.png](./image/upload-labs.png)

**3.2 如何判断上传漏洞类型?**

![sum_up.png](./image/sum_up.png)



## 第一关

查看源代码，调用的前端js限制上传文件类型

![image-20220210200504206](./image/image-20220210200504206.png)

先将php文件命名为.jpg文件，然后上传，抓包修改文件后缀名为.php文件，forword即可。鼠标右键查看图片源码，找到php文件路径，木马连接

![image-20220210200821939](./image/image-20220210200821939.png)

## 第二关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        if (($_FILES['upload_file']['type'] == 'image/jpeg') || ($_FILES['upload_file']['type'] == 'image/png') || ($_FILES['upload_file']['type'] == 'image/gif')) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH . '/' . $_FILES['upload_file']['name']            
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '文件类型不正确，请重新上传！';
        }
    } else {
        $msg = UPLOAD_PATH.'文件夹不存在,请手工创建！';
    }
}
```

上传phpinfo2.php文件，抓包，修改Content-Type内容为 `Content-Type: image/jpg`

![image-20220211005443531](./image/image-20220211005443531.png)

forward，访问上传文件

![image-20220211005655236](./image/image-20220211005655236.png)

另外，这一关也可以通过上传phpinfo.png抓包修改为phpinfo.php，因为上传后缀为png时候，这时候

Content-Type默认会是image/png

## 第三关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array('.asp','.aspx','.php','.jsp');
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //收尾去空

        if(!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;            
            if (move_uploaded_file($temp_file,$img_path)) {
                 $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '不允许上传.asp,.aspx,.php,.jsp后缀文件！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

直接上传php文件，提示：==不允许上传.asp,.aspx,.php,.jsp后缀文件！== 

可以知道是黑名单限制了后缀名，可以尝试用php3，phtml绕过

![image-20220211090123795](./image/image-20220211090123795.png)

![image-20220211085600101](./image/image-20220211085600101.png)

前提是apache的`httpd.conf`中有如下配置代码

```php
AddType application/x-httpd-php .php .phtml .phps .php5 .pht .php7等
```

![image-20220211091339123](./image/image-20220211091339123.png)



## 第四关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2","php1",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2","pHp1",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //收尾去空

        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件不允许上传!';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

这一关，可以看到几乎过滤了所有的可利用的文件类型，但是没有过滤`.htaccess`，可以上传一个`.htaccess`文件，内容如下：

```
SetHandler application/x-httpd-php
```

![image-20220211095923684](./image/image-20220211095923684.png)

然后上传后缀为jpg的图片马，也可以正常解析了

![image-20220211100032238](./image/image-20220211100032238.png)

## 第五关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //首尾去空

        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件类型不允许上传！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

同第四关，限制了各种后缀，同时加上了 `.htaccess` ，但是没有对大小写，直接上传.pHP文件

![image-20220211102554896](./image/image-20220211102554896.png)

## 第六关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess");
        $file_name = $_FILES['upload_file']['name'];
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;
            if (move_uploaded_file($temp_file,$img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件不允许上传';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

这关还是黑名单，但是没有对后缀名进行去空处理，可在后缀名中加空绕过：

windows下`xx.jpg[空格] 或xx.jpg.`这两类文件都是不允许存在的，若这样命名，windows会默认除去空格或点此处会删除末尾的点，但是没有去掉末尾的空格，因此上传一个`.php空格`文件即可。

![image-20220211104516013](./image/image-20220211104516013.png)

![image-20220211104527789](./image/image-20220211104527789.png)

## 第七关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //首尾去空
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.$file_name;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件类型不允许上传！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

对比第六关没有去除文件名末尾的点

![image-20220211105239669](./image/image-20220211105239669.png)

![image-20220211105211631](./image/image-20220211105211631.png)

## 第八关

```php
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = trim($file_ext); //首尾去空
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件类型不允许上传！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

NTFS文件系统包括对备用数据流的支持。这不是众所周知的功能，主要包括提供与Macintosh文件系统中的文件的兼容性。备用数据流允许文件包含多个数据流。每个文件至少有一个数据流。在Windows中，此默认数据流称为：`$ DATA`。上传`.php::$DATA`绕过。(仅限windows)

![image-20220211110756630](./image/image-20220211110756630.png)

![image-20220211110839590](./image/image-20220211110839590.png)

## 第九关

对比上面有个明显的一点就是这里用上传的文件名作为上传后的文件名，未重新命名。

![image-20220211112159130](./image/image-20220211112159130.png)

可以利用第7行和第11行，去末尾点和空的方法绕过

![image-20220211112532864](./image/image-20220211112532864.png)

![image-20220211113048532](./image/image-20220211113048532.png)

## 第十关

![image-20220211113129407](./image/image-20220211113129407.png)

覆写绕过

![image-20220211144944210](./image/image-20220211144944210.png)

![image-20220211144911747](./image/image-20220211144911747.png)

## 第十一关

![image-20220211145448008](./image/image-20220211145448008.png)

第8行，`save_path`参数可控，使用%00截断

![image-20220211150135290](./image/image-20220211150135290.png)

![image-20220211150603860](./image/image-20220211150603860.png)

## 第十二关

![image-20220211150815455](./image/image-20220211150815455.png)

不同于第十一关，第7行save_path参数是用POST方式传递的，这里需要对%00进行url解码，因为POST不会像GET对%00进行自动解码

![image-20220211151528898](./image/image-20220211151528898.png)

解码后

![image-20220211151759445](./image/image-20220211151759445.png)

![image-20220211151328655](./image/image-20220211151328655.png)

## 第十三关

![image-20220211160416177](./image/image-20220211160416177.png)

通过读文件的前2个字节判断文件类型，因此直接上传图片马即可，制作方法：

```powershell
copy hacker.png/b+phpinfo.php/a muma.png
```

![image-20220211160607033](./image/image-20220211160607033.png)

利用文件包含拿到webshell

![image-20220211160513519](./image/image-20220211160513519.png)

## 第十四关

![image-20220211161111956](./image/image-20220211161111956.png)

利用getimagesize()函数获取图像类型，同第十三关，制作图片马

![image-20220211161215610](./image/image-20220211161215610.png)

## 第十五关

![image-20220211161330583](./image/image-20220211161330583.png)

利用php_exif模块来判断文件类型，同样可以利用图片马就可进行绕过：

![image-20220211161432737](./image/image-20220211161432737.png)

## 第十六关

![image-20220211162711072](./image/image-20220211162711072.png)

本关综合判断了后缀名、content-type，以及利用imagecreatefromjpg判断是否为jpg图片，最后再做了一次二次渲染，绕过方法：

同样用上面的图片马方法可以绕过

![image-20220211162729777](./image/image-20220211162729777.png)

另外制作gif图片马好像更为简单

![image-20220211163358092](./image/image-20220211163358092.png)

![image-20220211163431157](./image/image-20220211163431157.png)

## 第十七关

![image-20220211172008079](./image/image-20220211172008079.png)

可以看到文件先经过保存，然后判断后缀名是否在白名单中，如果不在则删除，此时可以利用条件竞争在保存文件后删除文件前来执行php文件

![image-20220211230457742](./image/image-20220211230457742.png)

此时回在upload目录下，不断有phpinfo.php文件出现消失，证明利用该漏洞上传成功了。

另外可以不断抓包请求  `./upload/phpinfo.php`证明上传成功了，只不过很快被删了

## 第十八关

![image-20220211231002170](./image/image-20220211231002170.png)

![image-20220211231228967](./image/image-20220211231228967.png)

本关对文件后缀名做了白名单判断，然后会一步一步检查文件大小、文件是否存在等等，将文件上传后，对文件重新命名，同样存在条件竞争的漏洞。可以不断利用burp发送上传图片马的数据包，由于条件竞争，程序会出现来不及rename的问题，从而上传成功：

![image-20220211231840887](./image/image-20220211231840887.png)

选择空payload，进行爆破

![image-20220211232124083](./image/image-20220211232124083.png)

可以在www下面看到有些还未来得及重命名的文件，因此我们可以通过条件竞争来上传图片马。

![image-20220211232244646](./image/image-20220211232244646.png)

## 第十九关

![image-20220211232813079](./image/image-20220211232813079.png)

发现move_uploaded_file()函数中的img_path是由post参数save_name控制的，因此可以在save_name利用%00截断绕过：

![image-20220212000041977](./image/image-20220212000041977.png)

![image-20220212000133547](./image/image-20220212000133547.png)

另外move_uploaded_file会忽略掉文件末尾的`/.`	因此构造save_name参数为 `upload-19.phpjpg/.` 也是可以的

## 第二十关

![image-20220211234117990](./image/image-20220211234117990.png)

可以发现`$file_name`经过`reset($file) . '.' . $file[count($file) - 1];`处理。

如果上传的是数组的话，会跳过`$file = explode('.', strtolower($file));`。并且后缀有白名单过滤

```php
$ext = end($file);
$allow_suffix = array('jpg','png','gif');
```

而最终的文件名后缀取的是`$file[count($file) - 1]`，因此我们可以让`$file`为数组。`$file[0]`为`upload-20.php/`，也就是`reset($file)`，然后再令`$file[2]`为白名单中的jpg。此时`end($file)`等于jpg，`$file[count($file) - 1]`为空。而 `$file_name = reset($file) . '.' . $file[count($file) - 1];`，也就是`upload-20.php/.`，最终`move_uploaded_file`会忽略掉`/.`，最终上传`upload-20.php`。

![image-20220211235414622](./image/image-20220211235414622.png)

![image-20220211235459550](./image/image-20220211235459550.png)