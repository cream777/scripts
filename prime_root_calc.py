while True:
    while True:
        try:
            prime = int(input("\nPlease enter a prime number: "))
        except ValueError:
            print("Please enter a valid integer\n")
            continue        
        divs = 0
        for i in range(1, prime):
            if (prime / i) - (int(prime / i)) == 0:
        
                divs += 1
        print(divs)
        if divs > 1:
            continue         
        else:
            break
    print("Prime roots for {}:\n".format(prime))
    proots = []
    for i in range(1, prime):
        list =[]
        for n in range(1, prime):
            list.append((i ** n % prime))
        if len(set(list)) == len(list):
            proots.append(i)
    print(proots)
    another = input("\nAnother? ")
    if another == "y" or another == "yes":
        pass
    else:
        break
