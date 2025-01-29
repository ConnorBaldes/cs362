def fizz_buzz():
    numbers = ""
    for i in range(100):
        if ((i+1) % 3) != 0 and ((i+1) % 5) != 0:
            numbers += str(i+1)
        elif ((i+1) % 3) == 0 and ((i+1) % 5) == 0:
            numbers += "FizzBuzz"
        elif ((i+1) % 5) == 0:
                numbers += "Buzz"
        else:
            numbers += "Fizz"
        if i != 99:
            numbers +=" "
    return numbers