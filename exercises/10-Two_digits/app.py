#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  return (int(digit)//10, int(digit)%10)
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
