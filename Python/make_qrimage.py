import qrcode
import datetime
import os, getpass

qrstr = input('请输入要转换的字符串：')
print('输入的字符串为：'+qrstr)
qrimage = qrcode.make(qrstr)

# 获取当前时间,转化成字符串
timenow = datetime.datetime.now()
timestr = timenow.strftime("%Y-%m-%d-%H-%M-%S")

# 生成带时间的二维码图片名,图片保存在桌面上
qrname = "/Users/{0}/Desktop/{1}.png".format(getpass.getuser(), timestr)

#保存二维码图片
qrimage.save(qrname)
print("生成二维码成功:", qrname)