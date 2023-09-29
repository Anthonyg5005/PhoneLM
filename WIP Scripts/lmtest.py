import languagemodels as lm

# Settings
lm.set_max_ram('2gb')

while True:
    message = input("User: ")
    
    # Check if the user wants to exit the conversation
    if message.lower() == "exit":
        print("Goodbye!")
        break
    
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
    Assistant: Shakespeare
    User: When was the Declaration of Independence signed?
    Assistant: Independence
    User: {message}
    Assistant:
    ''')

    print("Assistant: " + topic)
