
#given a list find the gretest commmon factor,( the largest number that is divisible by all 
# items in the list

def cdf(arr):
	max_num = max(arr)
	for i in range(max_num +1,1,-1):
		if all(j%i == 0 for j in arr):
			return i

print(cdf([9,3,15]))
print(cdf([2,3,4]))
print(cdf([1000,100,10]))
