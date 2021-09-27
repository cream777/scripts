while True:
    while True:
        try:
            prime = int(input("Please enter a prime number: "))
        except ValueError:
            print("Please enter a valid integer\n")
            pass
        else:
            break
    print("Prime roots for {}:\n".format(prime))
    for i in range(1, prime):
        list =[]
        for n in range(1, prime):
            list.append((i ** n % prime))
        if len(set(list)) == len(list):
            print(i)
    another = input("\nAnother? ")
    if another == "y" or another == "yes":
        pass
    else:
        break
