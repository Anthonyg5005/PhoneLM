#import the languagemodels module
import languagemodels as lm

#module settings
lm.set_max_ram('2gb')

#variables
message = input("User: ")

#print the resulting response
print("Phone: " + lm.do(message))