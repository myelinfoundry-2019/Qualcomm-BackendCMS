import utils

def commentAdd(decodedBody,connection):
    print("Received CommentAdd request")
    
    cursor = connection.cursor()  # get the cursor object
    
    comment=decodedBody['comment']
    likes=decodedBody['likes']
    dislikes=decodedBody['dislikes']
    user_id=decodedBody['user_id']
    video_id=decodedBody['video_id']
    result = []
    fields = ['id','comments','replies','likes']
    sql="""SELECT EXISTS(SELECT * FROM comments WHERE user_id=%s and video_id=%s)"""
    cursor.execute(sql,(user_id,video_id,))
    extracted_data = cursor.fetchone()
    print("extracted",extracted_data)
    if extracted_data[0]==0:
        sql = "INSERT INTO comments (comment,replies,likes,dislikes,user_id,video_id) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (comment,replies,likes,dislikes,user_id,video_id)
        cursor.execute(sql,val)
        connection.commit()
    else:
        extracted_data=cursor.fetchall()
        for row in extracted_data:
            response=dict(zip(fields,row))
            result.append(response)
        cursor.close()
        response_data={'message':'already comment exist','data':result}
        return utils.response("Failed",response_data)
        
    
    #return http response
    return utils.response("Passed",response_data)


# def addRepliestoComment():
#     return 0

# def addLikestoComment():
#     return 0
# def addDislikestoComment():
#     return 0
# def addLikestoReplies():
#     return 0
# def addDislikestoReplies():
#     return 0    
# def updateComment():
#     return 0
# def addRepliestoComment():
#     return 0








