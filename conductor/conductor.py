
import paho.mqtt.client as mqtt     #import the client1
import time 

def on_message(client,userdata,message):
    reply = str(message.payload.decode("utf-8"))

    if(reply == "tracksAvailable"):
        print("The tracks on the SD cards are the following:")
        
    print(reply)  

def MQTT_publish(action,track=None,topic=-1):
    topics = ['STEPPERS_IN','XYLO_IN','PIANO_IN','TESLA_IN','ALL']
    #print("Transmitting ",action + track," to",topics[topic])
    if action == "PLAY":
        print("Transmitting ",action + track," to",topics[topic])
        client.publish(topics[topic],"PLAY"+track)               #transmit play signal 
    elif action == "STOP":
        print("Transmitting ",action,str(track),str(topics[topic]))
        client.publish(topics[topic],"STOP")                     #transmit stop signal
    elif action == "listTracks":
        client.publish(topics[topic],"listTracks")               #transmit listTracks signal
    elif action == "START":
        client.publish(topics[topic],"START")
    else:
        print("Not a valid action. Try again")
    print("Transmission over")

def MQTT_init():
    for i in range(1):
        try:
            #broker_address = '192.168.0.4'
            broker_address="192.168.4.1"        #connect to pi
            
            client.on_message=on_message        #attach callback
            client.connect(broker_address)      #connect to broker
            client.loop_start()                 #start the loop

            client.subscribe("STEPPERS_OUT")       #subscribe to steppers
            client.subscribe("XYLO_OUT")           #subscribe to XYLO
            client.subscribe("PIANO_OUT")          #subscribe to PIANO
            client.subscribe("TESLA_OUT")          #subscribe to TESLA
            client.subscribe("ALL")            #subscribe to ALL
        except TimeoutError as err:
            print("Check that the MQTT broker is running")
    
        
client = mqtt.Client("Conductor")   #create new instance



