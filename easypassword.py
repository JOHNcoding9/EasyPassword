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
   # 4.Number charactere's count must be between 0 and 2.

# Definition visualization (12 characteres password):
   # Examples: 5 small letters + 3 capital letters + 3 numbers + 1 symbol
   #           2 small letters + 3 capital letters + 5 numbers + 2 symbols
   #           2 small letters + 4 capital letters + 3 numbers + 3 symbols and so on ...

# Then, it uses lib 'secrets' to randomly  choose characters from the defined pools, present in "quantities" ditionary
# the condition for this is that: 3.A same individual character can't be used more than twice.




def character_definition(verbose: bool = True):
    """  Defines the quantitites of space allocated for each pool of characters in the password.

     Rules/Restrictions :
        1. Symbol characters count must be at least 3.
        2. All character types (except numbers) must appear at least once.
        3. Numbers can appear 0, 1, or 2 times (randomly chosen).


    Initial character counts are defined as:
        - 'small_letters': at least 1 character (includes 'ç')
        - 'capital_letters': at least 1 character (includes 'Ç')
        - 'symbols': minimum of 3 characters (includes currency and accented symbols)
        - 'numbers': randomly 0 to 2 characters

    Remaining characters (leftover space) are distributed among:
        - small_letters
        - capital_letters
        - symbols
      Numbers are excluded from redistribution.


    Returns:

        dict: A dictionary "quantities" with the structure:
            {
                'small_letters': {'count': int, 'pool': str},
                'capital_letters': {'count': int, 'pool': str},
                'numbers': {'count': int, 'pool': str},
                'symbols': {'count': int, 'pool': str}
            }

        Each 'count' defines how many characters of that type will be in the password.
        Each 'pool' defines the set of characters that can be randomly selected for that type.


    Example:
        >>> q = charactere_definition()
        Password length: 21
        Quantities: {'small_letters': 6, 'capital_letters': 5, 'numbers': 2, 'symbols': 8}
        >>> isinstance(q, dict)
        True
        >>> all(k in q for k in ['small_letters', 'capital_letters', 'numbers', 'symbols'])
        True
        >>> sum(v['count'] for v in q.values()) >= 12
        True """

    quantities = {
       'small_letters': {'count': 1, 'pool': string.ascii_lowercase + 'ç'}, 
       'capital_letters': {'count': 1, 'pool': string.ascii_uppercase + 'Ç'},
       'numbers': {'count': secrets.choice([0, 1, 2]), 'pool': string.digits}, 
       'symbols': {'count': 3, 'pool': string.punctuation + '¢£§°¥©¤¶µ±'} 
    } 

    password_length = secrets.choice(range(12,55))  # Randomly chooses a password length between 12 and 54

    allocated = sum(q['count'] for q in quantities.values()) # Allocated  sums the minimum counts of each pool
    leftover = password_length - allocated # Leftover is what is left to be allocated after the minimum counts are set

    # Distributes the leftover space among the types of characters that can be used more than once.
    # (Numbers  were already defined to be 0, 1 or 2, so they won't be used here)
    distribution = ['small_letters', 'capital_letters', 'symbols']
    while leftover > 0:
        chosen_type = secrets.choice(distribution)
        quantities[chosen_type]['count'] += 1
        leftover -= 1

    if verbose:
      print(f"Password length: {password_length}")
      print("Quantities:", {k: v['count'] for k, v in quantities.items()}) 

    return quantities



def password_generation(quantities: dict, verbose: bool = True, max_repeat: int = 2):
    
    """
    Generates a secure password based on specified quantities for each character type.

    Rules enforced:
        - Each character is selected from its associated pool.
        - A character cannot appear more than `max_repeat` times.
        - The total password length is the sum of all counts from the input dictionary.

    Parameters:
        quantities (dict): Dictionary with keys like 'small_letters', each containing:
            - 'count': number of characters to use
            - 'pool' : string of valid characters to choose from
        max_repeat (int, optional): Maximum number of times a single character may appear. Default is 2.
        verbose (bool, optional): If True, prints output formatting for password display.

    Returns:
        str: The generated password string.

    Example:
        >>> q = charactere_definition()
        >>> pwd = password_generation(q)
        >>> len(pwd) == sum(v['count'] for v in q.values())
        True
    """
    
    # Dictionary error handling
    required_keys = {'small_letters', 'capital_letters', 'numbers', 'symbols'}
    if not required_keys.issubset(quantities):
        raise ValueError("Missing required character pools in input dictionary.")
    

    password_chars = []  # list to store each individual character that will compose the whole password
    counter = Counter()  # Counts occurrences of each character to ensure (restriction 3) a same individual character can't be used more than twice

    for info in quantities.values():
        # Checks if the count of characters is greater than 0
        if info['count'] > 0:
            #  Adds characters to the password based on the defined quantities
            for _ in range(info['count']): 
                while True:
                    char = secrets.choice(info['pool'])
                    if counter[char] < max_repeat:  # Obeys resctricion 3 (A same individual charactere can't be used more than twice)
                        password_chars.append(char)
                        counter[char] += 1
                        break  # Exit loop and moves on to next character

    # Shuffles characters to ensure randomness
    random.SystemRandom().shuffle(password_chars)

    if verbose:
        print('==' * 40)
        print('Copy and paste your new password below:')
        print('==' * 40)

    return ''.join(password_chars) #Joins the characters into a single string to form the final password

print(password_generation(character_definition()))

        
        





    
