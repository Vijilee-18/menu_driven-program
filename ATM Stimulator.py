""" Author:Vijilee George Kurian
    Description:Simple ATM Stimulator"""

balance_amount=30000
while True:
    print("1) Check Balance amount")
    print("2) Deposit Money")
    print("3) Withdraw Money")
    print("4) Exit")
    choice=int(input("enter a number of the options:"))
    if choice==1:
        print(f'The Balance Amount is {balance_amount}')
    elif choice==2:
        Deposit_Amount=float(input("Enter the Amount you want to deposit:"))
        balance_amount=Deposit_Amount+balance_amount
        print(f'You have Deposited {Deposit_Amount} to your Bank account\nbalance amount is {balance_amount}')
    elif choice==3:
        Withdraw_Amount=float(input("enter the amount you need to withdraw:"))
        if Withdraw_Amount>balance_amount:
            print("You doesn't have enough balance to withdraw")
        else:
            balance_amount=balance_amount-Withdraw_Amount
            print(f'{Withdraw_Amount} has been credicted from your bank account\n balance amount is{balance_amount}')
    elif choice==4:
        print("Exiting...Thankyou!!")
    else:
        print("Please enter correct number")
