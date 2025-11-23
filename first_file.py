from alpha import random_file
from clam import clam_word
from check import check_word

alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z',
            'x','c','v','b','n','m']

random_file(alphabet)

x = [] 

while True:
  user = input('? or 0 for stop: ') 

  if not user.isdigit():
      print('error')
      continue
  if user == '0':
    break

  x.append(int(user)) 

result = clam_word(x)
check_word(result)
if check_word(result) == False:
   print(result)