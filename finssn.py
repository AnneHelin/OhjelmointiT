# CHECK ROUTINES FOR FINNISH SOCIAL SECURITY NUMBER

# LIBRARIES AND MODULES

# FUNCTIONS 

def centuryCode(ssnumber):
    """Extracts the century of birth from
    finnish social security number

    Args:
        ssnumber (string): a social security number

    Returns:
        int: century 1800, 1900 or 2000 
    """
    cCode = ssnumber[6]
    codeDict = {'+' : 1800, '-' : 1900, 'A' : 2000}
    century = codeDict[cCode]
    return century

if __name__ == "__main":
    ssnumber = '121138-555J'
    print('syntymävuosisata', centuryCode(ssnumber))    
