import sys

def get_code_ascii(code:str)->str:
	words:list=code.split(' ')
	result:str=''
	for word in words:
		letters:list=word.split('|')
		decoded_word:str=''
		for letter in letters:
			decoded_word+=chr(int(letter,2))
		result+=decoded_word+' '
	return result.strip()

dictionary_length:dict={}
dictionary_frequency:dict={}
with open('./word_len_freq.csv','r') as file:
	for line in file:
		word:str=line.strip().split('\t')[0]
		length:int=int(line.strip().split('\t')[1])
		dictionary_length[word]=length
		frequency:float=float(line.strip().split('\t')[2])
		dictionary_frequency[word]=frequency

def get_words_with_length(length:int)->list:
	sorted_words:list=list(dictionary_length)
	l:int=0
	r:int=len(sorted_words)
	while l<r:
		m:int=(l+r)//2
		if dictionary_length[sorted_words[m]]<length:
			l=m+1
		else:
			r=m
	min_index:int=l
	l:int=0
	r:int=len(sorted_words)
	while l<r:
		m:int=(l+r)//2
		if dictionary_length[sorted_words[m]]<=length:
			l=m+1
		else:
			r=m
	max_index:int=l
	return sorted_words[min_index:max_index]

def get_words_with_length_and_letters(length:int,letters:str)->list:
	words_with_length:list=get_words_with_length(length)
	result:list=[]
	for word in words_with_length:
		if all(letters.count(letter)>=word.count(letter) for letter in word):
			result.append(word)
	return result

def get_shift_word(word:str,shift:int)->str:
	result:str=''
	for letter in word:
		result+=chr((ord(letter)-65+shift)%26+65) if letter.isupper() else chr((ord(letter)-97+shift)%26+97) if letter.islower() else letter
	return result

def get_most_common_words(arr:list)->list:
	arr.sort(key=lambda x:dictionary_frequency[x],reverse=True)
	return arr

def cryptanalysis(code_ascii:str,shift:int=0)->str:
	new_code_ascii:str=get_shift_word(code_ascii,shift)
	words:list=new_code_ascii.split(' ')
	result:str=''
	for word in words:
		length:int=len(word)
		possible_words:list=get_words_with_length_and_letters(length,word)
		if len(possible_words)>0:
			result+='|'.join(get_most_common_words(possible_words))+' '
		else:
			result=' '
	if result.endswith("  ") or (result.startswith(" ") and result.endswith(" ")):
		result=''
	return result.strip()

def help()->str:
	return f"Usage: python {sys.argv[0]} <code>"

if len(sys.argv)!=2:
	print(help())
	sys.exit(1)

for i in range(1,len(sys.argv)):
	if sys.argv[i] in ["-h","--help"]:
		print(help())
		sys.exit(0)
	elif sys.argv[i]=="--version":
		print("1.0")
		sys.exit(0)

code:str=sys.argv[1]

code_ascii:str=get_code_ascii(code)
print(code_ascii)
print(''.join(['-' for i in range(len(code_ascii))]))
for i in range(26):
	ret:str=cryptanalysis(code_ascii.lower(),i)
	if len(ret)>0:
		ret=ret.split(' ')
		for j in range(len(ret)):
			words:list=ret[j].split('|')
			end:str='|' if len(words)>1 else ''
			ret[j]=f"\033[32m{words[0]}\033[0m{end+'|'.join(words[1:])}"
		ret=' '.join(ret)
		print(f"{get_shift_word(code_ascii,i)} (-{i})\t\t{ret}")
# TODO: classify words as nouns, verbs, etc, so that the output can be narrowed down and improved even more since english has conventions such as an adjective being before a noun
