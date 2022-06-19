import sys
import re
import os

def lex(characters, token_exprs):
	pos = 0
	tokens = []
	while pos < len(characters):
		match = None
		for token_expr in token_exprs:
			pattern, tag = token_expr
			regex = re.compile(pattern)
			match = regex.match(characters, pos)
			if match:
				text = match.group(0)
				if tag:
					token = [text, tag]
					tokens.append(token)
				break
		if not match:
			sys.stderr.write('Illegal character: %s\n' % characters[pos])
			exit()
		else:
			pos = match.end(0)
	return tokens