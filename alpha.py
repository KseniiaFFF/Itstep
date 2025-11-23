import random

def random_file(alphabet):

  with open('tewq.txt', 'w') as file:
    for i in range(15):
      a,b = random.choice(alphabet),random.choice(alphabet)
      z = a + b
      print(z)
      file.write(z + '\n')