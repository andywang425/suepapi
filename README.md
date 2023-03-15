# suepapi

上海电力大学网站 API，包括本科生教学管理系统，能源管理平台。

## Install

```
$ pip install suepapi
```

## Proxies

在非校园网环境下使用 suepapi 时需要配置代理，建议配合[docker-easyconnect](https://github.com/Hagb/docker-easyconnect)使用。

如果要使用 socks 代理，需要额外安装 PySocks 模块：

```
$ pip install pysocks
```

## Usage

1. 获取今日课表

```python
from suepapi import Login
from suepapi import StudentAPI
from pyquery import PyQuery as pq

proxies = {
    'http': 'socks5://127.0.0.1:10800',
    'https': 'socks5://127.0.0.1:10800'
}
suepLogin = Login('2021xxxx', '12345', proxies=proxies)
suepLogin.start()
if (suepLogin.isLogin):
    session = suepLogin.getSession()
    print('Cookies: ', dict(session.cookies))
    apis = StudentAPI(session, proxies)
    response = apis.todayCourse()
    print('状态码：', response.status_code)
    doc = pq(response.text)
    print(doc('table'))
```

2. 获取寝室电表信息

```python
import suepapi

proxies = {
    'http': 'socks5://127.0.0.1:10800',
    'https': 'socks5://127.0.0.1:10800'
}
suepLogin = suepapi.Login('2021xxxx', '12345', service='energy', proxies=proxies)
suepLogin.start()
if (suepLogin.isLogin):
    session = suepLogin.getSession()
    print('Cookies: ', dict(session.cookies))
    apis = suepapi.ElectricAPI(session)
    apis.proxies = proxies
    response = apis.getMeter()
    print('状态码：', response.status_code)
    print(response.text)

```

## TODO

- 增加数据处理功能
