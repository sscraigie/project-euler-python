prev_num = 1
n = 1
next_num = 1
fib_even_nums = []

while n < 4000000:
	if n % 2 == 0:
		fib_even_nums.append(n)
	next_num = n + prev_num
	prev_num = n
	n = next_num
	


print(fib_even_nums)
sum_fib = sum(fib_even_nums)
print(sum_fib)
