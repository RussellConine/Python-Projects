class Appliance():
    color = ''
    app_type = ''
    room = ''

    def __init__(self,color,app_type,room):
        self.color = color
        self.app_type = app_type
        self.room = room


    def install(self):
        return 'The {} is installed!'.format(self.app_type)


class Stove(Appliance):
    power_type = ''
    eye_count = 0
    has_oven = None

    def __init__(self,power_type,eye_count,has_oven):
        self.power_type = power_type
        self.eye_count = eye_count
        self.has_oven = has_oven


if __name__ == '__main__':
    a = Appliance('white', 'stove','kitchen')
    print('The {} {} is going in the {}.'.format(a.color,a.app_type,a.room))
    print(a.install())


    stove = Stove('electric',4,True)
    print('The {} stove has {} eyes'.format(stove.power_type,str(stove.eye_count)))