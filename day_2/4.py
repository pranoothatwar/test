f_num = [1,1]
i = 1
f = 0
while (f_num[i]<51):
	f = f_num[i] + f_num[i-1]
	i=i+1
	f_num.append(f)

for i in f_num:
	if(i<51):
		print i,	
	