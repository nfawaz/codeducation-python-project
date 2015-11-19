

def armstrong_nums(limit):
	nums = []
	if limit < 0:
		return 0
	for x in range(0,limit):
		summed = 0
		str_x = str(x)
		for y in range (0,len(str_x)):
			summed += int(str_x[y])**3
		if summed == x:
			nums.append(x)
	return nums

def sumOfNumString (nums):
	numList = nums.split(" ");
	sum = 0
	for x in numList:
		sum += int(x)
	return sum

def getStockValue (ticker):
	url="https://www.google.com/finance?q="+ticker
	readdata = requests.get(url)
	return readdata


tri = armstrong_nums(999)
print ("Armstrong Nums 0 to 999:")
for x in tri:
	print(x)


print ("Sum of string '2 3 4 569 99': %d" % sumOfNumString("2 3 4 569 99"))

