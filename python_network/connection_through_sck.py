import socket
s=socket.socket()
host=socket.gethostname()#get local machine name
port=45677#reserve a type for your n/w
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("Got connection fron",addr)
    
    c.send(b"Thankyou for connecting")
    c.close()

