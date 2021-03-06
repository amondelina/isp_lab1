import argparse


default_name = 'World'
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default=default_name)
name = parser.parse_args().name
if not name.isalpha():
	name = default_name
name = name.lower()
name = name[0].upper() + name[1:]
print('Hello, ', name, '!', sep='')