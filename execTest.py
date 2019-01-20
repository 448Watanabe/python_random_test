for n in range(3):
    exec("name%d = %d" % (n, 100 + n))

print(name1)