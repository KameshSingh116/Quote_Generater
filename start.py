#Radhe Radhe Hare Krishn
import random

choice='y'
while(choice=='y'):
    quote=["Love is the bridge between you and everything.",
           "The more love you give, the more your spirit glows.",
           "Your task is not to seek for love, but merely to seek and find all the barriers within yourself that you have built against it.",
           "When the soul lies down in that grass, the world is too full to talk about. Ideas, language, even the phrase each other doesn't make any sense.",
           "To love another person is to see the face of God.",
           "Love and compassion are necessities, not luxuries. Without them, humanity cannot survive.",
           "True love is born from understanding.",
           "Love is the purest form of a soul at peace.",
           "The spiritual journey is the unlearning of fear and the acceptance of love.",
           "Let yourself be silently drawn by the strange pull of what you really love. It will not lead you astray."
           ]
    
    out=random.choice(quote)
    print(out)

    choice=input("Do you want to generate another quote ?:(y/n):")
    if(choice=='y'):
        continue
    else:
        break


#Project complete
#Radhe Radhe