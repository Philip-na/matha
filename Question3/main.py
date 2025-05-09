def main():
    while True:
        try:
            user_input = input("Enter an integer between 1 to 10: ")
            
            try:
                number = int(user_input) #raise error if not interger
                
                # Validate range using exception handling
                try:
                    _ = 1/(number != 0)  #raise error if number is 0
                    _ = 1/(1 <= number <= 10)  #raise error if out of range
                    reciprocal = 1 / number
                    
                    print(f"The reciprocal of your number is: {reciprocal}")
                    break
                    
                except ZeroDivisionError as zde:
                    try:
                        _ = 1/(number != 0)  # This will succeed if number is non-zero
                        print("You did not enetr a number between 1 and 10!!!")
                        print("Please try again.")
                    except ZeroDivisionError:
                        print("Oops, you entered zero.")
                        print("Please try again")
                        
            except ValueError as ve:
                print("You did not enter an integer!!!")
                print("Please try again")
                
        except Exception as e:
            print("An unexpected error occurred.")
            print("Please, try again.")

main()