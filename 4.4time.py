class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s
    def display(self):
        print("Hours =",self.__hour)
        print("Minutes =",self.__minute)
        print("Seconds =",self.__second)
    def __add__(self,other):
        hr=self.__hour+other.__hour
        mint=self.__minute+other.__minute
        sec=self.__second+other.__second
        total=(hr*3600)+(mint*60)+sec
        hrs=total/3600
        total=total%3600
        mins=total%60
        secs=total%60
        print("Total hours :",hrs)
        print("Total minutes :",mins)
        print("Total seconds :",secs)

t1=Time(8,36,25)
t2=Time(3,42,50)
t1.display()
t2.display()
t1+t2

