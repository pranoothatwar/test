n = []

def dec2bin(num):
        rem = []
        for i in range(5):
                rem.append(num%2)
                num = num/2
        return rem[4],rem[3],rem[2],rem[1],rem[0]

def comp(num):
        return (1-(num%2))


for i in range(5):
        m = []
        for j in range(5):
                t = i*5 +j
                a,b,c,d,e = dec2bin(t)
                y = (comp(a)*comp(d)*e) or (comp(a)*comp(c)*d) or (comp(a)*b*c) or (comp(b)*comp(c)*d*e) or (a*comp(b)*c*comp(d)*comp(e)) or (a*b*comp(c)*comp(d)*comp(e))
                if y%2==1:
                        m.append("*")
                else:
                        m.append(" ")
        n.append(m)


for i in n:
        for j in i:
                print j,
        print "\n"
                
