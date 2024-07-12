import sys
import random

def help()->str:
	return f"Usage: python {sys.argv[0]} <message>"

if len(sys.argv)!=2:
	print(help())
	sys.exit(1)

for i in range(1,len(sys.argv)):
	if sys.argv[i] in ['-h','--help']:
		print(help())
		sys.exit(0)
	elif sys.argv[i]=='--version':
		print('1.0')
		sys.exit(0)

msg:str=sys.argv[1]
shift:int=random.randint(0,25)
shifted:str=''.join(chr((ord(i)-65+shift)%26+65) if i.isupper() else chr((ord(i)-97+shift)%26+97) if i.islower() else i for i in msg)
bin:str='|'.join(format(ord(i),'08b') for i in shifted)
word_list:list=bin.split('|'+format(ord(' '),'08b')+'|')
bin_list:list=[]*len(word_list)
for i in range(len(word_list)):
	tmp:list=[]*len(word_list[i])
	tmp=word_list[i].split('|')
	random.shuffle(tmp)
	bin_list.append('|'.join(tmp))
code:str=' '.join(bin_list)
print(code)