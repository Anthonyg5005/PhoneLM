#import the languagemodels and time modules
import languagemodels as lm
import time

#use high quality model
lm.set_max_ram('2gb')

#get the current time zone
zone = time.tzname[0]

#check for daylight savings
if(time.localtime().tm_isdst == 1):
    daylightsavings = "Daylight Savings is in effect."
else:
    daylightsavings = "Daylight Savings is not in effect."

#user message to the chatbot
message = input("User: ")

#get the current time and date
dateaandtime = lm.get_date()

#system message to introduce the chatbot. Base taken from https://github.com/oobabooga/text-generation-webui/blob/f2d82f731a3e74c7aa2f284c469170fa60028348/instruction-templates/Guanaco.yaml#L4
response = lm.chat(f'''
        System: A chat between a curious user and an intelligence phone assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. Limited to only one interaction, resulting in no memory of any previous interations due to limited resources on a phone. It is currently {dateaandtime} {zone}.{daylightsavings} 
        User: {message}
        Assistant:
''')

#print the response
print("Computer: " + response)