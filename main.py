import words
from hagman import logo
from hagman import stages

import random


print(logo)
for i in range(0,1):
  EscolherPalavraIndex = random.randint(0,len(words.word_list)-1)
  Palavra = words.word_list[EscolherPalavraIndex]
  
  conjuntoLetras = []
  Palabras = []
  PalavraHangman = []

  for letras in Palavra:
    conjuntoLetras.append(letras)
    for mod in letras:
      x = letras.replace(mod, '_')
      PalavraHangman.append(x)

  print('Bem vindo ao HANGMAN.')
  print(f'Sua palavra possui {len(Palavra)} letras.')
  print(Palavra)

  print(PalavraHangman)

  count = 0
  while True:
    chute = str(input('Chute uma letra: '))

    if count == -6:
      print(stages[-1+count])
      print('EndGame')
      break

    elif chute in Palavra:
      indexecao = [i for i, item in enumerate(conjuntoLetras) if item == chute]
      for x in indexecao:
        Letra = conjuntoLetras[x]
        PalavraHangman[x] = Letra
      print(PalavraHangman)

    elif chute not in Palavra:
      print(stages[-1+count])
      count-=1
      print(PalavraHangman)
    


    
    






