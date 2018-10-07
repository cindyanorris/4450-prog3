#!/bin/python3

from socket import *
import sys
import signal

#This is executed if the user types a CTRL-C
#It calls a function to write the cache directory to disk
#and it closes the listening socket.
def handleSIGINT(sig, frame):
   print("\nUpdating cache directory file");
   #add a call to your function that updates the cache
   #directory file

   print("Closing listening socket and terminating.")
   mySocket.close();
   sys.exit(0);

if (len(sys.argv) > 1 and sys.argv[1] == "clean"):
    #Add a call to your function that will 
    #delete the cache directory and the cached files
else:
    #register SIGINT signal handler
    signal.signal(signal.SIGINT, handleSIGINT)
    port =  #fill in your port number
    mySocket = socket(AF_INET, SOCK_STREAM)
    mySocket.bind(('', port))
    mySocket.listen(1)
    print("Server is listening on socket " + str(port))
    while 1:
        #accept the request
        #get the response
        #send the response
        #close the connection

