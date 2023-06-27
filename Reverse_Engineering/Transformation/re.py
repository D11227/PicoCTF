encoded_flag = open("enc").read()

flag = ""
for i in range(len(encoded_flag)):
    flag += str(encoded_flag[i].encode('utf-16be'), 'utf-8')

print(flag)

