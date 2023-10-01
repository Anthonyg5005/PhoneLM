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

#system message to introduce the chatbot. Taken from https://github.com/oobabooga/text-generation-webui/blob/f2d82f731a3e74c7aa2f284c469170fa60028348/instruction-templates/Guanaco.yaml#L4
response = lm.chat(f'''
        System: A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. Limited to only 3 interactions. Currently {dateaandtime} {zone}.{daylightsavings} 
        User: Hello, I am a curious user. I would like to know more about you.
        Assistant: I am an artificial intelligence assistant. I am here to provide detailed information about various topics. I can answer questions, provide definitions, and give examples. A downside is that I am limited to only a single interaction.
        User: What is a tree?
        Assistant: A tree is a woody perennial plant that typically has a single main stem or trunk, which supports branches and leaves above the ground. Trees are an essential part of the plant kingdom and come in various shapes, sizes, and species, with diverse characteristics and adaptations to different environments.
        User: {message}
        Assistant:
''')

#print the response
print("Computer: " + response)