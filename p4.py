class Bank:
    acbal=10000
    def deposit(self):
        deposit=int(input("enter deposit amount"))
        if(deposit>=100 and deposit<=50000 and deposit%100==0):
            print("accepted the deposit")
        else:
            if(deposit<100):
                print("cant deposit due to less than min deposit")
            elif(deposit>50000):
                print("cant deposit due to more than max deposit")
            elif(deposit%100!=0):
                print("cant deposit because amount is not multiples of 100")
    def withdraw(self):
        w_amount=int(input("Enter amount to withdraw"))
        no_of_transactions=int(input("Enter no of transactions"))
        if(w_amount>=100 and w_amount<=20000 and w_amount<self.acbal and w_amount%100==0 and self.acbal>=500 and no_of_transactions<=3):
            print("you can withdraw amount")
        else:
            if(w_amount<100):
                print("you cannot withdraw amount because less than min withdraw amount")
            elif(w_amount>20000):
                print("you cannot withdraw amount because greater than max withdraw amount")
            elif(w_amount>=self.acbal):
                print("you cannot withdraw amount because greater than account balance")
            elif(w_amount%100!=0):
                print("cant withdraw amount because amount is not multiples of 100")
            elif(self.acbal<500):
                print("cant withdraw because account balance is less than 500")
            elif(no_of_transactions>3):
                print("greater than number of transactions")

    def validation(self):
        pin=int(input("Enter pin number"))
        if(pin==1234):
            obj.options()
        else:
            for i in range(2):
                if(pin==1234):
                    obj.options()
                    break
                else:
                    pin = int(input("Enter again"))
            print("blocked")
    def options(self):
        print("1.Deposit\n2.Withdraw\n3.bal Enquiry\n4.exit")
        while(True):
            choice = int(input("Enter choice"))

            if(choice==1):
                self.deposit()
            elif(choice==2):
                self.withdraw()
            elif(choice==3):
                self.balenquiry()
            else:
                exit(0)
            print("1.Deposit\n2.Withdraw\n3.bal Enquiry\n4.exit")

obj = Bank()
obj.validation()