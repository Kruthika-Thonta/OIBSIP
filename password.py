import random
import string

c=string.ascii_letters

n=string.digits

s=string.punctuation

print(type(c))

length=int(input("enter the length of the password to be :"))

print("length of characters to be included within range of  0 to ",length," : ")

characters=int(input())

print("length of Numbers to be included within range of  0 to ",(length-characters)," : ")

numbers=int(input())

print("length of Symbols to be  included within range of  0 to ",(length-characters-numbers)," : ")

symbols=int(input())

password=''
password=password+''.join(random.choices(c,k=characters))
password=password+''.join(random.choices(n,k=numbers))
password=password+''.join(random.choices(s,k=symbols))

password=''.join(random.sample(password,k=len(password)))
print(password)
