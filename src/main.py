import argparse
from ids import start_sniffing

if __name__ == "__main__":
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="A simple real-time Intrusion Detection System.")
    parser.add_argument("-i", "--interface", type=str, help="Network interface to sniff on (e.g., eth0).")

    args = parser.parse_args()

    # Start the IDS. Pass the selected interface if provided.
    start_sniffing(args.interface)