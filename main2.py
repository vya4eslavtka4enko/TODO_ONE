# file = open("bear.txt",'r')
# convert_text = ''
# content = file.readline()
# content_split = content.split(' ')
# for item in content_split:
#     convert_text += " " + item.title() 


# print(convert_text)

# new_member = input("Enter the  new member ")
# file = open('member.txt','a')
# file.write('\n')
# file.write(new_member)
# file.close()

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for item in filenames:
#     file = open(item,'w')
#     file.write("Hello")
#     file.close()
# files = ["a.txt","b.txt","c.txt"]
# for file in files:
#     file = open(file,'r')
#     content = file.read()
#     print(content)
temperatures = [10, 12, 14]
 
file = open("file.txt", 'w')
 
    file.writelines(str(temperatures))