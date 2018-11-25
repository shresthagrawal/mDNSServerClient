
from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo
from time import sleep
import socket
from typing import cast
 
# create a service class to store multiple services and handle it simoltaneously
class Service:
    def __init__(self, name, serviceType, info, address):
        self.name = name
        self.serviceType = serviceType
        self.info = info
        self.address= address

# create a list serviceDirectory which will store all the services
serviceDirectory = []      
 
class MyClient:
    # function to show the details of a service
    def showDetails(self):
        index = int(input("Index of the service whose details are required: "))
        info = serviceDirectory[index].info
        if info:
            print("  Address: %s:%d" % (socket.inet_ntoa(cast(bytes, info.address)), cast(int, info.port)))
            print("  Weight: %d, priority: %d" % (info.weight, info.priority))
            print("  Server: %s" % (info.server,))
            if info.properties:
                print("  Properties are:")
                for key, value in info.properties.items():
                    print("    %s: %s" % (key, value))
            else:
                print("  No properties")
        else:
            print("  No info")
        print('\n')

    # functions to list all services from the list
    def printAllServices(self):
        print("################################################################")
        print("#                        LIST OF SERVICES                      #")
        print("################################################################")
        for index, service in enumerate(serviceDirectory):
            print(" "+str(index)+"  "+service.name)
        # input user data to perform actions     
        index = input("\n Enter:\n 'r' to refresh" +
                      "\n 'e' to exit"+
                      "\n 'd' for detail of the services"+
                      "\n 'Index of the service' to estabish connection: ")    
        if(index=="r"):
            self.printAllServices()
        elif(index=="e"):  
            # close the zeroConf connection object
            zeroconf.close()
        elif(index=="d"):
            self.showDetails()
            self.printAllServices()
        else:
            if(int(index)<len(serviceDirectory)):
                self.connect(serviceDirectory[int(index)].address, serviceDirectory[int(index)].info.port)   
            else:
                print("incorrect index")      
       
    # add a new servce to the service list once a new sevice is detected
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        address = ".".join(map(str, info.address))
        newService = Service(name,type,info,address)
        serviceDirectory.append(newService)
    
    #connect to a service when the user requests to
    def connect(self, address, port):
        # create a socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((address,port))
        print("Enter 'e' to exit: ")
        while True:
            # get data from server
            response = client.recv(1024)
            print('Received from the Server :',str(response.decode('ascii'))) 
            # wait for user data
            inputData = input()
            # exit if e is enterd by the user
            if inputData == "e":
                break
             # else encode the data and send it back to the server   
            client.send(inputData.encode('ascii'))
        client.close()
        
        
    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")
 
zeroconf = Zeroconf()
listener = MyClient()
browser = ServiceBrowser(zeroconf, "_service._tcp.local.", listener)
 
if __name__ == "__main__": 
    sleep(1)
    listener.printAllServices()
