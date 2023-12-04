# PhoneLM
## Running language models on a phone

This is the example code for running a powerful (*as much as a 2019 phone can handle*) language model on my Google Pixel 4 using the `languagemodels` python module. You can find the module on [GitHub](https://github.com/jncraton/languagemodels).

## How it works

I run this using [Termux](https://termux.dev/en/) on Ubuntu version 22.04 from [Andronix](https://andronix.app/).\
I used the 1 and 2 GB RAM models for this project as the phone only has [6GB of available memory](https://en.m.wikipedia.org/wiki/Pixel_4) and the next highest model is 4GB which did work, but it was slow and eventually crashed termux after finishing.

I don't believe you need to have a rooted device for any of this, but I will say my phone is running rooted Pixel OS.

To run this you just need to pip install -r requirements.txt and then run either of the two python files in working scripts. Normal is a more simple one and just gets real time info about the date and time. Wikipedia version is a bit more complicated and it first looks for a topic in the user's question, then it'll search that topic and if it exists as a wiki page then it'll get a relevant snippet as context to then respond to the original question

Wouldn't be possible, or at least this easy, without [languagemodels](https://github.com/jncraton/languagemodels) and its dependencies. (First one if counting my programming knowledge.)
