#coding=utf-8
try:
	from webdriver2 import WebDriver
except ImportError:
	from .webdriver2 import WebDriver
from sleep import time

class LoginPage(WebDriver):
	"""登录首页"""
	# 登录输入框
	def user_input(self，user):
		self.type("#user", user)

	# 密码输入框
	def password_input(self, password):
		self.type("#psw", password)

	# 登录按钮
	def login_button(self):
		self.click(".submit")




