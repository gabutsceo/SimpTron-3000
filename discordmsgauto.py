import json,time
import random
import text2emotion as te
from config import getResponses, getScope, getMisc
import discAutoMsg.discord_automessage as discAutoMsg

daComplimentList,daDefenseList,daAngryResponseList,daHappyResponseList,daSadResponseList,daFearfulResponseList, daSurprisedResponseList = getResponses()


reactTo,channelIDtoMsg,daGuildID = getScope()
msgAsReply,msgPingReply = getMisc()

def createCompliment(emotions):
    print("Creating Compliment")
    highest = 0.0
    daEmotion = ""
    daMessage = ""
    for emotion in emotions:
        if emotions[emotion] > highest:
            print(emotions[emotion])
            highest = emotions[emotion]
            daEmotion = emotion
    print(daEmotion)
    daMessage = ""
    if daEmotion == "Happy":
        daMessage += daHappyResponseList[random.randint(0,len(daHappyResponseList))-1]
        daMessage += daComplimentList[random.randint(0,len(daComplimentList))-1]
    elif daEmotion == "Angry":
        daMessage += daAngryResponseList[random.randint(0,len(daAngryResponseList))-1]
        daMessage += daComplimentList[random.randint(0,len(daComplimentList))-1]
    elif daEmotion == "Surprise":
        daMessage += daSurprisedResponseList[random.randint(0,len(daSurprisedResponseList))-1]
        daMessage += daComplimentList[random.randint(0,len(daComplimentList))-1]
    elif daEmotion == "Sad":
        daMessage += daSadResponseList[random.randint(0,len(daSadResponseList))-1]
        daMessage += daComplimentList[random.randint(0,len(daComplimentList))-1]
    elif daEmotion == "Fear":
        daMessage += daFearfulResponseList[random.randint(0,len(daFearfulResponseList))-1]
        daMessage += daComplimentList[random.randint(0,len(daComplimentList))-1]
    elif daEmotion == "":
        daMessage += daComplimentList[random.randint(0,len(daComplimentList))-1]
    return daMessage

while True:
    # print("Start of Loop")
    for channelID in list(channelIDtoMsg.keys()):
        #print("Start of for loop")
        daRecentMessage = discAutoMsg.getMessages(channelID,1)[0]
        if daRecentMessage != channelIDtoMsg[channelID]:
            daMessageID = daRecentMessage["id"]
            daMessageText = daRecentMessage["content"]
            print(daRecentMessage)
            channelIDtoMsg[channelID] = daRecentMessage
            if channelIDtoMsg[channelID]["author"]["id"] == reactTo:
                print(daMessageText)
                print(te.get_emotion(daMessageText))
                daEmotionParam = te.get_emotion(daMessageText)
                if msgAsReply == False:
                    discAutoMsg.sendMessage(channelID, createCompliment(daEmotionParam))
                else:
                    discAutoMsg.sendReply(channelID, createCompliment(daEmotionParam),daMessageID)
    time.sleep(.25)