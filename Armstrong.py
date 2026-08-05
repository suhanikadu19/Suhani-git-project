#20.To write a Python program to check whether a given number is an Armstrong
#number.
n = int(input("Enter a number: "))
temp = n
sum = 0
digit = len(str(n))
while temp >0:
  digits = temp % 10
  sum += digit ** digit
  temp //= 10
  if sum == n:
    print(n,"is an armstrong number")
else:
      print(n, "is not strong armstrong")