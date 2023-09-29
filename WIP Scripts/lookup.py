import languagemodels as lm
message = input("message: ")
topic = input("wiki: ")
lm.store_doc(lm.get_wiki(topic))
wikiresult = lm.get_wiki(topic)
wikisnip = lm.get_doc_context(message)
if(wikiresult == "No matching wiki page found."):
    print(f'''System: Couldn't find wiki page. Searched for: "{topic}"''')
    wikisnip = "No context available"
print(wikisnip)
