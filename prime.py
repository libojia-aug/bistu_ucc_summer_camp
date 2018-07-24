
num = int(input("input a number : "))
 
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not prime number")
           print(i," * ",num//i," is ",num)
           break
   else:
       print(num,"is prime number")
       
else:
   print(num,"is not prime number")