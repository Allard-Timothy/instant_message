import socket, threading, time, msvcrt

print "Fill this out"
url_input = raw_input("URL: ")
port_input = raw_input("Port: ")
print "Starting Instant Messenger: " + port

socketOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketOut.connect((url, int(port)))



print "Fill out below"
from_user = raw_input("User id: ")
to_user = raw_input("Bro id: ")


print """Connecting..."""



socketOut.sendall('@@@'+from_user+'##'+to_user)     # user details and response
response = socketOut.recv(port number)

def listener():
    while True:
        time.sleep(3)
        socketOut.sendall('$$$'+from_user)
        response = socketOut.recv(####)
        if response != " ":
            print "\n" + response


if response == 'All Good':
    resp_data = ""
    target_thread = threading.Thread(target=listener)
    target_thread.setDaemon(1)
    target_thread.start()
    while True:
        if msvcrt.kbhit():
            character = msvcrt.get()
        else:
            character = None
        if character:
            if character != '\n':
                data += character
            else:
                print '\n'
                socketOut.sendall('###'+from_user+'##'+data)
                response = socketOut.recv(###)
                if response != " ":
                    print response
                resp_data = ""

else:
    print "Doh!!!....Try again dude!"
        
socketOut.close()
