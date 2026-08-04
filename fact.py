#9.To write a Python program to calculate the factorial of a number using a loop.
num = int(input("Enter a number:"))
i=1
fact=1

for i in range(i,num+1):
  fact *= i
print("Factorial: ",fact)