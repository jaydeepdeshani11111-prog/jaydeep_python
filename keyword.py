#1.Basic Keyword Arguments.
def simple_interest(p:float,t:float,r:float):
    si=(p*r*t)/100
    print("simple interest:",si) 
#calling function.
simple_interest(p=10000,t= 2.5,r=3.5)

#2.add numbers.
def addnumbers (* args)
    total=0
    for num is args:
         total+=num
    return total
#calling function.
print(add.numbers(10,20))
print(add.numbers(5.10,15.20))