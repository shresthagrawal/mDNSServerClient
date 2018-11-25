from zeroconf import ServiceInfo, Zeroconf
import random
# import socket programming library 
import socket

# import thread module 
from _thread import *
import threading 


#server work
def work(data):
    return random.randint(0,int(data))

# thread fuction 
def workerThread(clientSocket):
    while True: 
        clientSocket.send(("Enter Max Value of the Random Number\n").encode('ascii')) 
        userData = str((clientSocket.recv(1024)).decode('ascii'))
        print("User Entered:"+ userData) 
        if (userData=="e"): 
            break 
        #doAnythingFromData()
        result = str(work(userData))+"\n"
        clientSocket.send(result.encode('ascii'))

    #Close Connection 
    clientSocket.close() 
            

# function to register service for mDNS
def registerService(info, name, port,zeroconf):
	zeroconf.register_service(info)
	print(f"{name}:{port} Service Registered")

def startListening(ip, port, zeroconf, info):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    connection.bind((ip, port)) 
    # put the socket into listening mode 
    connection.listen(5) 
    print("Listening for requests...")

    while True: 
        # establish connection with client 
        connRequest, address = connection.accept() 
        print('Connected to :', address[0], ':', address[1]) 
        # create a worker thread for the new request 
        start_new_thread(workerThread, (connRequest,)) 
    zeroconf.unregister_service(info)
    zeroconf.close()    
    connection.close() 
 
if __name__ == "__main__": 
    ip_ = input("Enter Ip:")
    port_ = int(input("Enter Port:"))
    name_ = input("Enter Name:")
    info_ = ServiceInfo("_service._tcp.local.",
                   name_ + "._service._tcp.local.",
                   socket.inet_aton(ip_), int(port_), 0, 0,
                   {}, "ash-2.local.")
    zeroconf_ = Zeroconf()
    registerService(info_,name_,port_,zeroconf_)
    startListening(ip_,int(port_),zeroconf_,info_)
	 
	