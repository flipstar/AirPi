import output
import time
#import paho.mqtt.client as mqtt
import paho.mqtt.client as paho_mqtt

class mqtt(output.Output):
       requiredData = []
       optionalData = []
       def __init__(self,data):
               pass

       def outputData(self,dataPoints):
               client = paho_mqtt.Client(client_id="AirPi")
               client.connect("10.11.14.55", 1883, 60)

               client.loop_start()

               for i in dataPoints:
                      client.publish("home/keller/airpi/" + i["name"], str(i["value"]))
               client.loop_stop() 
               client.disconnect()

               return True

