import random
import time

class TV_Remote():

    def __init__ (self,tv_control="off",tv_volume=0,channel_list=["BBC"],channel="BBC"):
        self.tv_control = tv_control
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def tv_turnon(self):
        if(self.tv_control == "turn on") :
          print("tv is already on")
        else:
            print("tv is opening") 
            self.tv_control = "on"
    
    def tv_turnoff(self):
        if(self.tv_control == " turn off") :
          print("tv is already off")
        else:
          print("tv is closing")
    def Volume_control(self):

        while True:
            answer= input("decrease the volume: '<'\nincrease the volume: '>'\nExit: exit")  
            if (answer == "<"):
              if(self.tv_volume != 0):
                 self.tv_volume -= 1
                 print("TV volume:",self.tv_volume)
            elif(answer == ">"):
                if(self.tv_volume !=31):
                    self.tv_volume += 1
                    print("TV volume:",self.tv_volume)
            else:
                print("Volume is updated:",self.tv_volume) 
                break
    def channel_adding(self,channel_name):
        print("Channel being added...")
        time.sleep = 2
        self.channel_list.append(channel_name) 
        print("channel is added")
    def random_channel(self):
        random_value=random.randint(0,len(self.channel_list)-1)   
        self.channel = self.channel_list[random_value]
        print("Channel which is on now:",self.channel) 
    def __len__(self):
        return len(self.channel_list)
    def __str__(self):
        return("TV Control: {}\nTV Volume: {}\nChannel List: {}\nChannel which is on now: {}\n".format(self.tv_control,self.tv_volume,self.channel_list,self.channel))

remote = TV_Remote()
print("1-Turn on\n2-Turn off\n3-Volume control\n4-Add channel\n5-Learn how manny channels there are\n6-go to random channel\n7-TV information\nclick q for exit")

while True:
    action =  input("choose the action:")
    if (action == "q"):
        print("Program is ending...")
        break
    elif(action == "1"):
        remote.tv_turnon()
    elif(action == "2" ):
        remote.tv_turnoff()
    elif(action == "3"):
        remote.Volume_control()    
    elif(action == "4"):
        channel_names=input("Kanal isimlerini ',' ile ayırarak giriniz:")
        channel_list = channel_names.split(",")
        for new_adding_channel in channel_list:
            remote.adding_channel(new_adding_channel)
    elif(action == "5"):
        print("Number of channels:",len(remote)) 
    elif(action == "6"):
        remote.random_channel()
    elif(action == "7"):
        print(remote)
    else:
        print("invalid transaction")           
