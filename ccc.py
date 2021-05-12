
# connection with out class threading




import socket
import os
import time

    
    

port = 5000  
    
ddd = " \033[0;31m : \033[0;34m "
    
host = str(input("\n \033[42m\033[1;30m put Host\033[0;31m :\033[0;33m ")) 
    
dadd = str(input("\n \033[42m\033[1;30m put her name\033[0;31m :\033[0;33m "))



def client_program():
    x = False
    client_socket = socket.socket() 
    
    
    list = [">        ",'->       ','-->      ','--->     ','---->    ','----->   ','------>  ','-------> ','-------->']
    xx = 0
    while xx < 3 :
        
        for i in list:


            time.sleep (0.05)
            os.system("clear")

            
            n = " \n \n \n \033[0;31m[\033[0;36m↑↓\033[0;31m] \033[0;32msearch for connect \033[0;31m[\033[1;33m{}\033[0;31m]  ".format(i)

            print (n)
            
            xx += 1

    
    print ("\n\n                           \033[0;36mwhite ..")
    time.sleep(2)
    try:
        # instantiate
        client_socket.connect((host, port))
        # connect to the server
    except ConnectionRefusedError:
        
        os.system("clear")
        print(" \n \n \n                          \033[1;31mtry again ,,,\n \n \n \n \n \033[0;31m[\033[0;36m#\033[0;31m] \033[0;32m put \033[0;31m[\033[0;36many key\033[0;31m] \033[0;32m to try again . \n \n \033[0;31m[\033[0;36m#\033[0;31m] \033[0;32m if u need exit program put \033[0;31m[\033[0;36me\033[0;31m] \033[0;32m to do it .\n \n \n \n " )
        mess=input(" \033[0;31m[\033[0;36m$\033[0;31m] \033[42m\033[1;30m type here\033[0;31m"+" : \033[0;33m")
    
        if mess == "e":
            client_socket.close()
        else:
            client_program()
    else:
        x=True
    

    if x == True :
        xxx = -1
        print ("\n \n good !! , connection is found .\n")
        while xxx < 1 :

            mess = input("\033[0;31m [\033[0;36m->\033[0;31m] \033[42m\033[1;30m me"+"\033[0;31m "+":  \033[0;33m")
        
        
            client_socket.send(mess.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response
            print("\033[0;31m [\033[0;36m웃\033[0;31m] " +"\033[0;3m\033[45m"+dadd + ddd + data) 
        
            if mess == "bye":
                x = False
                client_socket.close()
            
                xxx = 1
    else :
        client_socket.close()

if __name__ == '__main__':
    client_program()
    
