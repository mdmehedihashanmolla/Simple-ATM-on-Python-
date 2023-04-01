usernames = ['Mehedi', 'Arnab', 'Torsha']
pins = [1111, 2222, 3333]
balances = [5000, 10000, 15000]

class Deposit:
    def __init__(self):
        pass

    def balance_deposit(self, i):
        bal = balances[i]
        amount = int(input("Enter the deposit amount : "))

        bal = bal + amount
        print("Your current balance is : ", bal)
        balances[i] = bal

class withdraw:
    def __init__(self):
        pass

    def balance_withdraw(self, i):
        bal = balances[i]
        amount = int(input("Enter the withdraw amount : "))

        if amount<bal:
            bal = bal - amount
            print("Your current balance is : ", bal)
            balances[i] = bal
        else:
            print("Insufficient Balance")

class Statement:
    def __init__(self):
        pass

    def balance_check(self, i):
        bal = balances[i]
        print("You current balance is : ", bal)


class Main_Menu(Statement, withdraw, Deposit):
    def __init__(self):
        Statement.__init__(self)
        withdraw.__init__(self)
        Deposit.__init__(self)

    def transaction(self, i):
        s = input("Do you want to continue the transaction? \"Y/N\" : ")
        if s == "y":
            self.show_menu(i)
        elif s == "n":
            exit()
        else:
            self.transaction(i)

    def show_menu(self, i):
        print("\n ----------------------------")
        print("|         Main Menu          |")
        print("| Enter 1 for Balance Check  |")
        print("| Enter 2 for Withdraw       |")
        print("| Enter 3 for Deposit        |")
        print("| Enter 4 for Exit           |")
        print(" ----------------------------\n")

        c = int(input("Enter your Choice : "))
        if c == 1:
            self.balance_check(i)
        elif c == 2:
            self.balance_withdraw(i)
        elif c == 3:
            self.balance_deposit(i)
        elif c == 4:
            exit()
        else:
            self.show_menu()

        self.transaction(i)

class Login(Main_Menu):
    def __init__(self):
        Main_Menu.__init__(self)

    def verify_username(self):
        username = input("Enter the Username : ")

        if username in usernames:
            index_no = usernames.index(username)
            self.verify_pin(index_no)
        else:
            print("Wrong Username, Try Again!!!")    

    def verify_pin(self, i):
        c = 0
        while c<3:
            pin = int(input("Enter the pin : "))
            if pin == pins[i]:
                self.show_menu(i)
                break
            else:
                print("Wrong Pin.")
            c += 1

        if c == 3:
            print("3 wrong input, Your ATM Card is blocked for 24hrs.")
            
o = Login()
o.verify_username()
