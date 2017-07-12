n = 10
for a in range(n):
    for b in range(n):
        for c in range(n):
            num = 100*a + 10*b + c
	    arm_num = a**3 + b**3 + c**3
            if num == arm_num:
                print "arm_num", arm_num