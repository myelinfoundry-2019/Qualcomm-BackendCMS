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

channelAddRawPath = "/user/{userId}/channel/addChannel" #POST, BODY




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
            
    
    
    
                                 

        
        

        
    
    
