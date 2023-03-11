import suepapi

print('test2开始：获取寝室电表信息')
# 登录
proxies = {
    'http': 'socks5://127.0.0.1:10800',
    'https': 'socks5://127.0.0.1:10800'
}
# 填写你的账号(学号)和密码
suepLogin = suepapi.Login('2021xxxx', '12345', service='energy', proxies=proxies)
suepLogin.start()
if (suepLogin.isLogin):
    session = suepLogin.getSession()
    print('Cookies: ', dict(session.cookies))
    # 测试：获取电表信息
    apis = suepapi.ElectricAPI(session)
    apis.proxies = proxies
    response = apis.getMeter()
    print('状态码：', response.status_code)
    print(response.text)
