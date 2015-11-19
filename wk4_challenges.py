def isVowel (letter):
	if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
		return True; 
	else:
		return False;

def sumDivBy3or5 (num):
	mysum = 0

	for x in range(1, num-1):
	    if x % 3 == 0:
	    	mysum += x
	    elif x % 5 == 0:
	    	mysum +=x
	return mysum

def sumDivBy3and5 (num):
	mysum = 0

	for x in range(1, num-1):
	    if x % 3 == 0 and x % 5 == 0:
	    	mysum +=x
	return mysum

# for words only
def is_palindrome(word):
	charList = list(word)
	reverseList = charList.copy()
	reverseList.reverse()

	for x in charList:
		ch1 = charList.pop()
		ch2 = reverseList.pop()
		if (ch1 != ch2):
			return False;
	return True;




if isVowel("a"):
	print("True a");

if isVowel("x"):
	print("True x");

print("Sum of nums divisible by 3 or 5 less than 15: %i" % sumDivBy3or5(15))
print("Sum of nums divisible by 3 or 5 less than 10000: %i" % sumDivBy3or5(10000))

print("Sum of nums divisible by 3 and 5 less than 50: %i" % sumDivBy3and5(50))
print("Sum of nums divisible by 3 and 5 less than 10000: %i" % sumDivBy3and5(10000))

if is_palindrome('racecar'):
	print("'Racecar' is a palindrome")

if is_palindrome('cow'):
	print("'cow' is a palindrome")