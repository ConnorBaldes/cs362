def check_input_int(message, lower, upper, error_msg, size):
    
    bad_input = 1

    while bad_input:

        bad_input = 0

        num = input(str(message))
        if int(size) != 0 and int(size) != len(num):
            print("Must input integer of correct size.")
            bad_input = 1
            continue

        for c in range(len(num)):

            if ord(num[c]) not in range(int(lower),int(upper)+1):

                print(str(error_msg))

                bad_input = 1

                break

    return int(num)

        



def main(): 
    go_again = 1
    year = 0
    while go_again:
    
        year = check_input_int("Year: ",48,57,"You must input a positive integer ",0)

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print( str(year) + " is a leap year. ")
                else:
                    print( str(year) + " is not a leap year. ")
            else:
                print( str(year) + " is a leap year. ")
        else:
            print( str(year) + " is not a leap year. ")

        go_again = check_input_int("If you would like to go again enter 1 if not enter 0: ", 48, 49, "Enter either 1 or 0. ",1)

main()