#1
def sum_to(num):
  sum = 0
  for i in range(num + 1):
    sum += i
  return sum

 #2
 def largest(ls):
  largest = 0
  for num in ls:
    if num > largest:
      largest = num
  return largest

 #3

 def stuff(myString, s):
	if len(myString) == 0: 
		return 0

	if s in myString: 
		return 1 + stuff(myString[myString.index(s) + len(s):], s)
	else: 
return 0

#4
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product