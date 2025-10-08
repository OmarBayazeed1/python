#109.Implement encapsulation with private attributes
class BankAccount:
    def __init__(self,amount):
        self.__amount=amount
    def deposite(self,amount):
        if amount>0:
            self.__amount+=amount
        else:
            print('please deposite a positive amount')
    def withdraw(self,amount):
        if amount>0 and amount<self.__amount:
                self.__amount-=amount
        else:
            print('Insufficient funds or invalid amount')

        
    def get_amount(self):
        return self.__amount
while True:
    try:
        user_input=float(input('please enter initial value in bankAccount:'))
        b=BankAccount(user_input)
        print('amount is ',b.get_amount())
        user_deposite=float(input('please enter deposite :'))
        b.deposite(user_deposite)
        print('amount is ',b.get_amount())
        user_withdraw=float(input('please enter withdraw :'))
        b.withdraw(user_withdraw)
        print('amount is ',b.get_amount())
        break
    
    except ValueError:
        print('ValueError, retry with numaric values')    
        

