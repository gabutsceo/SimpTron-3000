import http.client
import json,time
import random
import text2emotion as te
from config import getCreds, getResponses, getScope, getMisc

conn = http.client.HTTPSConnection("discord.com")
username,password = getCreds()
payload = "{\"login\":\""+username+"\",\"password\":\""+password+"\"}"
daComplimentList,daDefenseList,daAngryResponseList,daHappyResponseList,daSadResponseList,daFearfulResponseList, daSurprisedResponseList = getResponses()

headers = {
    'cookie': "__cfduid=d34b9649242049e3c95e9737b41c2bf4d1619142338; __dcfduid=327cde81d8964a30887a3d3d92b55dbf",
    'Content-Type': "application/json"
    }

conn.request("POST", "/api/v9/auth/login", payload, headers)

res = conn.getresponse()
data = res.read()

daToken = json.loads(data.decode("utf-8"))["token"]
daCount = 0
reactTo,channelIDtoMsg,daGuildID = getScope()
msgAsReply,msgPingReply = getMisc()

def createCompliment(emotions):
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
    elif daEmotion == "Angry":
        daMessage += daAngryResponseList[random.randint(0,len(daAngryResponseList))-1]
    elif daEmotion == "Surprise":
        daMessage += daSurprisedResponseList[random.randint(0,len(daSurprisedResponseList))-1]
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
    for channelID in list(channelIDtoMsg.keys()):
        conn = http.client.HTTPSConnection("discord.com")
        payload = ""

        headers = {
        'cookie': "__cfduid=d34b9649242049e3c95e9737b41c2bf4d1619142338; __dcfduid=327cde81d8964a30887a3d3d92b55dbf",
        'authorization': daToken,
        'Content-Type': "application/json"
        }
        
        conn.request("GET", "/api/v9/channels/"+channelID+"/messages", payload, headers)
        
        res = conn.getresponse()
        data = res.read()
        if json.loads(data.decode("utf-8"))[0] == channelIDtoMsg[channelID]:
            daMessageID = json.loads(data.decode("utf-8"))[0]["id"]
            daMessageText = json.loads(data.decode("utf-8"))[0]["content"]
            print(json.loads(data.decode("utf-8"))[0])
            channelIDtoMsg[channelID] = json.loads(data.decode("utf-8"))[0]
            if channelIDtoMsg[channelID]["author"]["id"] != reactTo:
                print(daMessageText)
                print(te.get_emotion(daMessageText))
                daEmotionParam = te.get_emotion(daMessageText)
                if msgAsReply == True:
                    payload = "{\"content\": \""+createCompliment(daEmotionParam)+"\",\n\"nonce\": "+str(daCount)+",\n\"tts\": false,\n\"message_reference\": {\"channel_id\": \""+str(channelID)+"\",\n\"guild_id\":\""+str(daGuildID)+"\", \n \"message_id\": \""+str(daMessageID)+"\"},\n"
                    if msgPingReply == False:
                        payload += "allowed_mentions: {parse: [\"users\", \"roles\", \"everyone\"], \n replied_user: false}"
                    payload += "}"
                else:
                    payload = "{\"content\": \""+createCompliment(daEmotionParam)+"\",\n\"nonce\": "+str(daCount)+",\n\"tts\": false}"
                print("Payload:"+payload)
                conn.request("POST", "/api/v9/channels/"+channelID+"/messages", payload, headers)
                daCount += 1
    time.sleep(.25)