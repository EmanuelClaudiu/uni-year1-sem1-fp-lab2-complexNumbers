def create_number(x,y): #creates the number as a list
    n=[]
    set_rpart(n,x)
    set_ipart(n,y)
    return n
def set_rpart(n,rpart): #sets the real part
    n.append(rpart)
def set_ipart(n,ipart): #sets the imaginary part
    n.append(ipart)
def get_rpart(n): #returns the real part
    return n[0]
def get_ipart(n): #returns the imaginary part
    return n[1]
def add_numbers(data): #allows adding numbers to the list
    nr = int(input("How many numbers would you like to add to the list? "))
    while nr>0:
        x = int(input("the real part of the number is: "))
        y = int(input("the imaginary part of the number is: "))
        nr = nr -1
        data.append(create_number(x,y))
    return data
def init_numbers(): #it initializes the program with 10 default values
    ini=[]
    ini.append(create_number(2,5))
    ini.append(create_number(4,-2))
    ini.append(create_number(-5,5))
    ini.append(create_number(1,4))
    ini.append(create_number(15,1))
    ini.append(create_number(-2,3))
    ini.append(create_number(-1,7))
    ini.append(create_number(12,-4))
    ini.append(create_number(6,-1))
    ini.append(create_number(7,-4))
    return ini
