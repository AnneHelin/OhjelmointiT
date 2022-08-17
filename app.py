# HENKILÖTIETOJEN KYSELY JA TARKISTUS
#--------------------------------------

# KIRJASTOJEN JA MODUULIEN LATAUKSET

# LUOKKAMÄÄRITYKSET

class Person:
    """Properties of a client and a method
    for cheking the finnish social security number """
    def __init__(self, firstName, lastName, ssNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.ssNumber = ssNumber

# MAIN LOOP

# Ask for user input and store answers to variables
giveName = input('Mikä on etunimesi?')
surname = input('Mikä on sukunimesi?')
ssn = input('Syötä henkitunnuksesi:')

# Create an object from Person class

person1 = Person(giveName, surname, ssn)

print('Etunimesi on', person1.firstName, 'ja henkilötunnuksesi', person1.ssNumber)