def countPassword(password):  
    lowercase = 0
    uppercase = 0
    digit = 0
    noOfPassword = 0
    for x in password:
        if(x>='0' and x<='9'):
            digit = digit + 1
        if (x>='a' and x<='z'):
            lowercase = lowercase +  1
        if (x>='A' and x<='Z'):
            uppercase = uppercase + 1

        if (lowercase >=1 and uppercase >=1 and digit>=1):
            noOfPassword = noOfPassword + 1
            lowercase = 0
            uppercase = 0
            digit = 0
        else: continue
    return noOfPassword

import sys
for line in sys.stdin:
    print(countPassword(line.strip()))