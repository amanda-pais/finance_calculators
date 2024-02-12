import math

'''
Start

Print an output explaining the options available for the user to choose

Input from the user the option choosen and assign it to the variable 'user_calculation'

Input and store all the information needed in their respective variables

Create an if-elif-else statement to make the calculation for each option the user may choose

Output the total for the user

End

'''

print("\ninvestment - to calculate the amount of interest you'll earn on your investment",
    "\nbond - to calculate the amount you'll have to pay on home loan\n")


user_calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Using the method .lower() when a specific input from then user is needed to make sure the program runs right if the user types with lowercase or uppercase

user_calculation = user_calculation.lower()

# When the user chooses the investment option: 

if user_calculation == "investment":

    # Casting the values to integer to use them in the equation

    money_to_deposit = int(input("\nEnter the amount of money you would like to deposit: "))

    interest_rate = int(input("\nEnter the interest rate (as a percentage): "))

    number_of_years = int(input("\nEnter the number of years you plan on investing: "))

    interest = input("\nEnter either 'simple' or 'compound' to calculate the interest: ")

    interest = interest.lower()

    # When the user enters 'simple' the equation below is running

    if interest == "simple":

        simple_total = money_to_deposit * (1 + interest_rate/100 * number_of_years)

        print(f"\nGreat! After {number_of_years} years at {interest_rate} % interest rate, you will get back: £{simple_total}")

    # When the user enters 'compound' the equation below is running

    elif interest == 'compound':

        compound_total = money_to_deposit * math.pow((1 + interest_rate/100) , number_of_years)

        print(f"\nGreat! After {number_of_years} years at {interest_rate} % interest rate, you will get back: £{compound_total}")

# When the user chooses the bond option:

elif user_calculation == "bond":

    # Casting the values to integer to use them in the equation

    house_value = int(input("\nEnter the present value of the house: "))
                      
    interest_rate_bond = int(input("\nEnter the interest rate (as percentage): "))

    interest_rate_bond = interest_rate_bond/100

    interest_rate_bond = interest_rate_bond/12

    number_of_months = int(input("\nEnter the number of months you plan to repay the bond: "))

    # Running the equation below to calculate the total bond repayment
     
    repayment = (interest_rate_bond * house_value) / (1 - (1 + interest_rate_bond)**( - number_of_months))


    print(f"\nThe total you will need to pay each month for the house loan is £{round(repayment)}")

else:

    print("\nThere has been an error in the system.")