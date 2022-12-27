import mysql.connector
import json
import channels
import test
import subscribers
import comments
import videoMetadata

#addsIngestRawPath = "/channel/video/addIngest" # POST , BODY

#categoryAddRawPath = "/user/category/addCategory" # POST, BODY

#videoChannelRawPath='/video/videoChannel' # POST, BODY

testFunctionRawPath="/user/test" #GET, BODY

channelAddRawPath = "/user/{userId}/channels/addChannel" #POST, BODY
channelsViewRawPath = "/user/{userId}/channels" #GET, BODY
channelSearchRawPath = "/user/{userId}/channels/{searchItem}" #GET, BODY
updateChannelRawPath = "/user/{userId}/channels/updateChannel/{channelId}" #Patch, BODY
deleteChannelRawPath = "/user/{userId}/channels/deleteChannel/{channelId}" #DELETE, BODY


dbLogin={}

with open("creds.json", "r") as creds:
    dbLogin = json.load(creds)

def lambda_handler(event, context):
    print(event)
    print("something")
    event['rawPath']=event['resource']
    
    #print (event['rawPath'])
    
    
    connection = mysql.connector.connect(user=dbLogin['user_name'],
                                        password=dbLogin['password'],
                                        host=dbLogin['host'],
                                        port=dbLogin['port'],
                                        database=dbLogin['db_name']);
                                        
    if event['rawPath'] == testFunctionRawPath:
        print("Test success")
        return test.testFunction(connection)
        
        
    if event['rawPath'] == channelAddRawPath:
        print("Channel success")
        userId = event['pathParameters']['userId']
        
        decodedBody = json.loads(event['body'])
        return channels.channelAdd(userId,decodedBody,connection)
        
    if event['rawPath'] == channelsViewRawPath:
        print("Channels view success")
        userId = event['pathParameters']['userId']
        return channels.viewChannels(userId,connection)
        
    if event['rawPath'] == channelSearchRawPath:
        print("Channel view success")
        userId = event['pathParameters']['userId']
        searchItem = event['pathParameters']['searchItem']
        return channels.searchChannel(userId,searchItem,connection)
        
    if event['rawPath'] == updateChannelRawPath:
        print("Channel success")
        userId = event['pathParameters']['userId']
        channelId = event['pathParameters']['channelId']
        decodedBody = json.loads(event['body'])
        return channels.updateChannel(userId,channelId,decodedBody,connection)
        
    if event['rawPath'] == deleteChannelRawPath:
        print("Channel success")
        userId = event['pathParameters']['userId']
        channelId = event['pathParameters']['channelId']
        return channels.deleteChannel(userId,channelId,connection)
            
    
    
    
                                 

        
        

        
    
    
