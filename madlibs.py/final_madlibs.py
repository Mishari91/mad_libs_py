print("Mad Libs where libs get mad")
print("start below: \n")

time = input('Enter a number from 1 to 12:  ')

items = input('Enter a noun (plural):  ')

name = input('Enter a name:  ')

scream = input('Enter any sentence:  ')


action = input('Enter a verb:  ')

print('It was ' + time + " o'clock when i heard a knock at the door. \n"
      "I opened the door and there was a box full of " + items + ' with a note saying \"From Mr.' + name.title() + '.\"\n'
      'Just as I closed the door I heard a scream \"' + scream.upper() + '.\"\n'
      'I froze in place and all I could do was ' + action)



