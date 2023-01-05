import json
import channels
import subscribers
import comments
import video_metadata
import mysql.connector
#addsIngestRawPath = "/channel/video/addIngest" # POST , BODY

#categoryAddRawPath = "/user/category/addCategory" # POST, BODY

channelAddRawPath = "/user/channel/addChannel"

addCommentRawPath = "/user/comment/addComment"



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
    
    if event['rawPath'] == addCommentRawPath:
         decodedBody = json.loads(event['body'])
    return comments.commentAdd(decodedBody,connection)
    
    # if event['rawPath'] == channelAddRawPath:
    #     channel_name = event['queryStringParameters']['channel_name']
    #     channel_Description = event['queryStringParameters']['channel_Description']
    #     channel_profile_pic = event['queryStringParameters']['channel_profile_pic']

    #     return channels.channelAdd(channel_name,channel_Description,channel_profile_pic)
    
    