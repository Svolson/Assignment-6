import logging

logging.basicConfig(filename='logginginfo.log',level=logging.INFO,
                    format = '%(asctime)s:%(levelname)s:%(message)s')
def add(x , y):
    return x + y

def sub (x , y):
    return x - y

def multi(x , y):
    return x * y

def div(x , y):
    return x / y

def operation(num1: float  , num2: int)-> float:
     # The number can be int or float
    if not isinstance(num1 ,int) and not isinstance(num1 , float):
        raise TypeError('the num1 can only be int or float')
    
     # The num2 can only be int
    if not isinstance(num2, int):
        raise TypeError("The num2 can only be of int type")
    
    # If number > 0, we compute the calculation
    if num1 >= 0:
        return round(num1 ** num2, 2)
    raise TypeError("The number can only be >= 0")

num1 = float(input("number:"))
num2 = int(input('number:'))
      
add_result = add(num1 , num2)
logging.info(add_result)

sub_result = sub(num1 , num2)
logging.info(sub_result)

muli_result = multi(num1,num2)
logging.info(muli_result)

div_result = div(num1,num2)
logging.info(div_result)

