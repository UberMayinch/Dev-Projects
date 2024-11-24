import pandas as pd
import numpy as np
import pprint

df = pd.read_csv("wordlist.csv") 
df = df.drop(columns=['day'])

print(df)

# word_list = [] 

# word = np.random.choice(word_list)

# attempts = 5
# won = False

# while attempts:
#     guess = input()
#     if(len(guess) != 5):
#         print("Guess 5 letter word")
#     else:
#         pprint()

#     if won: 
#         break
    
#     else:
#         attempts -=1

# if won == False:
#     print(f"The word was {word}")




