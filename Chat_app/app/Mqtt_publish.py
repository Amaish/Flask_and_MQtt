import time
import paho.mqtt.client as paho
import random
import os

broker="sungura1-angani-ke-host.africastalking.com"
port = 10883                         #Broker port
user = "amaina"                    #Connection username
password = "set_password"            #Connection password

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

Connected = False   #global variable for the state of the connection


client= paho.Client("Anthony-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
print("connecting to broker ",broker)
client.connect(broker, port)#connect
client.loop_start() #start loop to process received messages

while Connected != True:    #Wait for connection
    time.sleep(0.1)

print("publishing ")


try:
    count = []
    
    while True:
        temp = random.randrange(16,38)
        
        if temp<=25:
            print "Normal temparature ranges"
            count.append(temp)
            print count
            print "press CTRL + C to exit\n"
            time.sleep(1)
            
        else:
            client.publish("amaina/temperature",temp)#publish
            print "Current temperature reading is above 25 degrees\nWarning message sent " #+ str(temp) 
            time.sleep(0.5)
            print "Press CTRL + C to exit\n"
        
        while len(count) > 5:
            os.system('clear')
            count = []
            break
 
except KeyboardInterrupt:
    print "\nexiting"
    client.disconnect() #disconnect
    client.loop_stop() #stop loop


