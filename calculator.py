import socket
import sys
import time
import errno
import math         
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("\t\t~~~~~~~~~~ Online Calculator using Python ~~~~~~~~~~  \n\t\t\t   Function : \tLOG(log), \n\t\t\t\t\tSQUARE ROOT(sqrt), \n\t\t\t\t\tEXPONENTIAL(exp) \n\t\t\t   Format: log/sqrt/exp <enter num> \n\t\t\t   Example: log 10 \n\t\t\t\t !!'exit' to GET OUT!!"))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")
        
        try:
            operation, value = data.split()
            op = str(operation)
            num = int(value)
        
            if op[0] == 'l':
                op = '\t\t\t   Log'
                answer = math.log10(num)
            elif op[0] == 's':
                op = '\t\t\t   Square root'
                answer = math.sqrt(num)
            elif op[0] == 'e':
                op = '\t\t\t   Exponential'
                answer = math.exp(num)
            else:
                answer = ('Error!')
        
            sendAnswer = (str(op) + ' ' + str(num) + ' = ' + str(answer))
            print ('GOOD JOB SERVER!')
        except:
            print ('JOB DONE')
            sendAnswer = ('THANK YOU FOR USING PYTHON CALCULATOR, BYE')
        
        if not data:
            break
            
        s_sock.send(str.encode(sendAnswer))
       
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8080))
    print("Listening...\nConnected.....")
    s.listen(28)
    
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('socket error')

            except Exception as e:        
                print("an exception happened!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
