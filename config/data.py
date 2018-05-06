import os
if os.environ['SETESTENV']:
    ENV = os.environ['SETESTENV']
else:
    ENV = 'test'

CONFIG = {
    'domain': 'http://localhost/wordpress/',
    'test': {
        'domain': 'http://localhost/wordpress/',
    },
    'production': {
        'domain': 'http://139.199.192.100:8000/'
    }
}

TEST_DATA = {
    'username': 'admin',
    'password': 'admin'
}

"""
使用demo：
from config.data import CONFIG

def test_login_success(self):
    username = TEST_DATA['username']
    password = TEST_DATA['password']

    login_page = LoginPage(self.dr, 'wp-login.php')
    dashboard_page = login_page.login(username, password)
    ......
    ......
    ......
"""
