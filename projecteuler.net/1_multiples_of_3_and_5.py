mult = []


for i in range(1000):
	if i % 3 == 0:
		mult.append(i)

	elif i % 5 == 0:
		mult.append(i)


#print(mult)
sum_mult = sum(mult)
print(sum_mult)
