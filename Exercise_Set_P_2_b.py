'''(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
'''
word=input()
n=30
word_list=word.split()[:n]
output=" ".join(word_list)
print(output)