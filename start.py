import whs
import sys
def read(filename):
	with open(f'{filename}.whc', 'r') as file:
		for n, line in enumerate(file, 1):
			line = line.rstrip('\n')
			try:
				whs.Core.imp(line)
			except IndexError as error:
				print(error)
			
read('my')