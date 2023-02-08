#!/bin/python3
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	print("-" * 50)
	print(f"Scanning target: {target}")
	print(f"Time started: {datetime.now()}")
	print("-" * 50)
	try:
		for port in range(50, 85):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target, port))
			if result == 0:
				print(f"Port {port} status: open")
			s.close()
	except KeyboardInterrupt:
		print(f"Exiting program")
		sys.exit()
	except socket.gaierror:
		print(f"Hostname couldn't be resolved")
		sys.exit()
	except socket.error:
		print(f"Couldn't connect to server")
		sys.exit()
			
else:
	print(f"Invalid number of arguments")
	print(f"Syntax: python3 scanner.py <ip>")
