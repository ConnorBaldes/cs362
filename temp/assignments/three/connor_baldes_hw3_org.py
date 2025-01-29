def main(): 
    go_again = 1
    year = 0
    while go_again:
    
        year = input("Year: ")
        year = int(year)

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

        go_again = input("If you would like to go again enter 1 if not enter 0: ")
        go_again = int(go_again)
    return 0

main()
