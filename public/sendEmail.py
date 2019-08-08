import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os,time
from base.read_config import get_config
from email.mime.application import MIMEApplication
def send_email(reporthtml,resultxlsx):
    #创建一个邮件
    msg=MIMEMultipart()
    #邮件标题
    msg['Subject'] = Header('接口自动化测试报告', 'utf-8')
    msg['from']=get_config('EMAIL', 'sender')  # 发送邮件的人
    msg['to']=get_config('EMAIL', 'receiver')
    #邮件正文内容
    content=MIMEText(open(reporthtml,'rb').read(),'html','utf-8')
    #将邮件内容添加到邮件
    msg.attach(content)
    #添加xlsx附件
    attacxlsx = MIMEApplication(open(resultxlsx,'rb').read())
    attacxlsx.add_header('Content-Disposition', 'attachment', filename=resultxlsx)
    msg.attach(attacxlsx)
    #添加html附件
    attachhtml=MIMEApplication(open(reporthtml,'rb').read())
    attachhtml.add_header('Content-Disposition', 'attachment', filename=reporthtml)
    msg.attach(attachhtml)
    '''
    attachhtml = MIMEText(open(reporthtml,'rb').read(), 'base64', 'utf-8')
    attachhtml['Content-Type'] = 'application/octet-stream'
    attachhtml["Content-Disposition"] = 'attachment;filename="APIReport.html"'
    msg.attach(attachhtml)'''
    try:
        s = smtplib.SMTP_SSL(get_config('EMAIL', 'serverip'), get_config('EMAIL', 'serverport'))#ssl加密方式登录邮箱
        s.login(get_config('EMAIL','username'), get_config('EMAIL','password'))
        # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
        s.sendmail(msg['from'],msg['to'], msg.as_string())
        print('%s----发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(err)
#2.定义：取最新测试报告
def get_NewFile(file_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    listreport=os.listdir(file_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    listreport.sort(key=lambda fn:os.path.getmtime(file_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(file_dir,listreport[-1])
#    L=file_path.split('\\')
#    file_path='\\\\'.join(L)
    return file_path
    
