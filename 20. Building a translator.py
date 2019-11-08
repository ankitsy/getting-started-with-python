# We will build a translator where we will replace vowels with g
def translator(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation =  translation + letter
    return translation

print(translator('My name is Ankit!'))