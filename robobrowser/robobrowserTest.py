# -*- coding: utf-8 -*-
"""
以下のサイトを参照にしてrobobrowserのテスト
https://tmg0525.hatenadiary.jp/entry/2017/11/07/022837
"""


from robobrowser import RoboBrowser

class robobrowserTest:

	def __init__(self):
		pass


	def robofunc(self, site_name):
		print(site_name)

		browser = RoboBrowser(features=self.browser.parser) 
		"""
		 features=self.browser.parserを入れないと以下のようなエラーがでる

		The code that caused this warning is on line 40 of the file /Users/yoshiya/.local/share/virtualenvs/robobrowser-dBzOXSvu/lib/python3.7/site-packages/robobrowser/browser.py. To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

		  features=self.browser.parser,
		  """
		print(aaa)
		browser.open(site_name)
		form = browser.get_form()
		print(form)



if __name__ == "__main__":
	robo = robobrowserTest()
	# print(robo)
	site_name = "https://tmg0525.hatenadiary.jp/entry/2017/11/07/022837"
	print(robo.robofunc(site_name))
