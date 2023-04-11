sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
print(sentence, "\n")

sentence_list = list(map(str,sentence.split(' '))) 
print(sentence_list , '\n')

sentence_set=set(sentence_list)
print(sentence_set, '\n')

num=len(sentence_set)
print(num,'\n')