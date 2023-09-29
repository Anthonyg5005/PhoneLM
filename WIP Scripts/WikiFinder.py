import languagemodels as lm

#use smallest model
lm.set_max_ram('1gb')

#user sends the message
message = input("User: ")

#extract the topic to find wiki
topic = lm.chat(f'''
System: Get one keyword from the user's question and write it. Write only a single word and don't include punctuation like periods.
User: What is minecraft?
Assistant: Minecraft
User: What is a well known social media site?
Assistant: Twitter
User: Tell me about netflix.
Assistant: Netflix
User: What is the capital of France?
Assistant: Paris
User: Who wrote the play 'Romeo and Juliet'?
Assistant: William Shakespeare
User: When was the Declaration of Independence signed?
Assistant: Declaration of Independence
User: {message}
Assistant:
''')

#switch to higher performing model
lm.set_max_ram('2gb')

#remove punctuation before getting wiki
topic = topic.rstrip('.')

#lookup topic on wiki and get a snippet
lm.store_doc(lm.get_wiki(topic))
wikisnip = lm.get_doc_context(message)

#give snippet as context
response = lm.chat(f'''
System: Use this context to respond, "{wikisnip}"
User: {message}
Assistant:
''')

#print the resulting reply
print("Bot: " + response)
