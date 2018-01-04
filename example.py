import getpass
import dutsso

print('\n********** 欢迎使用大连理工大学校园门户信息查询系统 **********')
print('******************** Powered by Zijin ********************')
user = dutsso.User()

username = input('\n请输入学号：')
password = getpass.getpass('请输入密码：')

# SSO登录
login = user.login(username, password)
if not login:
    print("用户名密码错误！")
else:
    print("登录成功！")

    # 查询校园卡余额
    card = user.get_card()
    print("\n您的校园卡信息为：")
    print("余额：%s元" % card["money"])
    print("最后交易时间：%s" % card["last_time"])

    # 查询研究生成绩
    scores = user.get_score()
    print("\n您的研究生成绩信息为：")
    print('共找到%d条必修课成绩' % len(scores["bx"]))
    for i in scores["bx"].keys():
        print(i, scores["bx"][i])
    print('\n共找到%d条选修课成绩' % len(scores["xx"]))
    for i in scores["xx"].keys():
        print(i, scores["xx"][i])

    # 查询图书馆
    lib_dict = user.get_library()
    print("\n您的图书馆信息为：")
    print("总借书次数：%s" % lib_dict['times'])
    print("欠费金额：%s" % lib_dict['money'])
    print("绑定邮箱：%s" % lib_dict['email'])
    print("绑定手机：%s" % lib_dict['phone'])
    
input('\n按Enter键退出...')