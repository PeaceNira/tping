# TCP Ping Utility

A Python script that mimics the functionality of `paping`, a TCP ping utility. It tests the availability and latency of a specific TCP port on a target host.

## Features
- **TCP Ping**: Checks connectivity to a specified host and port.
- **Colored Output**: Uses colors to indicate success (green), timeout (yellow), and errors (red).
- **Statistics Summary**: Provides a summary of packet transmission, success rate, packet loss, and round-trip time (min/avg/max).
- **Customizable Options**: Number of pings, interval between pings, and timeout duration can be configured.

## Requirements
- Python 3.x
- `termcolor` library (for colored output)

### Install `termcolor`:
```bash
pip install termcolor
```

## Usage
### Command Syntax
```bash
python tcp_ping.py <host> <port> [-c COUNT] [-i INTERVAL] [-t TIMEOUT]
```

### Arguments:
- `host` (required): Target hostname or IP address.
- `port` (required): Target port number.
- `-c`, `--count`: Number of pings to send (default: 4).
- `-i`, `--interval`: Interval between pings in seconds (default: 1).
- `-t`, `--timeout`: Timeout for each ping in seconds (default: 2).

### Examples:
1. Ping `example.com` on port `80` four times (default settings):
   ```bash
   python tcp_ping.py example.com 80
   ```

2. Ping `192.168.1.1` on port `22` with a 1-second timeout:
   ```bash
   python tcp_ping.py 192.168.1.1 22 -t 1
   ```

## Making the Script Executable
To simplify usage, you can make the script executable and move it to a directory in your `PATH`.

1. **Make Executable**:
   ```bash
   chmod +x tcp_ping.py
   ```

2. **Move to `PATH`**:
   ```bash
   mv tcp_ping.py ~/.local/bin/paping
   ```

3. **Run the Script**:
   ```bash
   paping example.com 80
   ```

