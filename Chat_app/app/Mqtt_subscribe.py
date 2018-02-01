import paho.mqtt.client as mqttClient
import time
import os
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

def on_message(client, userdata, message, temp = [] ):
    print ("Message received\nTemperature too high Current temperature is: "  + str (message.payload))
    global value
    time.sleep (1)
    os.system('clear')
    temp.append(int (message.payload))
    print ("All readings are:")
    print (temp)
    for reading in temp:
        value = str (reading)
    
   
Connected = False   #global variable for the state of the connection
 
broker_address= "sungura1-angani-ke-host.africastalking.com"  #Broker address
port = 10883                         #Broker port
user = "amaina"                    #Connection username
password = "TamaRind"            #Connection password
 
client = mqttClient.Client("Amaina")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback


client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("amaina/temperature")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()
