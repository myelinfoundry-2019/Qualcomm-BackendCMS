import utils

def commentreplyAdd(decodedBody,connection):
    print("Received commentreplyAdd request")
    
    cursor = connection.cursor()  # get the cursor object
    
    reply=decodedBody['reply']
    commentId=decodedBody['commentId']
    userId=decodedBody['userId']
    #likes=decodedBody['likes']
    #dislikes=decodedBody['dislikes']
    result=[]
    fields=['id','replies','likes','dislikes','created_at','comment_id','user_id']
    sql="""SELECT EXISTS(SELECT * FROM comment where id=%s)"""
    cursor.execute(sql,(commentId,))
    extracted_data=cursor.fetchone()
    if extracted_data[0]!=0:
        sql="""SELECT * FROM commentreply where replies=%s"""
        cursor.execute(sql,(reply,))
        extracted_data_c=cursor.fetchall()
        print(extracted_data_c,len(extracted_data_c))
    
        if(len(extracted_data_c)==0):
            sql="""INSERT INTO commentreply(replies,user_id,comment_id) VALUES(%s,%s,%s) """
            val = (reply,userId,commentId)
            cursor.execute(sql,val)
            connection.commit()
            sql="""Select id,replies,likes,dislikes,created_at,comment_id,user_id from commentreply where replies=%s"""
            cursor.execute(sql,(reply,))
            extracted_data_ch=cursor.fetchall()
            for row in extracted_data_ch:
              response_da=dict(zip(fields,row))
              result.append(response_da)
            response_data={'message':'commentreply Added',
                          'data':result}
            cursor.close()
        
        
        else:
            
            sql="""Select id,replies,likes,dislikes,created_at,comment_id,user_id from commentreply where replies=%s"""
            cursor.execute(sql,(reply,))
            extracted_data_ch=cursor.fetchall()
            for row in extracted_data_ch:
              response_da=dict(zip(fields,row))
              result.append(response_da)
            response_data={'message':'commentreply already exist for user','data':result}
            cursor.close()
    else:
        cursor.close()
        response_data={'message':'user or video not exist','data':[]}
    
    #return http response
    return utils.response("Passed",response_data)

def updatecommentReply(decodedBody,connection):
    cursor=connection.cursor()
    replyId=decodedBody['replyId']
    reply=decodedBody['reply']
    commentId=decodedBody['commentId']
    userId=decodedBody['userId']
    result=[]
    fields=['id','replies','likes','dislikes','created_at','user_id','video_id']
    
    sql="""SELECT EXISTS(SELECT * FROM commentreply where id=%s)"""
    cursor.execute(sql,(replyId,))
    extracted_data=cursor.fetchone()
    #print(extracted_data)
    if extracted_data[0]!=0:
        sql="""UPDATE commentreply SET replies=%s where id=%s"""
        val = (reply,replyId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select id,replies,likes,dislikes,created_at,user_id,comment_id from commentreply where replies=%s"""
        cursor.execute(sql,(reply,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_da=dict(zip(fields,row))
            result.append(response_da)
        response_data={'message':'commentreply updated for user','data':result}
        
    #return http response
    else:
        cursor.close()
        response_data={'message':'commentreply not exist','data':[]}
    return utils.response("Passed",response_data)
    
    
def deletecommentreply(commentreplyId,connection):
    cursor=connection.cursor()
    
    sql="""SELECT EXISTS(SELECT * FROM commentreply where id=%s)"""
    cursor.execute(sql,(commentreplyId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""DELETE from commentreply where id=%s"""
        cursor.execute(sql,(commentreplyId,))
        print("commentreply deleted")
        connection.commit()
        response_data={'message':'commentreply deleted','data':[]}
    else:
        cursor.close()
        response_data={'message':'commentreply not fount','data':[]}
    return utils.response("Passed",response_data)
    

def commentreplyCount(videoId,connection):
    cursor = connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM videos where id=%s)"""
    cursor.execute(sql,(videoId,))
    result=[]
    fields=['id','commentreply','likes','dislikes']
    extracted_data=cursor.fetchone()
    if(extracted_data[0]!=0):
        sql="""select count(commentreply),commentreply,likes,dislikes from commentreply where video_id=%s"""
        cursor.execute(sql,(videoId,))
        
        extract_commnet_count=cursor.fetchall()
        print(extract_commnet_count,extract_commnet_count[0])
        for row in extract_commnet_count:
            response_da=dict(zip(fields,row))
            result.append(response_da)
        count = [i[0] for i in extract_commnet_count]
        print("commentreply count",count[0])
        connection.commit()
        response_data={'message':'commentreply Count','count':count[0],
            'data':result
        }
    else:
        cursor.close()
        response_data={'message':'No commentreply exist','data':[]}
    return utils.response("Passed",response_data)


def addcommentreplyLike(decodedBody,connection):
    print("add commentreply request")
    cursor=connection.cursor()
    
    commentreplyId=decodedBody['commentreplyId']
    userId=decodedBody['userId']
    commentId=decodedBody['commentId']
    fields=['commentreply','likes']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM commentreply where id=%s)"""
    cursor.execute(sql,(commentreplyId,))
    extracted_data=cursor.fetchone()
    
    sql="""select likes from commentreply where id=%s"""
    cursor.execute(sql,(commentreplyId,))
    extract_likes=cursor.fetchone()
    
    print("hi",len(extract_likes),extract_likes[0])
    likes=extract_likes[0]
    
    
    if extracted_data[0]!=0:
        sql="""UPDATE commentreply SET likes=%s  WHERE id=%s"""
        val = ((int(likes)+1),commentreplyId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select replies,likes from commentreply where id=%s"""
        cursor.execute(sql,(commentreplyId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_data_body=dict(zip(fields,row))
            result.append(response_data_body)
            
        response_data={'message':'commentreply likes','data':result}
    else:
        print('hello else')
        cursor.close()
        response_data={'message':'commentreply not found','data':[]}
    return utils.response("Passed",response_data)
 
def addcommentreplyDislike(decodedBody,connection):
    print("add commentreply request")
    cursor=connection.cursor()
    
    commentreplyId=decodedBody['commentreplyId']
    userId=decodedBody['userId']
    commentId=decodedBody['commentId']
    fields=['commentreply','likes']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM commentreply where id=%s)"""
    cursor.execute(sql,(commentreplyId,))
    extracted_data=cursor.fetchone()
    
    sql="""select dislikes from commentreply where id=%s"""
    cursor.execute(sql,(commentreplyId,))
    extract_likes=cursor.fetchone()
    print("hi",len(extract_likes),extract_likes[0])
    likes=extract_likes[0]
    
    
    if extracted_data[0]!=0:
        sql="""UPDATE commentreply SET dislikes=%s  WHERE id=%s"""
        val = ((int(likes)+1),commentreplyId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select replies,dislikes from commentreply where id=%s"""
        cursor.execute(sql,(commentreplyId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_data_body=dict(zip(fields,row))
            result.append(response_data_body)
            
        response_data={'message':'commentreply dislikes','data':result}
    else:
        print('hello else')
        cursor.close()
        response_data={'message':'commentreply not found','data':[]}
    return utils.response("Passed",response_data)

def viewcommentreplies(commentId,connection):
    cursor=connection.cursor()
    result=[]
    fields=['commentreply','likes','dislikes','user_id']
    
    sql="""SELECT EXISTS(SELECT * FROM commentreply where comment_id=%s)"""
    cursor.execute(sql,(commentId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT replies,likes,dislikes,user_id from commentreply where comment_id=%s"""
        cursor.execute(sql,(commentId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
          response_data=dict(zip(fields,row))
          result.append(response_data)
        response_data={'message':'commentreply','data':result}
        print(response_data)
    else:
        cursor.close()
        response_data={'message':'commentreply not exist for user','data':[]}
        print("result->",result)
    return utils.response("Passed",response_data)








