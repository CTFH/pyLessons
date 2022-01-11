def weather():
    print('今日は晴です')
weather()


def calc_circle_area(r):
    return r**2*3.14
print(calc_circle_area(10))


import datetime
def nowstr():
    dt=datetime.datetime.today()
    return f'{dt.hour}時{dt.minute}分{dt.second}秒'
print(nowstr())


def nowint():
    dt=datetime.datetime.today()
    return dt.hour, dt.minute, dt.second

h,m,s=nowint() #戻り値タプル
print(h,m,s)


def is_leapyear(year):
    return year % 400 == 0 or (year % 4 == 0 and year%100 !=0)
print(is_leapyear(1600)) #True
print(is_leapyear(100))  #False
print(is_leapyear(2012)) #True
print(is_leapyear(2013)) #False

year=int(input('年>>'))
if is_leapyear(year):
    print(f'{year}年はうるう年です')
else:
    print(f'{year}年はうるう年ではありません')
