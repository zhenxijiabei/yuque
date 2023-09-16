centos开启weblogic服务

```bash
docker-compose up -d
```

![image-20211230152037583](./image/image-20211230152037583.png)
![image-20211230152055532](./image/image-20211230152055532.png)

![image-20211230152923464](./image/image-20211230152923464.png)



利用Java反序列化漏洞，上传木马，路径如下

/root/Oracle/Middleware/wlserver_10.3/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/cmd.jsp

![image-20211230151039001](./image/image-20211230151039001.png)

冰蝎连接木马

http://192.168.32.130:7001/console/framework/skins/wlsconsole/images/cmd.jsp

![image-20211230151227606](./image/image-20211230151227606.png)



