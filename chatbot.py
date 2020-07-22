from nltk.chat.util import Chat, reflections
pairs = [
     [
        r"what is your name ?|Who are you?",
        ["My name is Stella and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"i'm doing good|fine",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"who is your fav sportsperson ?",
        ["Ben stokes, Lockie Ferguson"]
],
    [
        r"quit",
        ["Bye take care. See you soon :) "]
],
]
def Stella():
        print("Thank you,have a great day:)") #default message at the start
chat = Chat(pairs, reflections)
chat.converse()
if __name__ == "__main__":
    Stella()
