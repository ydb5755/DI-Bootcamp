
# Instructions :
# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.
import translate
translator = translate.Translator(to_lang="en", from_lang='fr')
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
result = {}
for word in french_words:
    result[word] = translator.translate(word)
print(result)