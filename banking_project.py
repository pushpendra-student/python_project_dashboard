# python Banking Program

def show_balance( balance):
    print("*********************")
    print(f"your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter the amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("That's is not a valid number!")
        print("*********************")
        return 0
    else:
        return amount


def withdraw( balance):
    print("*********************")
    amount = float(input("Enter amount to be withdraw: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
    elif amount < 0:
        print("*********************")
        print("Amount must be geater than 0")
        print("*********************") 
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("  Banking program ")
        print("*********************")

        print("1.show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        print("*********************")
        choice = input("Enter your choice (1-4): ")
        print("*********************")
        if choice == '1':
            show_balance( balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw( balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not valid choice!")
            print("*********************")
    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")



if __name__ == '__main__':
    main()


