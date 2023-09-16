# js漏洞挖掘技巧



https://forum.butian.net/share/1441

第二点就是如何找接口，通过ctrl+F搜索path: '，就能看到他的路由配置或者直接搜routes或者home以及url,ajax,path等。

还有就是有的js下面会配置POST包或者GET包参数，如果POST就是data，GET就是params，不像这次这么简单直接访问就把参数补齐了



# 一些工具

## burpsuite

使用bp专业版可以对目标做脚本探针

![image-20220311095050476](./image/image-20220311095050476.png)

![image-20220311095138980](./image/image-20220311095138980.png)

可以复制，也可以将所有js导出到本地文本

![image-20220311095205111](./image/image-20220311095205111.png)



另外对主页或者功能点等浏览过后，在HTTP history这里也可以过滤js文件

![image-20220311094909321](./image/image-20220311094909321.png)

## LinkFinder

https://github.com/GerbenJavado/LinkFinder

python3环境

```bash
python3 linkfinder.py -i https://www.zut.edu.cn -d -o cli
```

![image-20220311092804875](./image/image-20220311092804875.png)



## JsFinder

https://github.com/Threezh1/JSFinder

python3环境

简单爬取：

```
python3 JSFinder.py -u https://www.jd.com/
```

![image-20220311095634980](./image/image-20220311095634980.png)

![image-20220311095650128](./image/image-20220311095650128.png)

深度爬取：

```
python3 JSFinder.py -u https://www.jd.com/ -d -ou jd_url.txt -os jd_domain.txt
```

结果保存到本地

![image-20220311095904604](./image/image-20220311095904604.png)

![image-20220311095934706](./image/image-20220311095934706.png)