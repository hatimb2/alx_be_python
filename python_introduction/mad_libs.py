print('Lets create a Mad Libs story!')
adjective1 = input('Enter an adjective: ')
adjective2 = input('Enter another adjective: ')
adjective3 = input('Enter one more adjective: ')
adjective4 = input('Final adjective: ')

if len (adjective1) <= 5:
    print(f"On a beautiful {adjective1} day, I went to the zoo.")
else:
   print(f"On a nice {adjective1} and day, I went to the zoo.")
  
  
print(f"I saw a funny {adjective2} monkey swinging from the trees.")
print(f"Then, I spotted a majestic {adjective3} lion lounging in the sun.")
print (f" What a wild and {adjective4} experience!")
