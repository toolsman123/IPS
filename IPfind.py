import click  # 导入库click
import httplib2
from urllib.parse import urlencode
import json
import IPy
import datetime
import os

text = {'ip': '', 'datatype': 'txt', 'callback': 'find'}
token = ""
headers={'token':''}


@click.command()  # 设置命令
@click.option('source','-s','-S', default="", help='input ip ,输入要查询的IP，信息')
@click.argument('ip',default="")
def IP(source,ip):
    """
    查询IP 信息 | find IP information
    """
    CheckFile()
    # click.echo(source)
    if source!='':
        try:
            IPy.IP(source)
            soipinfo(source)
        except Exception as e:
            click.echo("【非法IP】请咨询核对")
    elif ip !='':
        try:
            IPy.IP(ip)
            soipinfo(ip)
        except Exception as e:
            click.echo("【非法IP】请咨询核对")
    else:
        soipinfo(source)


@click.command()
@click.option('-change', '-c', '-C', default="", help='修改')
def tk(change):
    """
       显示token信息 | display token.txt
    """
    global token
    if change!="" and len(change)==32:
        open('token.txt', 'w').write(change)
        click.echo('【修改成功】token:'+change)
        token = change
        if token != "":
            infoToken()
    elif change=="":
        if token != "":
            infoToken()
        pass
    else:
        click.echo('【非法token】请核查是否正确')

@click.command()
def log():
    """
            打开历史查询记录 | searchlog
            'serchLog.txt' 不是内部或外部命令，也不是可运行的程序 代表没有log文件，正常查询即可
    """
    try:
        os.system("serchLog.txt")
    except Exception as e:
        click.echo('【提示】暂无搜索记录 请查询后重试 命令 command | IPS ip')

def infoToken():
    """
        显示token剩余请求数 | tonken information
    """
    count = "***token错误或失效，请更新后重试***"
    url = 'https://api.ip138.com/status/?datatype=txt&&token=' + token
    http = httplib2.Http()
    response, content = http.request(url,'GET')
    content = json.loads(content)
    try:
        for i in content['data'].values():
            count = str(i)
            # click.echo(count)

    except Exception as e:
        click.echo('token非法，请核实')
    click.echo("【该token剩余次数为】：" + count)
    showToken()

def soipinfo(source):
    now_time = datetime.datetime.now()
    text['ip'] = source
    params = urlencode(text)
    url = 'https://api.ip138.com/ip/?' + params
    http = httplib2.Http()
    response, content = http.request(url, 'GET', headers=headers)
    click.echo(content.decode("utf-8"))
    time = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
    open('serchLog.txt', 'a+').write("\n" +time+" info "+content.decode("utf-8") )

def showToken():

    click.echo("token:"+token)


def readToken():
    global token
    try:
        token_str = open('token.txt', 'r')
        str = token_str.readline()
        token = str
        headers['token'] = str
    except Exception as e:
        open('token.txt', 'w')
        click.echo("【token异常】：请修改 命令 command | IPS tk -c （token）")
        pass

def CheckFile():
    try:
        f = open('serchLog.txt','r')
        f.close()
        pass
    except Exception as e:
        click.echo("首次使用，将创建查询日志文件 PowerBy IPS (IP Search information display tool)")
        open('serchLog.txt','w').write("欢迎使用，该文本将记录历史查询记录，请勿轻易删除,海外IP部分信息为空,日志格式如下\n"+"【查询时间】【info】【IP】【地区信息】【运营商】【邮编】【区号】")

@click.group()
def cli():
    readToken()
    pass
cli.add_command(IP)
cli.add_command(tk)
cli.add_command(log)
cli()



# if __name__ == '__main__':
#     readToken()
#     cli()
#PowerBy Ni

