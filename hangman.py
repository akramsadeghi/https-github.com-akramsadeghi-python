import random

words = ['shirmoz', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'book']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock
joon = 10

while joon > 0:
    print('- ' * len(word)) # - - - - -

    user_character1 = input() # s
    user_character=user_character1.lower()

    if user_character in word:
        
        print('yes')
        break
    else:
        joon = joon - 1
        print('no')    
        
        
if joon==10:
    print("*شما با اولین حدس برنده شدید*")
            
print (joon)