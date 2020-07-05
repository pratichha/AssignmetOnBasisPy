#Search in list with for loop
friend = ["Ram","Laxmun","Sita","Binita",'Elon' ]
Colleagues =["Hari","Rita","sita"]
list1 = []
list1 = friend + Colleagues
print(list1)  
x = str(input("enter a input:"))
for i in list1:
    if i==x:
       print("Found")
    else:
        print("Not Found")  
   