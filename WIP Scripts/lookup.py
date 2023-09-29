import languagemodels as lm

message = input("message: ")

topic = input("wiki: ")

#search for the topic on the wiki
lm.store_doc(lm.get_wiki(topic))

wikiresult = lm.get_wiki(topic)

#get a relevant snippet of the wiki
wikisnip = lm.get_doc_context(message)

#if first model failed it's task, show user the failed search, else continue as normal
if(wikiresult == "No matching wiki page found."):
    print(f'''System: Couldn't find wiki page. Searched for: "{topic}"''')
    wikisnip = "No context available"

print(wikisnip)
