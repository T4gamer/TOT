
#connection with out class threading



import socket




port = 5000  
    
ddd = " \033[0;31m : \033[0;34m "
    
host = str(input("\n \033[42m\033[1;30m put Host\033[0;31m :\033[0;33m ")) 
    
dadd = str(input("\n \033[42m\033[1;30m put her name\033[0;31m :\033[0;33m "))



def server_program():
    # get the hostname

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))
        # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("\n    \033[0;32m Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print( dadd + ddd + str(data))
        data = input('\033[0;35m ===|> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
 