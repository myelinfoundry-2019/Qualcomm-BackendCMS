import mysql.connector
import json
import channels
import test
import followers
import comments
import videoMetadata
import commentreplies

#addsIngestRawPath = "/channel/video/addIngest" # POST , BODY

#categoryAddRawPath = "/user/category/addCategory" # POST, BODY

#videoChannelRawPath='/video/videoChannel' # POST, BODY

testFunctionRawPath="/qualcommbackendcms/test" #GET, BODY



channelAddRawPath = "/channels/addChannel" #POST, BODY
channelsViewRawPath = "/channels/viewChannel" #GET, BODY
channelSearchRawPath = "/channels/searchChannel" #GET, BODY
updateChannelRawPath = "/channels/updateChannel" #Patch, BODY
deleteChannelRawPath = "/channels/deleteChannel" #DELETE, BODY


commentsAddRawPath = "/comments/addComment" #POST, BODY
commentsUpdateRawPath = "/comments/updateComment" #PATCH, BODY
commentsDeleteRawPath = "/comments/deleteComment" #DELETE, BODY
commentsViewRawPath = "/comments/viewComments" #GET, BODY
commentsCountRawPath = "/comments/commentCount" #POST, BODY
commentsLikeRawPath = "/comments/addCommentLike" #PATCH, BODY
commentsDislikeRawPath = "/comments/addCommentDislike" #PATCH, BODY


commentsReplyAddRawPath ="/replies/addReply" #POST,BODY
commentsReplyUpdateRawPath ="/replies/updateReply" #PATCH,BODY
commentsReplyDeleteRawPath ="/replies/deleteReply" #DELETE,BODY
commentsReplyViewRawPath ="/replies/viewReply" #GET,BODY
commentsReplyCountRawPath ="/replies/countReplies" #GET,BODY
commentsReplyLikeRawPath ="/replies/addLikeReply" #PATCH,BODY
commentsReplyDislikeRawPath ="/replies/addDislikeReply" #PATCH,BODY

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
        decodedBody = json.loads(event['body'])
        return channels.channelAdd(decodedBody,connection)
        
    if event['rawPath'] == channelsViewRawPath:
        print("Channels view success")
        userId = event['queryStringParameters']['user_id']
        return channels.viewChannels(userId,connection)
        
    if event['rawPath'] == channelSearchRawPath:
        searchItem = event['queryStringParameters']['searchItem']
        return channels.searchChannel(searchItem,connection)
        
    if event['rawPath'] == updateChannelRawPath:
        print("Channel success")
        #channelId = event['queryStringParameters']['channelId']
        decodedBody = json.loads(event['body'])
        return channels.updateChannel(decodedBody,connection)
        
    if event['rawPath'] == deleteChannelRawPath:
        print("Channel success")
        userId = event['queryStringParameters']['userId']
        channelId = event['queryStringParameters']['channelId']
        return channels.deleteChannel(userId,channelId,connection)
            
    
    if event['rawPath'] == commentsAddRawPath:
        print("Comment success")
        # userId = event['queryStringParameters']['userId']
        # videoId = event['queryStringParameters']['videoId']
        decodedBody = json.loads(event['body'])
        return comments.commentAdd(decodedBody,connection)
        
    if event['rawPath'] == commentsUpdateRawPath:
        print("Comment success")
        # userId = event['queryStringParameters']['userId']
        # videoId = event['queryStringParameters']['videoId']
        #commentId = event['queryStringParameters']['commentId']
        decodedBody = json.loads(event['body'])
        return comments.updateComment(decodedBody,connection)
        
    if event['rawPath'] == commentsDeleteRawPath:
        print("Comment success")
        #userId = event['queryStringParameters']['userId']
        #videoId = event['queryStringParameters']['videoId']
        commentId = event['queryStringParameters']['commentId']
        return comments.deleteComment(commentId,connection)
        
    if event['rawPath'] == commentsViewRawPath:
        print("Comment success")
        videoId = event['queryStringParameters']['videoId']
        return comments.viewComments(videoId,connection)
        
    if event['rawPath'] == commentsCountRawPath:
        print("Comment success")
        videoId = event['queryStringParameters']['videoId']
        return comments.commentCount(videoId,connection)
        
    if event['rawPath'] == commentsLikeRawPath:
        print("Comment like success")
        # videoId = event['pathParameters']['videoId']
        # commentId = event['pathParameters']['commentId']
        decodedBody = json.loads(event['body'])
        return comments.addCommentLike(decodedBody,connection)
        
    if event['rawPath'] == commentsDislikeRawPath:
        print("Comment dislike success")
        decodedBody = json.loads(event['body'])
        return comments.addCommentDislike(decodedBody,connection)
        
        
    if event['rawPath'] == commentsReplyAddRawPath:
        print("Comment Reply success")
        decodedBody = json.loads(event['body'])
        return commentreplies.commentreplyAdd(decodedBody,connection)
        
    if event['rawPath'] == commentsReplyUpdateRawPath:
        print("Comment reply success")
        decodedBody = json.loads(event['body'])
        return commentreplies.updatecommentReply(decodedBody,connection)
        
    if event['rawPath'] == commentsReplyDeleteRawPath:
        print("Comment reply success")
        commentReplyId = event['queryStringParameters']['commentReplyId']
        return commentreplies.deletecommentreply(commentReplyId,connection)
        
    if event['rawPath'] == commentsReplyViewRawPath:
        print("Comment reply success")
        #userId = event['queryStringParameters']['userId']
        commentId = event['queryStringParameters']['commentId']
        return commentreplies.viewcommentreplies(commentId,connection)
        
    if event['rawPath'] == commentsReplyCountRawPath:
        print("Comment reply success")
        videoId = event['queryStringParameters']['videoId']
        commentId = event['queryStringParameters']['commentId']
        return commentreplies.commentreplyCount(videoId,commentId,connection)
        
    if event['rawPath'] == commentsReplyLikeRawPath:
        print("Comment reply like success")
        # videoId = event['pathParameters']['videoId']
        # commentId = event['pathParameters']['commentId']
        decodedBody = json.loads(event['body'])
        return commentreplies.addcommentreplyLike(decodedBody,connection)
        
    if event['rawPath'] == commentsReplyDislikeRawPath:
        print("Comment reply dislike success")
        decodedBody = json.loads(event['body'])
        return commentreplies.addcommentreplyDislike(decodedBody,connection)
    
                                 

        
        

        
    
    
