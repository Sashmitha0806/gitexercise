sentence =input("Enter the sentence :")
sentence_=sentence.lower()
print(sentence_)
vowels=("aeiou")
vowels_count=0
consonants_count=0
for x in sentence_:
    if x.isalpha():
        if x in vowels:
            vowels_count+=1
        else:
            consonants_count+=1

print(f" No. of vowels is {vowels_count}")
print(f" No. of consonants is {consonants_count}")
    
