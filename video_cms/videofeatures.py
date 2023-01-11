import utils


def addVideoLike(decodedBody,connection):
    #print("add video like request")
    cursor=connection.cursor()
    print("add video like request")
    videoId=decodedBody['video_id']
    userId=decodedBody['user_id']
    fields=['likes']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM videosfeature where video_id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    sql="""select likes from videosfeature where video_id=%s"""
    cursor.execute(sql,(videoId,))
    extract_likes=cursor.fetchone()
    
    print("hi",len(extract_likes),extract_likes[0])
    likes=extract_likes[0]
    
    
    if extracted_data[0]!=0:
        sql="""UPDATE videosfeature SET likes=%s,user_id=%s  WHERE video_id=%s"""
        val = ((int(likes)+1),userId,videoId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select likes from videosfeature where video_id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_data_body=dict(zip(fields,row))
            result.append(response_data_body)
            
        response_data={'message':'video likes','data':result}
    else:
        print('hello else')
        cursor.close()
        response_data={'message':'video not found','data':[]}
    return utils.response("Passed",response_data)
 
def addVideoDislike(decodedBody,connection):
    #print("add video like request")
    cursor=connection.cursor()
    print("add video dislike request")
    videoId=decodedBody['video_id']
    userId=decodedBody['user_id']
    fields=['dislikes']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM videosfeature where video_id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    sql="""select dislikes from videosfeature where video_id=%s"""
    cursor.execute(sql,(videoId,))
    extract_likes=cursor.fetchone()
    
    print("hi",len(extract_likes),extract_likes[0])
    likes=extract_likes[0]
    
    
    if extracted_data[0]!=0:
        sql="""INSERT into videosfeature(dislikes,user_id) value(%s,%s)"""
        val = ((int(likes)+1),userId)
        cursor.execute(sql,val)
        connection.commit()
        
        sql="""Select dislikes from videosfeature where video_id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
            response_data_body=dict(zip(fields,row))
            result.append(response_data_body)
            
        response_data={'message':'video dislikes','data':result}
    else:
        print('hello else')
        cursor.close()
        response_data={'message':'video not found','data':[]}
    return utils.response("Passed",response_data)

def getVideoViews(videoId,connection):
    print("channel  get views request")
    cursor = connection.cursor()
    result=[]
    #fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id','category']
    fields=['total_views']
    sql="""SELECT EXISTS(SELECT * FROM videofeatures where id=%s)"""
    cursor.execute(sql,(videoId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT sum(views) from followers where video_id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
            response_data=dict(zip(fields,row))
            result.append(response_data)
            response_data={'message':'video view','data':result}
            #print(response_data)
    
    return utils.response("Passed",response_data)