#primefacs
import math
testnumber=600851475143


def isPrime(n):
	for i in range(3,n,2):
		if (n%i==0):
			return False
		else:
			return True


for i in range(3,int(math.sqrt(testnumber))):
	if (testnumber%i==0):
		if isPrime(i):
			print i

