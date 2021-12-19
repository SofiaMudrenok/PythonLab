import datetime

class Ram:
    def __init__(self, _date, _manufacturer = 'none', _storage=2, _price=0):
        self.date = _date
        self.manufacturer = _manufacturer
        self.storage = _storage
        self.price = _price
    
    def age(self):
        date_now = datetime.datetime.today()
        time_var = date_now - self.date
        return time_var

    def V(self):
        volume_in_gb = self.storage/1024
        volume_in_kb =self.storage* 1024
        volume_in_b =self.storage/(1024*1024*8)
        print(volume_in_b)
        print(volume_in_gb)
        print(volume_in_kb)
     
    def ram_capacity(self):
        type_=input("тип ємкості (gb/kb/b): ")
        vol =input("кількість ")
        if type_.lower()=='gb':
            e_vol=vol/1024
            if self.storage>=e_vol :
                print("поміститься")
            else:
                print("нет")
        elif type_.lower()=='kb':
            e_vol=vol*1024
            if self.storage>=e_vol :
                print("поміститься")
            else:
                print("нет")
        elif type_.lower()=='b':
            e_vol=vol/(1024*1024*8)
            if self.storage>=e_vol :
                print("поміститься")
            else:
                print("нет")
        else:
            print("error")


########################


memory=Ram(datetime.datetime(2003,5,4))
m_age=memory.age()
print(m_age)




