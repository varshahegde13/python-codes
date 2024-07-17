#sum of first N natural no.s
# N = 10
# sum =0
# for i in range(N):
#     sum+=i
# print(sum)

# first N natural no. given in a range
# n1 = 3
# n2= 8
# sum  =0
# for i in range(n1,n2+1):
#     sum+=i
# print(sum)

# prime no. using ython
# n = 109
# flag = 0
# for i in range(2,n):
#     if n%i==0:
#         flag = 1
#         break
#
# if flag ==1:
#     print("Not prime")
# else:
#     print("prime")


# sum of no. of digits in python
# num = input("enter the number:")
# sum = 0
# for i in num:
#     sum = sum +int(i)
# print(sum)

#reverse a number using python
# num  = 1039
# temp = num
# rev = 0
# while num>0:
#     rem = num%10
#     rev = (rev*10)+rem
#     num = num//10
# print(rev)

# palindrome of a number
# num = 121
# rev = 0
# temp = num
# while num>0:
#     rem = num%10
#     rev = (rev*10)+rem
#     num = num//10
# if temp == rev :
#     print("palindrome")
# else:
#     print("not palindrome")

#
# num = 1233
# s = int(str(num)[::-1])
# print(s)
# if str ==num:
#     print("palindrome")
# else:
#     print("not palindrome")
#
# num = 371
# digit ,sum =0,0
# length = len(str(num))
# for i in range(length):
#    digit = int(num%10)
#    num = num/10
#    sum+=pow(digit,length)
# if sum ==num:
#     print("armstrong of a number")
# else:
#     print("not armstrong of a number")

# factorial of a number
# num = 4
# fact = 1
# if num ==1 or num==0:
#     print("the fact is 1")
# elif num<0:
#     print("the no. should be greater than 0")
# else:
#     for i in range(1,num+1):
#         fact = fact*i
# print(fact)

# HCF of a number
# hcf = 1
# n1 = 36
# n2 = 60
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         hcf =i
# print(hcf)

# check wheather the charcter vowel or string
# str = "a"
# if str== "a" or str== "e" or str== "i" or str== "o" or str== "u" or str== "A" or str== "E" or str== "I" or str== "O"or str== "U":
#     print("its a vowel")
# else:
#     print("Not vowel")

# remove the spaces from the string
# str = "prepinsta is a good varsha"
# str = "".join(str.split())
# print(str)

# str = "varsha"
# dict = {}
# for i in str:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i] =1
# print(dict)

# string is symmetrical or not
# str = "varshhhhaa"
# s = str[::-1]
# if str ==s :
#     print("symmetrical")
# else:
#     print("not symmetrical")
#
# str = "geeks quiz is for good"
# s = str.split()[::-1]
# l = []
# for i in s:
#     l.append(i)
# print(l)
# print(s)
# str =reversed(str)
# print(str)

# str = "hello god this is from heaven"
# # s = str[::-1]
# # print(s)
# # m = str.split()[::-1]
# # print(m)
# length = len(str)
# print(length)
#
# str1 = "hello this is"
# counter = 0
# for i in str1:
#     counter+=1
# print(counter)

# input_string = "varsha"
# output_string = input_string[0].upper() + input_string[1:]
# output_string = output_string[:-1] + output_string[-1].upper()
# print("Original string:", input_string)
# print("Modified string:", output_string)
#
# str = "varsha"
# out = str[0].upper()+str[1:]
# out = out[:-1]+out[-1].upper()
# print(out)

# Python program to print even length words in a string
# str = "varsha is good girls"
# n = str.split()
# for i in n:
#     if len(i)%2==0:
#         print(i)
#

# uppercase half string
# str = "hellovarsha"
# s = len(str)//2
# res = ''
# for i in range(len(str)):
#     if i>=s:
#         res+=str[i].upper()
#     else:
#         res+=str[i]
#
# print(res)

# Python program to check if a string has at least one letter and one number
# def check(str):
#     flag_l = False
#     flag_m = False
#     for i in str:
#         if i.isalpha():
#             flag_l = True
#         if i.isdigit():
#             flag_m = True
#     return flag_l,flag_m
# str = "wwelcome342hello"
# # print(check(str))
#
# str ="helloooooo"
# s = set(str)
# print(s)

# remove duplicate element from a string
# list1 = [1,2,3,2,3,4,5,6,33,44,55]
# s = list(set(list1))
# print(s)

# list1 = [1,1,2,3,4,5,5,6,7,88]
# dup =[]
# unique = []
# for i in list1:
#     if i not in unique:
#         unique.append(i)
#     else:
#         dup.append(i)
# print(unique)
#
# using function
# def fun(list1):
#     s = list(set(list1))
#     return s
# list1 = [1,1,2,3,4,4,5,4,6,7]
# print(fun(list1))

# def fun(list1):
#     dup = []
#     unique = []
#     for i in list1:
#         if i not in unique:
#             unique.append(i)
#         else:
#             dup.append(i)
#     return unique
# list1 = [1,1,2,3,3,3,4,5,6]
# print(fun(list1))