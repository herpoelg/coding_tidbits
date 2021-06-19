person1 = "Gerard"
person2 = "Finchy"

print(person1)
print(person2)
#> can be hard to guess which one is person1 and person2 when checking the output

#this can be a solution, but it is tedious
print("person1:", person1)
print("person2:", person2)

#time for some icecream: a Python library that makes print debugging more readable with minimal code.
#icecream will show the output, the function and its arguments
# pip install icecream

from icecream import ic

def power_up(num,pow):
    return num **pow

ic(power_up(5,2))
ic(power_up(4,4))

#checking code execution without the need to add prints

def welcomeMaster(sithLord:"Herpoelaert"):
    if sithLord=="Herpoelaert":
        print("Welcome, master")
    else:
        print("Do not enter this realm")

welcomeMaster("Herpoelaert")

def welcomeIceCreamMaster(sithLord:"Herpoelaert"):
    if sithLord=="Herpoelaert":
        ic()
    else:
        ic()
welcomeIceCreamMaster("Herpoelaert") #you will see that line 36 has been executed

#adding a custom icecream prefix (eg time, ie the sprinkles on the icecream)
from datetime import datetime
import time

#mistake: this will set the prefix once, so each timestamp will be the same
ic.configureOutput(prefix=f'{datetime.now()}|>>> ')

time.sleep(3)
welcomeIceCreamMaster("Herpoelaert")
time.sleep(5)
welcomeIceCreamMaster("Duyck")

#setting up a dynamic prefix
def getnow():
    return f'{datetime.now()}>>>'

ic.configureOutput(prefix=getnow)
time.sleep(3)
welcomeIceCreamMaster("Herpoelaert")
time.sleep(5)
welcomeIceCreamMaster("Duyck")

#adding more context:
ic.configureOutput(includeContext=True)
time.sleep(2)
welcomeIceCreamMaster("Duyck")
