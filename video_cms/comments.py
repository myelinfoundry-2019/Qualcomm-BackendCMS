import utils

def commentAdd(decodedBody,connection):
    print("Received CommentAdd request")
    
    cursor = connection.cursor()  # get the cursor object
    
    userId=decodedBody['userId']
    videoId=decodedBody['videoId']
    comment=decodedBody['comment']
    result=[]
    fields=['id','comment','likes','dislikes','created_at','user_id','video_id']
    sql="""SELECT EXISTS(SELECT * FROM videos where id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    if extracted_data[0]!=0:
        sql="""SELECT * FROM comment where comment=%s"""
        cursor.execute(sql,(comment,))
        extracted_data_c=cursor.fetchall()
        print(extracted_data_c,len(extracted_data_c))
    
        if(len(extracted_data_c)==0):
            sql="""INSERT INTO comment(comment,user_id,video_id) VALUES(%s,%s,%s) """
            val = (comment,userId,videoId)
            cursor.execute(sql,val)
            connection.commit()
            sql="""Select id,comment,likes,dislikes,created_at,user_id,video_id from comment where comment=%s"""
            cursor.execute(sql,(comment,))
            extracted_data_ch=cursor.fetchall()
            for row in extracted_data_ch:
              response_da=dict(zip(fields,row))
              result.append(response_da)
            response_data={'message':'Comment Added',
                          'data':result}
            cursor.close()
        
        else:
            
            sql="""Select id,comment,likes,dislikes,created_at,user_id,video_id from comment where comment=%s"""
            cursor.execute(sql,(comment,))
            extracted_data_ch=cursor.fetchall()
            for row in extracted_data_ch:
              response_da=dict(zip(fields,row))
              result.append(response_da)
            response_data={'message':'comment already exist for user','data':result}
            cursor.close()
    else:
        cursor.close()
        response_data={'message':'user or video not exist','data':[]}
    
    #return http response
    return utils.response("Passed",response_data)

def updateComment(decodedBody,connection):
    cursor=connection.cursor()
    
    comment=decodedBody['comment']
    userId=decodedBody['userId']
    videoId=decodedBody['videoId']
    commentId=decodedBody['commentId']
    result=[]
    fields=['id','comment','likes','dislikes','created_at','user_id','video_id']
    
    sql="""SELECT EXISTS(SELECT * FROM comment where id=%s)"""
    cursor.execute(sql,(commentId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""UPDATE comment SET comment=%s where id=%s"""
        val = (comment,commentId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select id,comment,likes,dislikes,created_at,user_id,video_id from comment where comment=%s"""
        cursor.execute(sql,(comment,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_da=dict(zip(fields,row))
            result.append(response_da)
        response_data={'message':'comment updated for user','data':result}
        cursor.close()
    #return http response
    else:
        cursor.close()
        response_data={'message':'comment not exist','data':[]}
    return utils.response("Passed",response_data)
    
    
def deleteComment(commentId,connection):
    cursor=connection.cursor()
    
    sql="""SELECT EXISTS(SELECT * FROM comment where id=%s)"""
    cursor.execute(sql,(commentId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""DELETE from comment where id=%s"""
        cursor.execute(sql,(commentId,))
        print("comment deleted")
        connection.commit()
        response_data={'message':'comment deleted','data':[]}
    else:
        cursor.close()
        response_data={'message':'comment not fount','data':[]}
    return utils.response("Passed",response_data)
    

def commentCount(videoId,connection):
    cursor = connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM videos where id=%s)"""
    cursor.execute(sql,(videoId,))
    result=[]
    fields=['id','comment','likes','dislikes']
    extracted_data=cursor.fetchone()
    if(extracted_data[0]!=0):
        sql="""select count(comment),comment,likes,dislikes from comment where video_id=%s"""
        cursor.execute(sql,(videoId,))
        
        extract_commnet_count=cursor.fetchall()
        print(extract_commnet_count,extract_commnet_count[0])
        for row in extract_commnet_count:
            response_da=dict(zip(fields,row))
            result.append(response_da)
        count = [i[0] for i in extract_commnet_count]
        print("comment count",count[0])
        connection.commit()
        response_data={'message':'Comment Count','count':count[0],
            'data':result
        }
    else:
        cursor.close()
        response_data={'message':'No comment exist','data':[]}
    return utils.response("Passed",response_data)


def addCommentLike(decodedBody,connection):
    print("add comment request")
    cursor=connection.cursor()
    
    commentId=decodedBody['commentId']
    userId=decodedBody['userId']
    videoId=decodedBody['videoId']
    fields=['comment','likes']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM comment where id=%s)"""
    cursor.execute(sql,(commentId,))
    extracted_data=cursor.fetchone()
    
    sql="""select likes from comment where id=%s"""
    cursor.execute(sql,(commentId,))
    extract_likes=cursor.fetchone()
    
    print("hi",len(extract_likes),extract_likes[0])
    likes=extract_likes[0]
    
    
    if extracted_data[0]!=0:
        sql="""UPDATE comment SET likes=%s  WHERE id=%s"""
        val = ((int(likes)+1),commentId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select comment,likes from comment where id=%s"""
        cursor.execute(sql,(commentId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_data_body=dict(zip(fields,row))
            result.append(response_data_body)
            
        response_data={'message':'comment likes','data':result}
    else:
        print('hello else')
        cursor.close()
        response_data={'message':'comment not found','data':[]}
    return utils.response("Passed",response_data)
 
def addCommentDislike(decodedBody,connection):
    print("add comment request")
    cursor=connection.cursor()
    
    commentId=decodedBody['commentId']
    userId=decodedBody['userId']
    videoId=decodedBody['videoId']
    fields=['comment','likes']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM comment where id=%s)"""
    cursor.execute(sql,(commentId,))
    extracted_data=cursor.fetchone()
    
    sql="""select dislikes from comment where id=%s"""
    cursor.execute(sql,(commentId,))
    extract_likes=cursor.fetchone()
    
    print("hi",len(extract_likes),extract_likes[0])
    likes=extract_likes[0]
    
    
    if extracted_data[0]!=0:
        sql="""UPDATE comment SET dislikes=%s  WHERE id=%s"""
        val = ((int(likes)+1),commentId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select comment,dislikes from comment where id=%s"""
        cursor.execute(sql,(commentId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_data_body=dict(zip(fields,row))
            result.append(response_data_body)
            
        response_data={'message':'comment dislikes','data':result}
    else:
        print('hello else')
        cursor.close()
        response_data={'message':'comment not found','data':[]}
    return utils.response("Passed",response_data)

def viewComments(videoId,connection):
    cursor=connection.cursor()
    result=[]
    fields=['user_id','comment','likes','dislikes']
    
    sql="""SELECT EXISTS(SELECT * FROM comment where video_id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT comment,likes,dislikes from comment where video_id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
          response_data=dict(zip(fields,row))
          result.append(response_data)
        response_data={'message':'COMMENT','data':result}
        print(response_data)
    else:
        cursor.close()
        response_data={'message':'comment not exist for user','data':[]}
        print("result->",result)
    return utils.response("Passed",response_data)



def topComments(videoId,connection):
    cursor=connection.cursor()
    result=[]
    fields=['user_id','comment','likes','dislikes']
    
    sql="""SELECT EXISTS(SELECT * FROM comment where video_id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT user_id,comment,likes,dislikes from comment where video_id=%s order by likes desc LIMIT 2"""
        cursor.execute(sql,(videoId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
          response_data=dict(zip(fields,row))
          result.append(response_data)
        response_data={'message':'COMMENT','data':result}
        print(response_data)
    else:
        cursor.close()
        response_data={'message':'comment not exist for user','data':[]}
        print("result->",result)
    return utils.response("Passed",response_data)



def newComments(videoId,connection):
    cursor=connection.cursor()
    result=[]
    fields=['user_id','comment','likes','dislikes']
    
    sql="""SELECT EXISTS(SELECT * FROM comment where video_id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT user_id,comment,likes,dislikes from comment where video_id=%s ORDER BY `created_at` DESC"""
        cursor.execute(sql,(videoId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
          response_data=dict(zip(fields,row))
          result.append(response_data)
        response_data={'message':'COMMENT','data':result}
        print(response_data)
    else:
        cursor.close()
        response_data={'message':'comment not exist for user','data':[]}
        print("result->",result)
    return utils.response("Passed",response_data)

def viewCommentsUser(videoId,connection):
    print("user comments")
    cursor=connection.cursor()
    result=[]
    fields=['first_name','profile_pic_link','comment','likes','dislikes']
    
    sql="""SELECT EXISTS(SELECT * FROM comment where video_id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT u.first_name,u.profile_pic_link,c.comment,c.likes,c.dislikes from comment c inner join users u on u.id=c.user_id where video_id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
          response_data=dict(zip(fields,row))
          result.append(response_data)
        response_data={'message':'USER COMMENTS','data':result}
        print(response_data)
    else:
        cursor.close()
        response_data={'message':'comment not exist for user','data':[]}
        print("result->",result)
    return utils.response("Passed",response_data)