import socket

ClientSocket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8")) #startmodify

print('Math calculator')
print('Function available:')
print('Logarithmic Expression = l')
print('Square Root = s')
print('Exponential Expression = e')
print('Exit calculator = x')
print('Please type input in [*function*:*number*] format, exp = s:123')
print ("\n")
while True:
    
    Input = input('Enter the function and number : ')
    
    if Input == 'x':
        break
    
    else:  
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print('Answer for calculation: ')
        print(Response.decode('utf-8')) #endmodify

ClientSocket.close()
