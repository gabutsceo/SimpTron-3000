daEmail = "putyouremailhere@gmail.com" #put discord email here
daPassword = "putyourpasswordhere" #put discord password here
daUser = "000000000000000000" #Target UserID
#put list of compliments here
daComplimentList = ["you're so talented!","you have nice eyes","i am a better person around you", "you make me smile", "you are beautiful", 
"your laff is aamzing", "you are an attractive female", "I would like to procreate with you, as you have hips that are perfect for bearing children", "you're fun to talk to",
"will you be the crewmate to my impostor? Because I wanna eat you alive :smiling_imp:","you make me want to make you my baehan", "Ur my type", "you're cute???", "you are a gem", 
"you are an absolute masterpiece of God.", "You are absolute, astoundingly gorgeous and that's the least interesting thing about you.", "I want to suck on your toes", "You are the most gorgeous person that I have ever seen.", 
"Your hair is one of the most gorgeous that i've ever seen.", "And you smell like strawberries.", "You are always so happy and kind to people, it's like a big breath of fresh air when i walk into the street and see you!",
"I love talking to you.", "You dress in a stunning way, and you look really nice every day.", "I want to suckle the sweat from your succulent teat", "You are a real life Mona Lisa.",
"You are the breathing, talking, living equivalent of a piece of art.", "I love seeing your smile, it brightens my day every time.", 
"I wish I could make you laugh like that more often. You're beautiful all the time, but when you smile like that I swear my world stops.", "I cannot believe how incredibly smart you are.",
"You're that \"Nothing\" when people ask me what I'm thinking about.", "I like your style.", "You have the best laugh.", "I appreciate you.", "You are the most perfect there is.", "You're a great listener.", 
"How is it that you always look great, even in sweatpants", "Your smile brightens up the most gloomy day.", "These sound like greeting cards", "you always manage to find a way to make me laugh", "your empathy knows no bounds"]
daDefenseList = ["You are literally so stinky, you have no right to be talking shit please stop.", "That's an incredibly rude statement.", "Are you sure you're not looking in a mirror?", 
"no one asked", "Your mother is currently engaging in numerous sexual relationships with many individuals most of whom are not your father, and this is leading to the detriment and eventual downfall of your parents' marriage.",
"Your grandparents hate you.", "I would advise you to stop talking as I am currently engaging in repeated sexual engagements with your mother.", "Dude, you literally suck at everything please be quiet.",
"Please disengage from the conversation as you are in possession of a negative amount of braincells.", "That's really maen", "Don't talk to my friend like that", "WTF bro", "Stop talking shitter"]
daAngryResponseList = ["Omg yes pop off queen", "so true", "yes", "fax", ":100:", "yeah go off bestie you tell em"]
daSurprisedResponseList = ["Wow! That's amazing!", "Incredible!", "That's insane!", "I am surprised at this statement."]
daHappyResponseList = ["Perfect!", "Fantastic!", "This is why I'm your number one fan"]
daSadResponseList = ["Oh, that's so sad. ", "That's unfortunate, but you should know that ", "RIP\nbtw "]
daFearfulResponseList = ["It's gonna be okay, ", "It will be fine, ", "You'll get through this, "]
#Put list of channel ids
daChannelList = ["000000000000000000","000000000000000000","000000000000000000"]
msgAsReply = True
msgPingReply = False
#You don't need to change anything under this
daChannelDictionary = dict.fromkeys(daChannelList, "")
def getCreds():
    return(daEmail,daPassword)
def getResponses():
    return(daComplimentList,daDefenseList,daAngryResponseList,daHappyResponseList,daSadResponseList,daFearfulResponseList, daSurprisedResponseList)
def getScope():
    return(daUser,daChannelDictionary)
def getMisc():
    return(msgAsReply, msgPingReply)