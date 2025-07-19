import secrets 
import random
import string 
from collections import Counter


# Using lib secret to generate a secure random password
# Password's character length can either be 12 or randomly higher (max 54).

# First, it defines how many capital letters,small letters, numbers and special characteres it will contain
# The conditions for that are:
   # 1.Symbol characteres count must be higher than 2.
   # 2.All types of characteres (besides numbers) must be used, representing the password's  total length.
   # 4.Number charactere's count can't be used more than twice, but it can be 0.

# Definition visualization (12 characteres password):
   # Examples: 5 small letters + 3 capital letters + 3 numbers + 1 symbol
   #           2 small letters + 3 capital letters + 5 numbers + 2 symbols
   #           2 small letters + 4 capital letters + 3 numbers + 3 symbols and so on ...

# Then, it uses lib 'secrets' to randomly  choose characters from the defined pools, present in "quantities" ditionary
# the condition for this is that: 3.A same individual character can't be used more than twice.




def charactere_definition():
    # Informations include: how many of each type of character will be used in the password and which pool of characters to choose from.
    # the pool of characters includes: small letters, capital letters, numbers and symbols.
    quantities = {
       'small_letters': {'count': 0, 'pool': string.ascii_lowercase + 'ç'},
       'capital_letters': {'count': 0, 'pool': string.ascii_uppercase + 'Ç'},
       'numbers': {'count': 4, 'pool': string.digits},
       'symbols': {'count': 1, 'pool': string.punctuation + '¢£§°¥©¤¶µ±'}
    } 
    password_length = secrets.choice(range(12,55))  # Randomly chooses a password length between 12 and 54

    total = 0
    # sets total = 0 to  enter the while loop


    while ((total != password_length) or (quantities['numbers']['count'] > 2) or (quantities['symbols']['count'] <= 2)): # Obey restrictions 1,2 and 4
         
      total = 0 # resets total to 0 when loop is restarted by 'continue' statement
         

      quantities['small_letters']['count'] = secrets.randbelow((password_length // 2)) + 1
      leftover = password_length - quantities['small_letters']['count']
      # Leftover can be explained as: the number of counts left, after defining the current character's count pool.
      # Ex: Password length is 12, small letters count were randomly set to 5, so leftover = 12 - 5 = 7.
      # Which means, 7 counts (spaces) are left to be claimed by the remaining pool of characters.


      if leftover <= 3: # This condition treats the variable 'leftover' and ensures that it is equal or higher than 3 for symbols (1.Symbol characteres count must be higher than 2)
         continue       # If its not, it restarts the loop and redefines the character counts.

      quantities['symbols']['count'] = secrets.randbelow(leftover) + 1
      leftover =  password_length - (quantities['small_letters']['count'] + quantities['symbols']['count'])
      # leftover Ex: Password length is 12, small letters count were randomly set to 5, symbols count were randomly set to 3, so leftover = 12 - (5 + 3) = 4.
      # Now, 4 counts (spaces) are left to be claimed by the remaining pool of characters.


      if leftover <= 1:  # This condition treats the variable 'leftover' and ensures that it is at least 1 for  capital_letters (2.All types of characteres (besides numbers) must be used, representing  the password's  total length)
         continue  # If its not, it restarts the loop and redefines the character counts.


      quantities['capital_letters']['count'] = secrets.randbelow(leftover) + 1
      leftover = password_length - (quantities['small_letters']['count'] + quantities['symbols']['count'] + quantities['capital_letters']['count'])

      if leftover > 2: # This condition treats the variable 'leftover' and ensures that it is equal or lower than 2 for numbers (3.Number charactere's count can't be used more than twice, but it can be 0)
         continue # If its not, it restarts the loop and redefines the character counts.

      quantities['numbers']['count'] = leftover # The numbers simply takes whats left from leftover, which can be 0 up to 2.


      total = sum(info['count'] for info in quantities.values()) # Calculates the total number of space used by each pool to ensure it matches the password length.(Validation on loop while)

      print('Password Length', password_length)
      print('Total:', total)
      print('Quantities:', quantities)

    return quantities



def password_generation(quantities):
    password_chars = []  # list to store each individual character that will compose the whole password
    counter = Counter()  # Counts occurrences of each character to ensure (restriction 3) a same individual character can't be used more than twice

    for info in quantities.values():
        # Checks if the count of characters is greater than 0
        if info['count'] > 0:
            #  Adds characters to the password based on the defined quantities
            for _ in range(info['count']): 
                while True:
                    char = secrets.choice(info['pool'])
                    if counter[char] < 2:  # Obeys resctricion 3 (A same individual charactere can't be used more than twice)
                        password_chars.append(char)
                        counter[char] += 1
                        break  # Sai do loop e passa para o próximo caractere

    # Shuffles characters to ensure randomness
    random.SystemRandom().shuffle(password_chars)

    print('==' * 40)
    print('Copy and paste your new password below:')
    print('==' * 40)
    return ''.join(password_chars)

print(password_generation(charactere_definition()))
print('==' * 40)
        
        





    
