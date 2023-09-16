Java代码审计Fortify扫描工具

https://www.bilibili.com/video/BV1Kx41197AQ?p=2&spm_id_from=pageDriver



未对输入数据做过滤，存在sql注入

![image-20220413230233419](./image/image-20220413230233419.png)

针对sql注入，一般是用一个？作为一个占位符，然后对？做各种限定，而不是直接把用户输入内容直接拼接到sql语句中
称为==预处理== 

![image-20220413225844486](./image/image-20220413225844486.png)



![image-20220413235153869](./image/image-20220413235153869.png)