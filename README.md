# Version 1.1.1 更新 2022年4月23日
修复
- 优化ipf命令使用
-- 默认非记事本打开.txt文件存在逻辑错误，会导致多次查询（已修复）
优化
- ipf命令重构
-- Version 1.1.0版本中IPfile.txt文件会再命令初始化中永久创建，目前已经变更为临时创建，批量查询完成后将移除IPfile.txt文件


# Version 1.1.0 更新
- 新增ipf 子命令
-- ipf IPfile，使用时会生成一个IPfile.txt文本文件用于接收IP数据，相较于IPS ip -s 命令兼容性更好，可兼容换行符，适合大批量查询IP，结果同样会输入在控制台和日志文件
- IPS ip -s 已支持多IP输入，（逗号、分号、空格） 多种分隔符匹配，示例：
-- IPS ip -s "6.119.44.11 125.60.124.102;45.15.140.104, 119.29.29.29"
![Multi IP input](https://github.com/toolsman123/IPS/blob/main/photo/Multi%20IP%20input.png)

***
注：

- 该工具查询IP接口由ip138.com 提供，使用前请仔细阅读[官方接口文档说明](https://user.ip138.com/ip/doc/)
- 工具采用python click库编写




# 使用前准备

1. 注册ip138.com 账号，获取接口token(1000次内免费使用)

2. 下载IPS 工具 ，保存至 /Windows/System32 路径下 （Linux 可保存在 /usr/bin 路径下）
·保存路径不正确会导致无法直接在命令行运行（需自行配置环境变量解决）


# 如何使用

![命令总览](https://github.com/toolsman123/IPS/blob/main/photo/version%201.1.0.png)

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

注：后续将会接入ip-api.com的接口
- mail:1724063267@qq.com
