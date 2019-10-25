def fib2(n,arr):
	if n==0 or n==1:
		return arr[n]
	if n in arr.keys():
		return arr[n]
	else :
		arr[n]=fib2(n-1,arr)+fib2(n-2,arr)
		return fib2(n-1,arr)+fib2(n-2,arr)
arr={0:0,1:1}
print(fib2(99,arr))