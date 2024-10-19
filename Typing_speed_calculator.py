from time import *
import random 

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay,2)
    speed = len(userinput)/time_roundoff
    return round(speed)


test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
"my name is vipin singh", "I love to watch anime with english subbed."]

while True:
    check = input("Ready for the test (yes/no): ").lower()
    if  check == "yes":
        test1 = random.choice(test)
        print("***** typing speed test *****")
        print(test1)
        print()
        print()
        time1 = time()
        testinput = input("Enter : ")
        time2 = time()

        print("speed: ",speed_time(time1,time2,testinput),"w/s")
        print("Error: ",mistake(test1,testinput))
    elif check == "no":
        print("Goodbye!")
        break
    else:
        print("wrong input!")