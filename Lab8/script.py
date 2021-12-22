file = open("token.txt", "w")
for i in range(10000):
    file.write('{0:04}'.format(i))
    file.write('\n')
file.close()
