## 0x01设置启动指定目录

文件->偏好设置->通用->启动选项

![image-20211231180238682](./image/image-20211231180238682.png)



## 0x02修改代码字体大小

找到**codemirror.css**文件

![image-20211215214129650](./image/image-20211215214129650.png)

找到**font-size**，这里我修改为16px

![image-20211215214204436](./image/image-20211215214204436.png)



## 0x03修改字体

![image-20211215205023742](./image/image-20211215205023742.png)

![image-20211215205055659](./image/image-20211215205055659.png)

找到对应的主题，如这里我修改为微软雅黑**Microsoft YaHei** ，英文修改为新罗马**Times New Roman**

![image-20211215204823289](./image/image-20211215204823289.png)



## 0x04设置代码块字体和行间距

在themes文件夹下，添加base.user.css文件，这里选择字体Consolas

![image-20211215212342555](./image/image-20211215212342555.png)

效果如下：![image-20211215211712283](./image/image-20211215211712283.png)



另外两种备选字体1：Comic Sans Ms

![image-20211215212038301](./image/image-20211215212038301.png)

字体2：Courier New

![image-20211215212208866](./image/image-20211215212208866.png)

## 0x05设置代码块字体和行间距

![image-20220315160717278](./image/image-20220315160717278.png)

![image-20220315160740644](./image/image-20220315160740644.png)

![image-20220315160803579](./image/image-20220315160803579.png)

![image-20220315160642591](./image/image-20220315160642591.png)

末尾添加

```css
p .md-image:only-child{
    width: auto;
    text-align: left;
}
```

