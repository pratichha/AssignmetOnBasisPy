#Palindrome
def is_palindrome():
  str1 = input("enter a input:")
  if str1 == str1[::-1]:
   print("yes palindrome")
  else:
    print("No palindrome") 
is_palindrome() 