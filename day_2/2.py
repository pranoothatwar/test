inp = (raw_input("give temp of form 23C or 23F: "))
unit = inp[-1]
temp = int(inp[:-1])

if unit=='F' or unit =='f' :
	print inp, "is ",(temp-32)/1.8,"C"
else:
	print inp, "is ",(temp*1.8)+32
	