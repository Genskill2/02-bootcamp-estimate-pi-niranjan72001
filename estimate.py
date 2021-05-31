
def wallis():
	n=input("enter the number of iterations to be done")
	y=1
	for i in range(1,int(n)+1):
		y=y*(4*i*i/(4*i*i-1))
	print(f"the value of pi is{2*y}")
def monte_carlo():
	import random as ra
	import math as m
	z,u=0,0
	n=input("enter the number of iterations to be done")
	for i in range(1,int(n)+1):
		x=ra.random()
		y=ra.random()
		if((x**2+y**2)**0.5)<=1.0:
			 z+=1
		else:
		 	 u+=1
	print(f"the value of pi is{4*(z/(z+u))}")
	
