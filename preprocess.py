# Delete all acronyms from words.csv and save the result in words2.csv
# out:str=''
# with open('./words.csv','r') as file:
# 	for line in file:
# 		acronym:bool=False
# 		for c in line:
# 			if c.islower():
# 				acronym=False
# 				break
# 			else:
# 				acronym=True
# 		if not acronym:
# 			out+=line.lower()
# with open('./words2.csv','w') as file:
# 	file.write(out)

# Sort the words in words2.csv by length and save the result in words3.csv
# words:dict={}
# with open('./words2.csv','r') as file:
# 	for line in file:
# 		words[line.strip()]=len(line.strip())
# sorted_words:list=[]
# for word in words:
# 	l:int=0
# 	r:int=len(sorted_words)
# 	while l<r:
# 		m:int=(l+r)//2
# 		if words[word]<words[sorted_words[m]]:
# 			r=m
# 		else:
# 			l=m+1
# 	sorted_words.insert(l,word)
# with open('./words3.csv','w') as file:
# 	for word in sorted_words:
# 		file.write(word.replace("\"",'')+'\t'+str(words[word]-2)+'\n')

# Count the frequency of each unigram in unigram_freq.csv and save the result as a percentage in unigram_freq2.csv
# unigrams:dict={}
# total:int=0
# with open('./unigram_freq.csv','r') as file:
# 	for line in file:
# 		word:str=line.strip().split(',')[0]
# 		freq:int=int(line.strip().split(',')[1])
# 		unigrams[word]=freq
# 		total+=freq
# for word in unigrams:
# 	unigrams[word]=unigrams[word]/total
# with open('./unigram_freq2.csv','w') as file:
# 	for word in unigrams:
# 		file.write(word+'\t'+str(unigrams[word])+'\n')

# Load ./words3.csv and ./unigram_freq2.csv and add a 3rd element to each line in ./word_len_freq.csv with the unigram frequency of the word, along with the word and it's length as the first 2 elements
# words:dict={}
# with open('./words3.csv','r') as file:
# 	for line in file:
# 		word:str=line.strip().split('\t')[0]
# 		length:int=int(line.strip().split('\t')[1])
# 		words[word]=length
# unigrams:dict={}
# with open('./unigram_freq2.csv','r') as file:
# 	for line in file:
# 		word:str=line.strip().split('\t')[0]
# 		freq:float=float(line.strip().split('\t')[1])
# 		unigrams[word]=freq
# with open('./word_len_freq.csv','w') as file:
# 	for word in words:
# 		if word in unigrams:
# 			file.write(word+'\t'+str(words[word])+'\t'+str(unigrams[word])+'\n')
