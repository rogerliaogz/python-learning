"""
用户身份验证
by roger
"""
username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admim' and password == "12345":
    print("身份验证成功！")
else:
    print("身份验证失败！")

