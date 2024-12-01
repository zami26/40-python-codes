# 1.write a program to print hello world.
print("Hello World")


# 2.Write a program to sum of two number. 
firstnum = int(input("enter a number :"))
secnum = int(input("enter a number :"))
add = firstnum + secnum
#print(add)
print(f"sum is = {add}")


# 3.Write a program to calculate the sqrt of number. 
def sqr_root(n):
    if n<0:
        print("This number's root is not real")
    else:
        return n**0.5
 
 
mynum = int(input("Enter a number = "))
root_num = sqr_root(mynum)
print(f"The root of{mynum} is = {root_num}") 
 
 
# 4.Write a program to calculate area of triangular. 
def triangle_d(a,b,c):
    s = (a+b+c)/2
    if a**2 == b**2 + c**2:
        return 0.5*b*c
    else:
        return s*(s-a)*(s-b)*(s-c)
 
 
a = int(input("enter larger side of T."))
b = int(input("enter secound side of T."))
c = int(input("enter 3rd side fof T."))
sum = triangle_d(a,b,c)
print(sum) 
 
 
# 5.Write a program to cheque Odd number & Even number. 
def check_odd_even(n):
    if n%2==0:
        return "is an even number "
    else :
        return "is an odd number"
mynum = int(input("enter a num : "))
check = check_odd_even(mynum)
print(f"answare : {check}")
 