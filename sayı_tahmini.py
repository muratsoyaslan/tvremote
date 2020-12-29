import random 
import time 

random_number=random.randint(1,40)
prediction_limit= 3

while True:

    prediction=int(input("Your Prediction?"))
    if(prediction < random_number ) :
        print("Checking your prediction if it is true ")
        time.sleep(2)

        print("Type bigger number than your last prediction")
        prediction_limit -= 1 
    elif (prediction > random_number):
        print("Checking your prediction if it is true ")
        time.sleep(2)
        print("type your prediction less number")
        prediction_limit -= 1
    else:
        print("Checking your prediction")  
        time.sleep(2)
        print("Congrulations!Your prediction is true",random_number)
        break
    if (prediction_limit==0):
        print("Your prediction limit is full")
        print("Random Number:",random_number)
        break
 



         