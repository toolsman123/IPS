注：
<<<<<<< HEAD
- 该工具查询IP接口由ip138.com 提供，使用前请仔细阅读官方接口文档说明
- 工具采用python click库编写
=======
***该工具查询IP接口由ip138.com 提供，使用前请仔细阅读官方接口文档说明
***工具采用python click库编写
>>>>>>> main

# 使用前准备

1. 注册ip138.com 账号，获取接口token

2. 下载IPS 工具 ，保存至 /Windows/System32 路径下 （Linux 可保存在 /usr/bin 路径下）
·保存路径不正确会导致无法直接在命令行运行（需自行配置环境变量解决）


# 如何使用

![命令总览](https://github.com/toolsman123/IPS/blob/cf1cfab9f445b20ce8a08e2d8547c7c445011bf9/photo/1.png)

## 首次使用

**运行 IPS tk -c 【token】，完成token配置**
**serchLog和token文件将生成在根目录下**

​

![](https://github.com/toolsman123/IPS/blob/main/photo/token.png)

--help，展示该工具命令说明，任何命令下都有效

​

![](https://github.com/toolsman123/IPS/blob/main/photo/help.png)

查询IP（不指定IP表示本地公网IP信息）

IPS ip 119.29.29.29 | IPS ip -s 119.29.29

​

![](https://github.com/toolsman123/IPS/blob/main/photo/IPS%20ip.png)

查看token 信息

IPS tk | IPS tk -c 【token】

​

![](https://github.com/toolsman123/IPS/blob/main/photo/IPS%20tk.png)

查看搜索日志

IPS log 

![](https://github.com/toolsman123/IPS/blob/main/photo/IPS%20log.png)

​

注：目前可以满足简单的查询需求，后续计划实现批量查询模式，欢迎交流讨论
- mail:1724063267@qq.com
