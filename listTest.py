list = [1,2,3]

print list

print("--------1")

print len(list)

print("--------2")

print len(list)

print ("-------4")

for x in range(len(list)-1,-1, -1):
	print list[x]


list.append(4)

print("---------3")
print list
