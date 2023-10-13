关于csdn通过markdown使用链接转存图片后没有水印的问题，这里可以通过修改markdown里的代码为每个图片添加上水印



链接图片之后，最后一步，需要重新做下水印，

可以在sublime里（ 不要在正则模式）   		

将  `.png)` 替换为

```html
.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA572R57uc5a6J5YWo5bCP55m9Nw==,size_20,color_FFFFFF,t_70,g_se,x_16)
```



这样即可实现为每个上传的图片添加上水印

