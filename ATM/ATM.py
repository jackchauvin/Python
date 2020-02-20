#-------------------------------------------------------------------------
#     Change Calculator (May 2018)  
#     
#     Jack Chauvin                                                           
#    
#     User input, logical statements, loops                                                                        
#-------------------------------------------------------------------------

# initial change amount
quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("Welcome to change-making program.\n")
print("Stock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

# while loop stops if 'q'
while in_str != 'q':
    # amount of change given to customer
    quarters_customer = 0
    dimes_customer = 0
    nickels_customer = 0
    pennies_customer = 0
    
    # runs if purchse price input is negative
    if float(in_str) < 0:
        print("Error: purchase price must be non-negative.")
        print()
        print("Stock: {} quarters, {} dimes, {} ni"
        "ckels, and {} pennies".format(quarters, dimes, nickels, pennies))
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        continue  #continue reutrns to beginning of while loop
        
    paid_int=input("Input dollars paid (int): ")    # amount paid 
    cents=round(100*(int(paid_int)-float(in_str)))  # total change required
    
    # runs if change is less than zero (amount paid is less than purchse price)
    if cents < 0:
        print("Error: insufficient payment.") 
        continue
    # runs if change is more than total amount of change left
    elif cents > (25*quarters+10*dimes+5*nickels+pennies):
        print("Error: ran out of coins.")
        in_str="q"
        continue
    # runs if no change (purchase price equals paid amount)
    elif cents == 0:
        print("No change.")
        print()
        print("Stock: {} quarters, {} dimes, {} ni"
        "ckels, and {} pennies".format(quarters, dimes, nickels, pennies))
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        continue
    else:
        # runs through coins from largest to smallest to calculate change
        # smallest amount required 
        while cents >=25 and quarters > 0:
            cents-=25
            quarters-=1
            quarters_customer+=1
        while cents >=10 and dimes > 0:
            cents-=10
            dimes-=1
            dimes_customer+=1
        while cents >=5 and nickels > 0:
            cents-=5
            nickels-=1
            nickels_customer+=1
        while cents >=1 and pennies > 0:
            cents-=1
            pennies-=1
            pennies_customer+=1
            
        print()
        print("Collect change below: ")
        
        # if no change given to the customer, the amount will not be printed
        if quarters_customer > 0:
            print("Quarters:", quarters_customer)
        if dimes_customer > 0:
            print("Dimes:", dimes_customer)
        if nickels_customer > 0:
            print("Nickels:", nickels_customer)
        if pennies_customer > 0:
            print("Pennies:", pennies_customer)
    
    print()
    print("Stock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")