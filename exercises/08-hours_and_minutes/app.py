#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  
  return (secs//int(3600),secs//int(60) )




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))