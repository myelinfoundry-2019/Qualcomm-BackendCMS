import json
import channels
import follow
import comments
import video_metadata
import mysql.connector
#addsIngestRawPath = "/channel/video/addIngest" # POST , BODY

#categoryAddRawPath = "/user/category/addCategory" # POST, BODY

channelAddRawPath = "/user/channel/addChannel" #POST, BODY

addCommentRawPath = "/user/comment/addComment" #POST, BODY

dbLogin={}

with open("creds.json", "r") as creds:
    dbLogin = json.load(creds)

def lambda_handler(event, context):
    
    print (event['rawPath'])
    
    print (event)
    
    connection = mysql.connector.connect(user=dbLogin['user_name'],
                                        password=dbLogin['password'],
                                        host=dbLogin['host'],
                                        port=dbLogin['port'],
                                        database=dbLogin['db_name'])

    if event['rawPath'] == channelAddRawPath:
        decodedBody = json.loads(event['body'])
        return channels.channelAdd(decodedBody,connection)
    
    if event['rawPath'] == addCommentRawPath:
         decodedBody = json.loads(event['body'])
    return comments.commentAdd(decodedBody,connection)
    
    
    