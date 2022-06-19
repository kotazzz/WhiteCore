import lexer

class Vars():
	codes = []
	vars = []
	cache =
	libName = []
	libImp = []
	libFunc = []
	
RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'
SA       = 'SPLITARG'
ARG      = 'ARG'
base = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'[0-9]+',                INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
    (r'[А-Яа-я][А-Яа-я0-9_]*', ID),
]

def ws_imp(characters):
    return lexer.lex(characters, base)
    
class Core():
	def imp(cmd):
		vars = Vars.vars
		token = ws_imp(cmd)
		if token == []:
			pass
		elif token[0][0] == 'use':
			with open(f'{token[1][0]}.py', 'r') as file:
				for n, line in enumerate(file, 1):
					if n == 2:
						libname = line.replace('#', '')
						libname = libname.split(' ')[0]
						Vars.libName += [libname]
					if n == 3:
						libimp = line.replace('#', '')
						libimp = libimp.split('/')
						
						Vars.libImp += [libimp]
						libimp = libimp.pop(len(libimp)-1)
					if n == 4:
						libfunc = line.replace('#', '')
						libfunc = libfunc.split('/')
						Vars.libFunc += [libfunc]
						libfunc = libfunc.pop(len(libfunc)-1)
					else:
						pass
		else:
			lib = []
			for libs in Vars.libName:
				lib.append(__import__(libs))
			for index, keyword in enumerate(Vars.libImp):
				for ptdindex, method in enumerate(keyword):
					if token[0][0] == method:
						exec(f'lib[index].{Vars.libFunc[index][ptdindex]}')
