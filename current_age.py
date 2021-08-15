from datetime import date
class emrooz:
    
    count=0
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def cal_age(self):
        today=date.today()
        age=today.year-self.year-((today.month,today.day)<(self.month,self.day))
        return age
aknoon=date.today()
aknoon=aknoon.year
birth=input("pls enter your birth date like(2000/10/11):")
birth=birth.replace('/',' ')
birth=birth.split()
birth=list(map(int,birth))
if birth[1]>12 or birth[2]>31 or birth[0]>aknoon:
    print('WRONG')
else:
    a=emrooz(birth[0],birth[1],birth[2])
    print(a.cal_age())


