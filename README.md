# Real-Time Intrusion Detection System (IDS)  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>

![GitHub last commit](https://img.shields.io/github/last-commit/dimuzzo/arduino-exercises?style=flat-square&logo=github&label=Last%20Commit)
![GitHub repo size](https://img.shields.io/github/repo-size/dimuzzo/arduino-exercises?style=flat-square&logo=github&label=Repo%20Size)
![GitHub stars](https://img.shields.io/github/stars/dimuzzo/arduino-exercises?style=flat-square&logo=github&label=Stars)

This project is a simple real-time Intrusion Detection System (IDS) built with Python and Scapy. It's designed to monitor network traffic and detect potential threats, such as SYN Flood attacks.

This is a learning project based on the concepts described in [this freeCodeCamp article](https://www.freecodecamp.org/news/build-a-real-time-intrusion-detection-system-with-python/).

## Features

-   **Real-time Packet Sniffing**: Captures and analyzes network packets on the fly.
-   **SYN Flood Detection**: Identifies potential Denial-of-Service (DoS) attacks by monitoring the rate of SYN packets from a single source IP.
-   **Configurable**: Easily adjust detection parameters like the time window and packet thresholds.

## How It Works

The IDS listens to network traffic on a specified interface. For each packet, it checks if it's a TCP packet with the SYN flag set. It maintains a record of recent SYN packets for each source IP address. If the number of SYN packets from a single IP exceeds a defined threshold within a specific time window, it raises an alert.

## Requirements

-   Python 3.7+
-   Scapy

You will also need administrative/root privileges to run the packet sniffer.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dimuzzo/intrusion-detection-tester.git
    cd intrusion-detection-tester
    ```

2.  **Install the dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    venv\Scripts\activate

    # Install the required packages
    pip install -r requirements.txt
    ```

## Usage

You need to run the script with root privileges to allow Scapy to access raw sockets for packet sniffing.

```bash
python src/main.py
```

You can also specify a network interface to monitor:

```bash
python src/main.py --interface eth0
```

The script will start monitoring the traffic and print an alert to the console if a potential SYN flood attack is detected.

## Disclaimer

This is a basic educational tool and should not be used as a standalone, production-grade security solution.

---

> Created with passion by [dimuzzo](https://github.com/dimuzzo)

