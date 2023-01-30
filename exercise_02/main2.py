import random
import time
start=time.time()       #https://www.programiz.com/python-programming/examples/elapsed-time#:~:text=Example%201%3A%20Using%20time%20module&text=In%20order%20to%20calculate%20the,which%20gives%20the%20execution%20time.
num1=0                  #uses two time stamps and then subtracts the difference to get the total time that it runs
num2=1
num3=0
rand=(int)((random.random()*21)+15)

for i in range(rand):
    num3=num1
    num1=num1+num2
    num2=num3

print(f'fib({rand})={num1}')
end=time.time()
print(f'fib({rand}) took {end-start} seconds.')
