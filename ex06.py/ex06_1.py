# iteration
def fib1(n):
	fib=[]
	for i in range(n+1):
		if i==0: fib.append(0)
		elif i==1: fib.append(1)
		else: fib.append(fib[-1]+fib[-2])
	return fib[n]

def fib2(n):
	if n==0:return 0
	elif n==1:return 1
	return fib2(n-1)+fib2(n-2)

n=int(input())
print(fib1(n)," ",fib2(n))