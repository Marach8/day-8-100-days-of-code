print('\033[33mWholesome Positivity Machine.\033[0m')
print()
a = input('Who are you? ')
print()
c = input('What do you want to acheive? ')
if len(a) > 2:
  print()
  b = int(input('On a scale of 1-10, How do you feel today? '))
  
  if b > 0:
    print()
    print(f'''\033[33m
Hey {a}, keep your chin up! Today, you are going to {c}! in the most amazing way. Just keep being you.
    ''')