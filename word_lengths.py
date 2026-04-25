#list of words
words = ["apple", "banana", "kiwi", "cherry", "mango"]

#start with an empty dictionary
word_lengths = {}

#loop through each word in the list
for word in words:
    #get the length of the current word
    length = len(word)
    
    #add the word as the 'key' and its length as the 'value'
    word_lengths[word] = length

#see the final result
print(word_lengths)