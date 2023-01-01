# class with private attribute
class Private_Class:
    def __init__(self):
        # assign initial ssn as private attribute
        self.__ssn = '888-22-6666'
    
    # getter function for private attribute
    def get(self):
        return self.__ssn

# setter function for private attribute
    def set(self,private):
        self.__ssn = private

# class with protected attribute
class Protected_Class:
    def __init__(self):
        # assign initial phone number as protected attribute
        self._phoneNum = '123-456-7890'

if __name__ == '__main__':
    # instantiate Private_Class object
    my_ssn = Private_Class()
    # get initial SSN
    print('Old SSN is ' + my_ssn.get() + '.')
    new_ssn = '654-99-8521'
    # set new SSN
    my_ssn.set(new_ssn)
    print('New SSN is ' + my_ssn.get() + '.')

    # instantiate Protected_Class object
    my_phoneNum = Protected_Class()
    # get initial phone num
    print('\nOld Phone Num is ' + my_phoneNum._phoneNum + '.')
    new_PhoneNum = '404-888-9632'
    # set new phone num
    my_phoneNum._phoneNum = new_PhoneNum
    # print new phone num
    print('New Phone Num is ' + my_phoneNum._phoneNum + '.')

