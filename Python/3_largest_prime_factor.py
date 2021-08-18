import math

num = 600851475143
number_to_check = int(math.sqrt(num))

#---------------------------------#

def check_factors(input):
	factors = []
	for n in range(1,int(math.sqrt(num))+1):
		if input % n == 0:
			factors.append(n)
	return factors



fact_to_check = check_factors(num)



def check_prime(n):
	return len(check_factors(n)) == 2



prime_factors = []
for i in fact_to_check:
	if check_prime(i) == True:
		prime_factors.append(i)


#-----------------------#

print("High Prime Factor:")
print(prime_factors[-1])



print(" ")
print(fact_to_check)

