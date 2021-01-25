def int_func(user_inp):
  user_inp = ' '.join(word[0].upper() + word[1:] for word in user_inp.split())
  return user_inp
  
  
print(int_func(input('Введите одно или несколько слов строчными буквами: ')))
