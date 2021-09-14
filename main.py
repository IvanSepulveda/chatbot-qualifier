import random

name = input("Welcome to the chatbot. Please enter your name: ")

goodmoods = ["good", 'happy', 'great', 'well']
badmoods = ['poor', 'sad', 'bad']

mood = input("Hello, " + name + ". How is your day?").lower()

moodlist = mood.split()

usermood = ''


for m in moodlist:
    if m in goodmoods:
        if moodlist[moodlist.index(m)-1] == 'not':
            usermood = 'bad'
        else:
            usermood = 'good'
    elif m in badmoods:
        if moodlist[moodlist.index(m)-1] == 'not':
            usermood = 'good'
        else:
            usermood = 'bad'

if usermood == 'good':
    print("glad to see you doing good")
elif usermood == 'bad':
    print('I hope your day gets better')
else:
    print("glad to hear from you")

while True:
    print("Trivia")
    print("Joke")
    print("Fun Fact")
    selectedgame = input("Select a game from one of these 3")
    if selectedgame.lower() == "trivia":
        questionbank = ['What does “www” stand for in a website browser?', 'How long is an Olympic swimming pool (in meters)?']
        answerbank = ['world wide web', '50']
        question = random.choice(questionbank)
        answer = input(question).lower()
        if answer in answerbank:
            input('congrats on getting it right! enter anything to continue')
        else:
            input('wow you got it wrong? just enter anything to continue')
    if selectedgame.lower() == "joke":
        jokebank = ['why did the chicken cross the road?', 'what do you call a red fruit?']
        jokeanswers = ['to get to the other side', 'an apple']

        joke = random.choice(jokebank)
        index = jokebank.index(joke)
        answer = jokeanswers[index]
        input(joke)
        input(answer)
    if selectedgame.lower() == "fun fact":
        factbank = ["Land snails have two sets of tentacles that stick out, the longer set of tentacles are the ones that have the snail's eyes. This way they can move their tentacles around to get the best view. Water snails, on the other hand, have eyes at the tentacles' base and they have only one pair of tentacles."]
        input(random.choice(factbank))
        input("did you think that fact was fun?")
        input("glad to hear your feedback!")
    else: 
        print("")