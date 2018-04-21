########################################################################################
################################  Problem Statement​ ​1: ###############################
########################################################################################

##Write a Python Program to implement your own myreduce() function which works exactly
##like Python's built-in function reduce()

def myreduce(f,lst):
	
	result=0
	if len(lst) > 1:
		for i in range(len(lst)):
			if i == 0:
				a=lst[i]
				b=lst[i+1]
			
				result = f(a,b)
			elif i+1 < len(lst):
				b=lst[i+1]
				result=f(result,b)
			else:
				print ('Result of Reduce function: ',str(result))
				
	else:
		print ("Sequence should be passed with 2 elements atleast")
	
	
lst=[2,3,5,8]
f=lambda a,b:a+b

myreduce(f,lst)

########################################################################################
################################  Problem Statement​ ​2: ###############################
########################################################################################

##Write a Python program to implement your own myfilter() function which works exactly
##like Python's built-in function filter()

def myfilter(f,lst):
	
	output=[]
	if len(lst) > 0:
		for i in range(len(lst)):
			a=lst[i]
			result = f(a)
			if result:
				output.append(a)
			
		print ('Result of Filter function: ',output)
				
	else:
		print ("Sequence can't be null. Atleast one element needed")
		

fib = [0,1,1,2,3,5,8,13,21,34,55]
f=lambda x: x % 2
f1=lambda x: x % 2 == 0

#myfilter(f,fib)
myfilter(f1,fib)