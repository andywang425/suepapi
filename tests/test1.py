from suepapi import Login
from suepapi import StudentAPI
from pyquery import PyQuery as pq

print('test1开始：获取今日课表')
# 登录
proxies = {
    'http': 'socks5://127.0.0.1:10800',
    'https': 'socks5://127.0.0.1:10800'
}
# 填写你的账号(学号)和密码
suepLogin = Login('2021xxxx', '12345', proxies=proxies)
suepLogin.start()
if (suepLogin.isLogin):
    session = suepLogin.getSession()
    print('Cookies: ', dict(session.cookies))
    # 测试：获取今日课表
    apis = StudentAPI(session, proxies)
    response = apis.todayCourse()
    print('状态码：', response.status_code)
    doc = pq(response.text)
    print(doc('table'))
