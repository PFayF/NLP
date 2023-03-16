"Given code part 1"
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""Cat and monkey seem to be similar because they are both animals;
Monkey and banana have a higher similarity than cat and
banana.
"""

"Given code part 2 - my own example"
print("My example with dog, bird and bone")
word1 = nlp("dog")
word2 = nlp("bird")
word3 = nlp("bone")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""dog and bird seem to be similar because they are both animals;
Dog and bone have a higher similarity than bird and
bone.
"""

# Working with vectors

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Working with sentences

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""After trying the exact same code in the example file with 
en_core_web_sm, we find that the more advanced language model
'en_core_web_md' is able to find similarities and differences more accurately
 than the original language model 'en_core_web_sm' and also without warnings.
The strength of the similarity increases all the way up to 1 
when two words are exactly similar. 
The ouputs are saved in a file called output.txt.
"""
 
