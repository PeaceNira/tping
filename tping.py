#!/usr/bin/env python3
import socket
import time
import argparse
from termcolor import colored

def tcp_ping(host, port, count, interval, timeout):
    """
    Perform a TCP ping to the specified host and port.

    :param host: Target hostname or IP address.
    :param port: Target port number.
    :param count: Number of pings to attempt.
    :param interval: Interval in seconds between pings.
    :param timeout: Timeout for each connection attempt in seconds.
    """
    print(colored(f"Pinging {host}:{port} with TCP packets:", "cyan"))

    success_count = 0
    total_time = 0

    for i in range(count):
        try:
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            # Record the start time
            start_time = time.time()

            # Attempt to connect to the target
            sock.connect((host, port))

            # Calculate round-trip time
            rtt = (time.time() - start_time) * 1000  # Convert to milliseconds
            total_time += rtt
            success_count += 1

            print(colored(f"Reply from {host}:{port}: time={rtt:.2f} ms", "green"))
        except socket.timeout:
            print(colored(f"Request timed out for {host}:{port}", "yellow"))
        except socket.error as e:
            print(colored(f"Connection error for {host}:{port}: {e}", "red"))
        finally:
            sock.close()

        # Wait for the specified interval before the next attempt
        if i < count - 1:
            time.sleep(interval)

    print("\n--- TCP ping statistics ---")
    print(f"{count} packets transmitted, {success_count} received, {(count - success_count) / count * 100:.1f}% packet loss")
    if success_count > 0:
        print(f"round-trip min/avg/max = {total_time / success_count:.2f}/{total_time / count:.2f}/{total_time:.2f} ms")
    else:
        print("No successful connections.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple TCP ping utility.")
    parser.add_argument("host", type=str, help="Target hostname or IP address.")
    parser.add_argument("port", type=int, help="Target port number.")
    parser.add_argument("-c", "--count", type=int, default=4, help="Number of pings to send (default: 4).")
    parser.add_argument("-i", "--interval", type=float, default=1, help="Interval between pings in seconds (default: 1).")
    parser.add_argument("-t", "--timeout", type=float, default=2, help="Timeout for each ping in seconds (default: 2).")

    args = parser.parse_args()

    tcp_ping(args.host, args.port, args.count, args.interval, args.timeout)

