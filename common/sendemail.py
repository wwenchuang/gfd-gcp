"""
 -*- coding: utf-8 -*-
 @Time    : 2022/9/20 16:34
 @Author  : 文闯
 @File    : sendemail.py
 @Software: PyCharm
 @company : 功夫豆信息科技
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication
#from AutoMation.PLUIAuto_Test_001.config.config import FSYJ_ZH,FSYJ_SQM,JSYJ_ZH,CSYJ_ZH,SMTP,SMTP_Port
from common.conf import MyConf
from common.path import conf_dir
import ssl

# 实例化配置类对象
conf = MyConf(os.path.join(conf_dir, "automation.ini"))
FSYJ_ZH = conf.get("FSYJ_ZH", "FSYJ_ZH")
print("发送邮箱是：",FSYJ_ZH)
JSYJ_ZH = conf.get("JSYJ_ZH", "JSYJ_ZH")
CSYJ_ZH = conf.get("JSYJ_ZH", "JSYJ_ZH")
SMTP = conf.get("SMTP", "SMTP")
SMTP_Port = conf.get("SMTP_Port", "SMTP_Port")
FSYJ_SQM = conf.get("FSYJ_SQM", "FSYJ_SQM")

def mail(filename, title = None, description = None):
    """
    通过邮件，将生成的文件，作为附件，发送给对应人员
    :param filename：测试报告所在路径：相对或绝对路径都可以，不过一定要能够找到数据
    :param title: 邮件名称，可以不加，有默认值
    :param description: 邮件描述，可以不加，有默认值
    """
    # with open(r"..\report\2022-06-02-15_21_54_result.html","rb") as f:
    #     print(f.read())
    #     html_nr = f.read()

    # file = urlopen(r"..\report\2022-06-02-15_21_54_result.html").read()
    # print(file)


    msg = MIMEMultipart() # 生成一个带附件的邮件
    msg['From'] = formataddr(["功夫豆GCP自动化测试报告", FSYJ_ZH])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["接收测试报告账号",','.join(JSYJ_ZH.split(','))])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Cc'] = formataddr(["抄送账号", CSYJ_ZH])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    if title == None:
        msg['Subject'] = "功夫豆GCP自动化测试脚本运行结果"  # 邮件的主题，也可以说是标题
    else:
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

    # # 添加附件（pdf文档）
    # pdfFile = "report\\2022-06-02-15_21_54_result.html"  # 需发文件路径
    # pdf = MIMEApplication(open(pdfFile, 'rb').read())
    # pdf.add_header('Content-Disposition', 'attachment', filename='pdf')
    # 文字部分
    if description == None:
        part = MIMEText("GCP测试报告，请查收！")
    else:
        part = MIMEText(description)
    msg.attach(part)

    # msg.attach(pdf)
    # filepath = "..\\" + filename
    # file_msg = MIMEApplication(open(r"..\report\2022-06-02-15_21_54_result.html", "rb").read())
    # 将测试报告作为附件，增加到邮件中
    file_msg = MIMEApplication(open(filename, "rb").read())
    file_msg.add_header("content-disposition", "attachment", filename = "GCP测试报告.html")
    msg.attach(file_msg)

    # # 读文件
    # f = open(filename,'rb')
    # mail_body = f.read()
    # f.close()
    # # 邮件正文是MIMEText
    # body = MIMEText(mail_body,'html', 'utf-8')
    # # 邮件对象
    # msg = MIMEMultipart()
    # msg.attach(body)
    # # 附件
    # att = MIMEText(mail_body, "base64", "utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment'
    # msg.attach(att)


    # server.quit()  # 关闭连接
    try:
        server = smtplib.SMTP_SSL(SMTP, SMTP_Port)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(FSYJ_ZH, FSYJ_SQM)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(FSYJ_ZH, JSYJ_ZH.split(','), msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        print("接收邮箱账号是：",msg['To'])
    except Exception as e:
        print('邮件发送失败，原因：{}'.format(e))
    else:
        print('邮件发送至{}成功！'.format(msg['To']))
    finally:
        server.quit()


# ======================查找最新的测试报告==========================

def new_report(testreport):
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-2]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new


if __name__ == '__main__':
    test_report = "/Users/gfd/Desktop/gfd/reports"
    report = new_report(test_report)
    mail(report)