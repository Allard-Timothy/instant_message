import SocketServer

conn_port = port_number
conn_clients = {}


class Client:
    queue = []
    def __init__(self, conn_socket, conn_source, conn_dest):
        print "You're currently waiting, duh"
        self.socket = conn_socket
        print "Heads Up, here comes: %s" % self.socket
        self.user = conn_source
        print "User: " + self.user
        self.bro = conn_dest                       # bro_list :-)
        print "Bro: " + self.bro
        print "Created Bro"


class Handler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "Connected to", self.client_address
        while True:
            received_data = self.request.recv(port_number)
            if not received_data:
                break
            
   
            if received_data.startswith('%%%',0,3):              # client details
                print "Success"
                received_data = received_data.replace('%%%', '', 1).lstrip()    # get handling code
                QD = received_data.split('##',1)
                socket = self.request
                source = QD[0]
                dest = QD[1]
                client = client(socket, source, dest)
                conn_clients[source] = client                  # use username as key 
                socket.sendall('AUTH_OK')                 # send success message
                print "Connected " + source + "Success "       

            
            if received_data.startswith('$$$',0,3):   # send details to user
                source = received_data.replace('$$$', '', 1).lstrip()
                if len(conn_clients) > 1:              # check if more than 1 user     
                    conn_clients[source] = client
                    if len(client.queue) < 1:
                        client.socket.sendall(" ")
                    else:
                        messages = ""
                        for q in client.queue:
                            messages += q + '\n'
                        client.socket.sendall(msgs)
                        client.queue = []
                        print "Sent the messages " + client.user
                else:
                    socket.sendall(" ")

          
            if received_data.startswith('&&&',0,3):
        
                received_data = received_data.replace('###', '', 1).lstrip()
                QD = received_data.split('###',1)
                source = QD[0]
                text = QD[1]
                if text.strip != "":
                    print "Got some stuff here"
                    client_source = conn_clients[source]   #client source
                    client_dest = conn_clients[client_source.bro]     #client bro
                    msg = source+": "+text
                    print "Adding to list" + client_source.bro
                    client_dest.queue.append(msg)
                    print "Queue of: " + client_dest.user + " = %s" % client_dest.queue
                client_dest.socket.sendall(" ")
            else:
                if len(clients) < 2:
                    self.request.sendall(received_data)

        for client in conn_clients.values():
            if self.request == client.socket:
                client.socket.close()
                del conn_clients[client.user]
            

        print "Disconnected", self.client_address
        
server = SocketServer.ThreadingTCPServer(('',conn_port),Handler)
server.serve_forever()
