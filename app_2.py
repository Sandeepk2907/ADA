n=float(input("Enter a number:"))
g=n/2
for i in range(15):
    g=(g+n/g)/2
    print(g)
print("Square Root:",g)