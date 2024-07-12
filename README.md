# Eminent Encryption

## Description

A program to demonstrate simple encryption and cryptanalysis techniques.

```diff
- The ./decode.py program currently does not classify words as nouns, verbs, etc., so that the output can be narrowed down and improved even more since english has conventions such as an adjective often being before a noun.
```

## Files

- `./encode.py` is used to encode an input message.
- `./decode.py` is used to decode an encoded message.
- `./preprocess.py` is used to make the `./word_len_freq.csv` file from the `./words.csv` and `./unigram_freq.csv` files.

## Usage

```sh
python ./preprocess.py
python ./encode.py <message>
python ./decode.py <encoded_message>
```

## Explanation

### Encode.py

- The message is encoded using a ceasar cipher with a random shift value from 0-25 (26 letters in the alphabet).
- Then each character in the message is replaced with its ascii value's binary representation.
- The binary values are then shifted about in their corresponding word and separated by a pipe (`|`) with a space to separate the words of the input message.

> Example:

```sh
python ./encode.py "test" # 01110011|01110011|01110010|01100100
```

```py
# Returns a list of ascii values from a string.
def get_ascii(message:str,shift:int=0)->list:
	return [ord(c)-shift for c in message]
# Returns a binary representation of an integer.
def get_binary(num:int)->str:
	return bin(num)[2:].zfill(8)
# In this case, the shift value is 1.
shift:int=1
# The shuffling is random, but this output will show how the encoded message looks before being shuffled.
print('|'.join([get_binary(i) for i in get_ascii("test",shift)])) # 01110011|01100100|01110010|01110011
# Since that output is before any shuffling, we'll define it as a linear list, such as: [1,2,3,4].
# 01110011|01100100|01110010|01110011 (before shuffling) vs 01110011|01110011|01110010|01100100 (after shuffling).
# We can tell that the new message is a permutation of the old one with the new order: [1,4,3,2].
```

## Decode.py

- Loop through every possible shift value from 0-25.
- Output any possible words that could be made using the shuffled message with the reversed ceasar cipher (using the current shift iteration). This is done by comparing the letters in each word to the words in the English language (`./word_len_freq.csv`).
- Order the words by most likely to be correct (most frequently used words).

> Example:

```sh
python ./decode.py "01110011|01110011|01110010|01100100"
```

will output

```
ssrd
----
ssrd (-0)		sdrs
ttse (-1)		test|sett|stet
ddco (-11)		codd
eedp (-12)		deep|peed|pede|depe
oonz (-22)		zoon
```

where the output is formatted as:

```
<shuffled word with no shifts>
<dashed line>
<shuffled word with opposite shift> (-<shift>)		<possible words that can be made by shuffling the letters in the word>
...
```

> How to read the output?

The output is most likely one of the green colored words on one of the lines (could be multiple green colored words per line if the given message has multiple words) as the green indicates that the word is more commonly used in the English language compared to the other possible words.
