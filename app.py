# # a=int(input("Enter A: "))
# # b=int(input("Enter B:"))
# # while b!=0:
# #     a,b=b,a%b                      #Euclid's Algorithm
# # print("GCD is ",a)

# n=float(input("Enter A Number:"))
# sqrt=n**0.5
# print(sqrt)

# def gcd(a,b):
#     s=min(a,b)
#     while s>0:
#         if a%s==0 and b%s==0:
#             return s
#         s-=1
# a=float(input("Enter A:"))
# b=float(input("Enter B:"))
# print(gcd(a,b)) 
n=int(input("Enter N:"))
i=2
print("Prime Factors are:")
while n>1:
    while n%i==0:
        print(i)
        n//=i
    i+=1
    