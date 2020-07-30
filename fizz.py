for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    elif fizzbuzz % 7 == 0:
        print("Fizzbang")
        continue
    print(fizzbuzz)

	