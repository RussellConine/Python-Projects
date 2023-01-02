from abc import ABC, abstractmethod

class car(ABC):
    def paySlip(self, amount):
        print('Purchase amount: ', amount)

    # function telling us to pass in an argument
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):

    # define how to implement payment from parent payslip class
    def payment(self, amount):
        print('Your purchase amount of {} exceeded limit'.format(amount))

class CreditCardPayment(car):
    def payment(self,amount):
        print('Purchase amount on credit card: {}'.format(amount))

obj = DebitCardPayment()
obj.paySlip('$400')

obj2 = CreditCardPayment()
obj2.paySlip('$500')
obj2.payment('500')