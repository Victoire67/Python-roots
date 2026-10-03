input = '()[]{}'

valid_matches = set(["()", "{}", "[]"])


def isValid(s: str) -> bool:

    # we check if there is any valid match .
    # We remove the valid match until we can't find any which means we return FALSE ,
    # or we reach to a point where there is nothing inside the array .

    #    The while loop should run as long as :
    #    1. There is a character inside the string which matches something inside the valid_matches
    #    2. The string is not empty 

    while(len(s) > 0 and any(char in valid_matches in s)) : 

        # get the match 
        

    return True


isValid(input)


# Are all opened closed ?
#
