#tuple with your first name, last name, and age and sort it with addition of other value
my_info = ('pratichha', 'kunwar', 25)
list1 = [('sita', 'Thapa',20), ('rita', 'cheetri', 34),('pari','pari','25')]
list1.extend({my_info})
print(list1)
friend_info = ('anu','poudel',23),('poonam','kafle',24)
list1.extend(friend_info)
print(list1)
sorted_list=sorted(list1, key=lambda x: str(x[2]))
print(sorted_list)
