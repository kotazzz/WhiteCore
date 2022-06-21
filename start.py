import sys

import whs

def read(filename):
	with open(f'{filename}.whc', 'r') as file:
		for n, line in enumerate(file, 1):
			line = line.rstrip('\n')
			try:
				whs.Core.run(line)
			except IndexError:
				print('Argument is not found')
			
read(sys.argv[1])
