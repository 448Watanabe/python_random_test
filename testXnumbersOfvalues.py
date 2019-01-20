import os

class classA:
	def __init__(self, value1=None):
		self.value1 = value1

def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")


def func(x):

	"""
	create x numbers of values
	and give them certain instances
	"""


	# init dictianry
	my_dict = {}
	print(type(my_dict))
	pause()

	# initialize value, x
	try:
		
		for i in range(x):
			val_x = "val{}".format(i)
			my_dict[val_x] = classA(i)
	except ValueError:
		print("you got syntax error")

	
	try:
		print("\n")
		print("val_x: \n" + val_x)
		print("my_dict:"); print(my_dict)
	except:
		print("\ncannot print my_dict")

	print("\n")

	# print(help(arr))-> show all functions in arr



if __name__ == "__main__":
    func(2)

    print("print document\n")
    print(func.__doc__)