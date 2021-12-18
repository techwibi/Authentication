passwords = 'password.txt'
file = open("final_password.txt", "w")
with open(passwords) as password:
    line1 = password.readline()
    line2 = password.readline()
    while line1:
        file.write(line1.strip())
        file.write("\n")
        file.write(line2.strip())
        file.write("\n")
        file.write("peter\n")
        line1 = password.readline()
        line2 = password.readline()
file.close()
