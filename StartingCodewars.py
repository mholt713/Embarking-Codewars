#even/odd

def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

#convert number

def number_to_string(num):
    return str(num)

#number of vowels

def get_count(sentence):
    num_vowels = 0
    for vow in ["a", "e", "i", "o", "u"]:
        num_vowels += sentence.count(vow)
    return num_vowels
