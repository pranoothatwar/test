def inp():
    return raw_input(" tell the operation (+, -, *, /, exit): ")

def inp_num():
    return float(raw_input(" first number: ")), float(raw_input(" second number: "))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return (a)/b

flag = True

while flag:
    i = inp()
    if i == 'exit':
        flag = False
    else:
        a,b = inp_num()
        if i =='+':
            print " answer of ",a,i,b," = ",add(a,b)
        elif i =='-':
            print " answer of ",a,i,b," = ",sub(a,b)
        elif i =='*':
            print " answer of ",a,i,b," = ",mul(a,b)
        elif i =='/':
            while(b ==0):
                print " invalid input, divide by zero is not allowed!\n enter them again"
                a,b = inp_num()
            print " answer of ",a,i,b," = ",div(a,b)
    
        
                     
                     
	
