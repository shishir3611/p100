class Atm:
    def __init__(self, cardNum, pin, cashAmount):
        self.cardNum = cardNum
        self.pin = pin
        self.cashAmount = cashAmount
    def cashWithdraw(self, amount):
        self.cashAmount -= amount
        print('You deducted £'+str(amount)+' and you have £'+str(self.cashAmount)+' left.')
    def cashDeposit(self, amount):
        self.cashAmount += amount
        print('You deposited £'+str(amount)+' and you have £'+str(self.cashAmount)+'.')
    def checkBalance(self):
        print('You have £'+str(self.cashAmount)+'.')
def main():
    card_number = input('Enter Card Number\n')
    pin_number = input('Enter Pin Number\n')
    new_member = Atm(card_number, pin_number, 84000)
    activity = input('Press 1 to withdraw cash\nPress 2 to deposit cash\nPress 3 to find your balance\n')
    if(int(activity) == 1):
        x = int(input('How much do you wish to withdraw\n'))
        new_member.cashWithdraw(x)
    elif(int(activity) == 2):
        x = int(input('How much do you wish to deposit\n'))
        new_member.cashDeposit(x)
    elif(int(activity) == 3):
        new_member.checkBalance()
    else:
        print('type a valid number please')
main()
    