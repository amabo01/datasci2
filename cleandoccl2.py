def clean(doc):
  cleaned_string = ""
  things_to_clean_out = ["(", ")", ",", ".", "!", "?", "\'", "/", "[", "]","*", "\""]
  for char in doc:
    if char not in things_to_clean_out:
      cleaned_string += char

  return cleaned_string

def isNumber(word):
  for char in word:
    if not char.isdigit():
      return False
  return True

def wordcount(doc):
  words = doc.lower().split(" ")
  word_dict = {}
  for word in word_dict:
    if isNumber(word):
      pass
    else: 
      if word in word_dict:
        word_dict[word] += 1
      else: 
        word_dict[word] = 1


string_input = "Emeka is my closest friend at the moment. I like talking about my relationships with him. He's a great friend overall! <3"
print(isNumber("50"))
wordcount(clean(string_input))