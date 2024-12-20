def capitalize_words(input_string):
    result = ' '.join(word.capitalize() for word in input_string.split())
    return result

print(capitalize_words("hi"))  
print(capitalize_words("i love programming")) 
