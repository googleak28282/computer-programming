# def fib2(n,arr):
# 	if n==0 or n==1:
# 		return arr[n]
# 	if n in arr.keys():
# 		return arr[n]
# 	else :
# 		arr[n]=fib2(n-1,arr)+fib2(n-2,arr)
# 		return fib2(n-1,arr)+fib2(n-2,arr)
def fib3(n):
	global k
	k += 1
	if n==0:return 0
	elif n==1:return 1
	return fib3(n-1)+fib3(n-2)
# arr={0:0,1:1}
# print(fib2(99,arr))
k=0
fib3(5)
print(k)
