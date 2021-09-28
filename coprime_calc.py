while True:
	while True:
		try:
			num = int(input("\nEnter an integer: "))
		except ValueError:
			print("Please enter a valid integer\n")
			pass
		else:
			break
	print("Coprimes of {}:\n".format(num))
	coprimes = []
	numfactors = []
	numdivs = []

	for i in range(2, num):
			if ( num / i ) - (int( num / i )) == 0:
				numdivs.append(i)


	for i in range(1, num):
		idivs = []
		for j in range(1, num):
			if (i / j) - int(i / j) == 0:
				idivs.append(j)

		if not (set(idivs) & set(numdivs)):
			coprimes.append(i)
			
	print(coprimes)
	another = input("\nAnother? ")
	if another == "y" or another == "yes":
		pass
	else:
		break


				