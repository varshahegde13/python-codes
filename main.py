# # # factorial of a number
# # # fact = 1
# # # num = 10
# # # if num<0:
# # #   print("negeative nos are not allowed")
# # # elif num ==1 or num ==0:
# # #   print("the fact is 1 or 0")
# # # else:
# # #   for i in range(1,num+1):
# # #     fact = fact*i
# # #   print(fact)
# #
# # # def factorial(num):
# # #   fact =1
# # #   if num<0:
# # #     return "the number should be +ve"
# # #   elif num ==1 or num==0:
# # #     return "the fact is 1 "
# # #   else:
# # #     for i in range(1,num+1):
# # #       fact = fact*i
# # #   return fact
# # # num =4
# # # print(factorial(num))
# #
# #
# #
# # # fibponacci series
# # # n1 = 0
# # # num = 7
# # # n2 = 1
# # # for i in range(0,num+1):
# # #   n3  =n1+n2
# # #
# # #   n1 = n2
# # #   n2 = n3
# # # print(n3)
# #
# # # def fibonacci(num):
# # #   n1 = 0
# # #   n2 = 1
# # #   for i in range(0,num+1):
# # #     n3 = n1+n2
# # #     n1 = n2
# # #     n2 = n3
# # #   return n3
# # # num = 7
# # # print(fibonacci(num))
# #
# # # #palindrome of a number
# # # num = 121
# # # rev = 0
# # # while num>0:
# # #   rem = num%10
# # #   rev = (rev*10)+rem
# # #   num = num//10
# # # if sum ==num:
# # #   print("palindrome of a number")
# # # else:
# # #   print("not palindrome of a number")
# #
# # #palindrome of a string
# # # str = "amma"
# # # s= str[::-1]
# # # if str == s:
# # #   print("palindrome")
# # # else:
# # #   print("not palindrome")
# #
# # # power of a number
# # # digit = 2
# # # num = 7
# # # b = pow(digit,num)
# # # print(b)
# #
# # #prime number
# # # n = 6
# # # for i in range(2,n):
# # #   if n%i ==0:
# # #     print(i,"prime numebr")
# # #   else:
# # #     print(i,"not prime number")
# #
# # #reverse a number
# # # num = 1234
# # # rev = 0
# # # while num>0:
# # #   rem = num%10
# # #   rev = (rev*10)+rem
# # #   num = num//10
# # # print(rev)
# #
# # # reversing a list
# # # list = [1,2,3,4,5,6]
# # # s = list[::-1]
# # # print(s)
# #
# # #  elements exist in a list or not
# # # s = [1,2,3,4,5,6]
# # # num = 8
# # # if num in s:
# # #   print("element exist")
# # # else:
# # #   print("element not exist")
# #
# # #  sum of number in a list
# # list = [1,2,3,5]
# # sum = 0
# # for i in list:
# #   sum = sum+i
# # print(sum)
#
# #check whether the string palindrome or not
# #count +ve and -ve elements in a list
# list = [11,2,-4,-5,6,-8]
# pos,neg = 0,0
# for i in list :
#   if i >0:
#     pos+=1
#   else:
#     neg+=1
# print(pos)
# print(neg)

# remove all empty tuples in a list
# list = [1,2,3,4,(),(),7,()]
# for i in list :
#   i.remove()
#   # if i ==():
#   #   i.remove()
#     print(list)


# remove the duplicate element ffrom the list
# list = [1,22,3,4,1,1,5,4,9]
# dup = []
# n = len(list)
# for i in range(n):1       ``````````` 
#   i.append(dup)
#   if i in dup:
#     i.remove(dup)
# print(dup)

#  remove duplicate elements from a list