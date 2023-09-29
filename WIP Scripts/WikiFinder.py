#import the languagemodels module
import languagemodels as lm

#use smallest model -- quicker and seems to work better for this task
lm.set_max_ram('1gb')

#user sends the message
message = input("User: ")

#extract the topic to find wiki by examples
topic = lm.chat(f'''
System: Get one keyword from the user's question and write it. Write only a single keyword.
User: Who wrote the play 'Romeo and Juliet'?
Assistant: William Shakespeare
User: When was the Declaration of Independence signed?
Assistant: Declaration of Independence                
User: What is minecraft?
Assistant: Minecraft
User: H ow many pages are on wikipedia?
Assistant: Wikipedia
User: Tell me about netflix.
Assistant: Netflix
User: What is the capital of France?
Assistant: Paris
User: {message}
Assistant:
''')

#switch to higher performing model
lm.set_max_ram('2gb')

#remove punctuation before getting wiki
topic = topic.rstrip('.')

#search for the topic on the wiki
lm.store_doc(lm.get_wiki(topic))

wikiresult = lm.get_wiki(topic)

#get a relevant snippet of the wiki
wikisnip = lm.get_doc_context(message)

#if first model failed it's task, show user the failed search, else continue as normal
if(wikiresult == "No matching wiki page found."):
    print(f'''System: Couldn't find wiki page. Searched for: "{topic}"''')
    wikisnip = "No context available"
else:
    print(f'''System: Wiki page found, searched for "{topic}"''')

#give snippet as context
response = lm.chat(f'''
System: Use this context to respond if available, if context not relevant say "Context not relevant to topic". Context: "{wikisnip}"
User: {message}
Assistant:
''')

#print the resulting reply
print("Computer: " + response)   
