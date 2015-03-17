def factorial(n):
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

def factorial2(n):
	if n == 1:
		return 1
	else:
		return n * factorial2(n - 1)

def fibonacci(n):
	fiblist = []
	a = 1
	b = 1
	for i in range(n):
		fiblist.append(a)
		a, b = b, a + b
	return fiblist

def sum_of_digits(n):
	n = abs(n)
	result = 0
	while n is not 0:
		result += n % 10
		n = n // 10
	return result

def to_digits(n):
	n = abs(n)
	l = []
	while n is not 0:
		l.insert(0, n % 10)
		n = n // 10
	return l

def fact_digits(n):
	list = to_digits(n)
	result = []
	for number in list:
		result.append(factorial(number))
	return sum(result)

def reverse2(list):
	return list[::-1]

def reverse(element):
	element = str(element)
	element = element[::-1]
	return element

def palindrome(obj):
	obj = str(obj)
	if obj == reverse(obj):
		return True
	else:
		return False

def to_number(digits):
	result = 0
	for i in range(len(digits)):
		result *= 10
		result += digits[i]
	return result

def fib_number(n):
	return ("".join(map(str, fibonacci(n))))

def count_vowels(str):
	str = str.lower()
	counter = 0
	for i in range(len(str)):
		if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'y':
			counter += 1
	return counter

def count_consonants(str):
	str = str.lower()
	counter = 0
	for i in range(len(str)):
		if str[i] == 'b' or str[i] == 'c' or str[i] == 'd' or str[i] == 'f' or str[i] == 'g' or str[i] == 'h' or str[i] == 'j' \
		or str[i] == 'k' or str[i] == 'l' or str[i] == 'm' or str[i] == 'n' or str[i] == 'p' or str[i] == 'q' or str[i] == 'r' \
		or str[i] == 's' or str[i] == 't' or str[i] == 'v' or str[i] == 'w' or str[i] == 'x' or str[i] == 'z':
			counter += 1
	return counter

def char_histogram(string):
	dict = {}
	for letter in string:
		if letter in dict:
			dict[letter] += 1
		else:
			dict[letter] = 1
	return dict

def p_score(n):
	if palindrome(n):
		return 1
	else:
		return 1 + p_score(n + int(reverse(n))) 

def is_increasing(seq):
	for i in range(len(seq) - 1):
		if seq[i] >= seq[i+1]:
			return False
	return True

def is_decreasing(seq):
	for i in range(len(seq) - 1):
		if seq[i] <= seq[i+1]:
			return False
	return True

def count_the_ones(binary):
	counter = 0
	for i in range(len(binary)):
		if binary[i] == '1':
			counter += 1
	return counter

def is_hack(n):
	binary = bin(n)
	binary = binary[:0] + binary[1:]
	binary = binary.replace('b', "")
	ones = count_the_ones(binary)
	if palindrome(binary) and ones % 2 is not 0:
		return True
	else:
		return False

def next_hack(n):
	number = n + 1
	while not is_hack(number):
		number = number + 1
	return number

def next_hack2(n):
	flag = False
	number = n + 1
	while flag == False:
		if is_hack(number):
			flag = True
			return number
		else:
			number += 1