f = open("file1.txt")

content1 = f.read()

content = content1.split('\n')
dict = {}

for i in content:
    # data.append(i.split(' '))
    ele = i.split(' ')
    dict[ele[0]] = ele[1]
    # print(ele)

person = ""
highest = 0

for i in dict:
    if int(dict[i]) > highest:
       highest = int(dict[i])
       person = i

f = open('file2.txt', 'w')
f.write(str(str(highest) + " " + person))

print("Topper: ", person)
print("Marks: ", highest)
