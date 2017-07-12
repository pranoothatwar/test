city = {'madras':'TN',
        'mumbai':'MH',
        'bangalore':'KA',
        'delhi':'DL',
        'nagpur':'MH',
        'kharagpur':'WB',
        }

inp= raw_input('enter city name as MH or KA or TN or WB or DL: ')
print "The city is in the state of ", [(key) for key,value in city.items() if value==str.upper
                                       (inp)]
