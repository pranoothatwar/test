password = raw_input("enter passkey: ")
flag = False

def symb(word):
        #sym
        flag_1 = False
        for i in word:
                if (ord(i)==38 or ord(i)==35 or ord(i)==64):
                        flag_1 = True
        #print flag_1,

        #num
        flag_2 = False
        for i in word:
                if (ord(i)>47 and ord(i)<58):
                        flag_2 = True
        #print flag_2,

        #caps
        flag_3 = False
        for i in word:
                if (ord(i)>64 and ord(i)<91):
                        flag_3 = True
        #print flag_3,                        

        #lower
        flag_4 = False
        for i in word:
                if (ord(i)>96 and ord(i)<123):
                        flag_4 = True
        #print flag_4,

        #len
        flag_5= False
        if(len(word)<17 and len(word)>5):
                flag_5 = True
        #print flag_5,

        return (flag_1)and(flag_2)and(flag_3)and(flag_4)and(flag_5)

if symb(password):
        print "valid"
else:
        print "not valid"
	
