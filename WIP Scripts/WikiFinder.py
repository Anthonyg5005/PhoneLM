import languagemodels as lm

#settings
lm.set_max_ram('2gb')

message = input("User: ")

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

topic = topic.rstrip('.')

lm.store_doc(lm.get_wiki(topic))

wikisnip = lm.get_doc_context(message)

print("Bot: " + wikisnip)
