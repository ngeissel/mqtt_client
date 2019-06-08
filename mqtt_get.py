import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    msg = message.payload.decode('UTF-8')
    print("Message received: %s"%msg)

Connected = False   #global variable for the state of the connection

broker_address= "m23.cloudmqtt.com"  #Broker address
port = 10243                         #Broker port
user = "iscknkjs"                    #Connection username
password = "zfpeW-8BkJ0j"            #Connection password

client = mqttClient.Client("PythonTest")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("python/test")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
