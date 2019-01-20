# -*- coding: utf-8 -*-

class kwargTest:
	def __init__(self):
		self.a = "value"

	def print_keyword_args(self):
		print "a"
	"""
	or
	@staticmethod
	def print_keyword_args(self):
		print "a"
    """ 
testInstance = kwargTest()
#kwargTest().print_keyword_args()

testInstance.print_keyword_args()
