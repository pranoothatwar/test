def inp():
    return str(raw_input("enter any month or day of week: "))

value = {'monday':"first day",
        'tuesday':'second day',
        'wednesday':'third day',
        'thursday':'fourth day',
        'friday' :'fifth day',
        'saturday' :'sixth day',
        'sunday':'seventh day',
        'january' :'first month',
        'february':'second month',
        'march':'third month',
        'april':'fourth month',
        'may':'fifth month',
        'june':'sixth month',
        'july':'seventh month',
        'august':'eighth month',
        'september':'ninth month',
        'october':'tenth month',
        'november':'eleventh month',
        'december':'twelfth month',
        }
flag = True
print "to exit write exit!"

while(flag):
    a=inp()
    if str.lower(a) == 'exit':
        flag = False
    else:
        try:
            print value[str.lower(a)]
        
        except:
            print "enter valid input!"
