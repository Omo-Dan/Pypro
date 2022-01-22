#Madlibs random story generator
from random import randint
import copy

story =(
    "One day my {} friend and I decided to go to the {} game in {}. " + 
    "We realy wanted to see the {} and play {}." +
    "So, we {} our {} down to the {} and bought some {}s " +
    "We got into the game and it was a lot fun.  " +
    "We ate some {} {} and drank some. " +
    "we had some great time! and we plan to go ahead next year!"
)

#create a dictionary to look up words by type
word_dict = {
    'adjective':['greed', 'abrasive', 'grubby', 'rich','harsh', 'tasty'],
    'city name':['Chicago', 'New York', 'Charlotte','Indianapolis'],
    'noun':['people','map','music','dog','salad','hotdog', 'ball', 'hamster'],
    'action verb':['run', 'fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    'sports noun':['ball', 'mit', 'puck', 'uniform','helmet','player'],
    'place':['park','desert', 'forest','store','restoraunt','waterfall']
}

#Function for selecting words from dictionary randomly
def get_word(type, local_dict):
    words=local_dict[type]
    cnt=len(words)-1
    index=randint(0,cnt)
    return local_dict[type].pop(index)
#Function for  story
def create_story():
    local_dict=copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective',local_dict),
        get_word('sports noun',local_dict),
        get_word('city name',local_dict),
        get_word('noun',local_dict),
        get_word('noun',local_dict),
        get_word('action verb',local_dict),
        get_word('noun',local_dict),
        get_word('place',local_dict),
        get_word('noun',local_dict),
        get_word('adjective',local_dict),
        get_word('noun',local_dict),
        get_word('adjective',local_dict),
        get_word('noun',local_dict),
    )

print("Story 1: ")
print(create_story())
print()
print("Story 2: ")
print(create_story())