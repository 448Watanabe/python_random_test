import urllib.request
from bs4 import BeautifulSoup
# https://www.pointmp4.com/en
# response = urllib.request.urlopen('https://accounts.google.com/ServiceLogin/signinchooser?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26hl%3Den%26app%3Ddesktop%26action_handle_signin%3Dtrue&hl=en&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
open_url = "https://item.fril.jp/b877d26b1b96142fdeb54d35e6fbadef"

response = urllib.request.urlopen(open_url)
html = response.read()

# print(html)

soup = BeautifulSoup(html, "html.parser")

item_names =  soup.find_all("h1")

count = 1
for item_name in item_names:
	print(count)
	print()
	print(item_name)
	print("\n")
	count += 1

# button = soup.button
# print(item_name)
