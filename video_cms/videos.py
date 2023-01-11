import utils


def videoList(channelId,connection): 
    print("received videolist request")
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM videos where channel_id=%s )"""
    cursor.execute(sql,(channelId,))
    extracted_data=cursor.fetchone()
    
    fields=['id','videolink','thumbnail_url','video_tittle','video_Description','video-type','created_at']
    #field_tournament=['tournament_name']
    result=[]

    if extracted_data[0]!=0:
        sql="""select v.id,v.videolink,v.thumbnail_url,vm.video_tittle,vm.video_Description,vm.video_type,vm.created_at from videos v inner join videosmetadata vm on v.id=vm.video_id where v.video_type=%s"""
        cursor.execute(sql,(channelId,))
        extracted_data=cursor.fetchall()

        for row in extracted_data:
            response_data=dict(zip(fields,row))
            result.append(response_data)


        response_data={'message':'Videos',
                                'data':result}

        cursor.close()

        #return http response 
        return utils.response("Passed",response_data)    

    else:
        response_data={'message':'List empty',
                                'data':[]}
        cursor.close()
        return utils.response('Failed',response_data)


def livevideoList(userId,connection): 
    print("received videolist request")
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM users where id=%s )"""
    cursor.execute(sql,(userId,))
    extracted_data=cursor.fetchone()
    live="Live"
    
    fields=['id','videolink','thumbnail_url','video_tittle','video_Description','video-type','created_at']
    #field_tournament=['tournament_name']
    result=[]

    if extracted_data[0]!=0:
        sql="""select v.id,v.videolink,v.thumbnail_url,vm.video_tittle,vm.video_Description,vm.video_type,vm.created_at from videos v inner join videosmetadata vm on v.id=vm.video_id where vm.video_type=%s"""
        cursor.execute(sql,(live,))
        extracted_data=cursor.fetchall()

        for row in extracted_data:
            response_data=dict(zip(fields,row))
            result.append(response_data)


        response_data={'message':'Videos',
                                'data':result}

        cursor.close()

        #return http response 
        return utils.response("Passed",response_data)    

    else:
        response_data={'message':'List empty',
                                'data':[]}
        cursor.close()
        return utils.response('Failed',response_data)
        
        
def vodvideoList(userId,connection): 
    print("received videolist request")
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM users where id=%s )"""
    cursor.execute(sql,(userId,))
    extracted_data=cursor.fetchone()
    vod="VOD"
    fields=['id','videolink','thumbnail_url','video_tittle','video_Description','video-type','created_at']
    #field_tournament=['tournament_name']
    result=[]

    if extracted_data[0]!=0:
        sql="""select v.id,v.videolink,v.thumbnail_url,vm.video_tittle,vm.video_Description,vm.video_type,vm.created_at from videos v inner join videosmetadata vm on v.id=vm.video_id where vm.video_type=%s"""
        cursor.execute(sql,(vod,))
        extracted_data=cursor.fetchall()

        for row in extracted_data:
            response_data=dict(zip(fields,row))
            result.append(response_data)


        response_data={'message':'Videos',
                                'data':result}

        cursor.close()

        #return http response 
        return utils.response("Passed",response_data)    

    else:
        response_data={'message':'List empty',
                                'data':[]}
        cursor.close()
        return utils.response('Failed',response_data)

def deleteVideo(channelId,videoId,connection):
    print("delete video request")
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM videos where id=%s and channel_id=%s)"""
    cursor.execute(sql,(videoId,channelId,))
    extracted_data=cursor.fetchone()
    print("hello")
    if extracted_data[0]!=0:
        print("hello")
        sql="""SELECT * from videos where id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data=cursor.fetchall()
        print("deleting")
        sql="""DELETE from videosmetadata where video_id=%s"""
        cursor.execute(sql,(videoId,))
        connection.commit()
        sql="""DELETE from videos where id=%s"""
        cursor.execute(sql,(videoId,))
        connection.commit()
        response_data={'message':'video deleted','data':[]}
        cursor.close()
        print("result->",response_data)
    else:
        cursor.close()
        response_data={'message':'video not exist for channel','data':[]}
        #print("result->",response_data)
    return utils.response("Passed",response_data)
    
def top10videoList(connection): 
    print("received top 10 video request")
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM videos)"""
    cursor.execute(sql)
    extracted_data=cursor.fetchone()
    
    fields=['id','videolink','thumbnail_url','created_at','channel_id']
    #field_tournament=['tournament_name']
    result=[]

    if extracted_data[0]!=0:
        sql="""select id,videolink,thumbnail_url,created_at,channel_id from videos where channel_id=%s LIMIT """
        cursor.execute(sql,(channelId,))
        extracted_data=cursor.fetchall()

        for row in extracted_data:
            response_data=dict(zip(fields,row))
            result.append(response_data)


        response_data={'message':'Videos',
                                'data':result}

        cursor.close()

        #return http response 
        return utils.response("Passed",response_data)    

    else:
        response_data={'message':'List empty',
                                'data':[]}
        cursor.close()
        return utils.response('Failed',response_data)
        
def addVideo(decodedBody,connection):
  
    print("Received add Video request")
    
    cursor = connection.cursor()  # get the cursor object
    
    channelId=decodedBody["channel_id"]
    userId = decodedBody["user_id"]
    video_tittle = decodedBody["video_tittle"]
    video_description = decodedBody["video_Description"]
    video_type= decodedBody["video_type"]
    video_link = decodedBody["video_link"]
    thumbnail_url = decodedBody["thumbnail_url"]
    category_description = decodedBody["category_description"]
    video_tags = decodedBody["video_tags"]
    #my_string = ','.join(map(str, video_tags)) 
    video_id=decodedBody["video_id"]
    likes=0
    dislikes=0
    views=0
    #my_string = ','.join(map(str, video_tags))
    result=[]
    fields=['id','channel_id','user_id','video_tittle','video_Description','video_link','thubnail_url','category_description','video_tags']

    sql="""SELECT EXISTS(SELECT * FROM channel where id=%s)"""
    cursor.execute(sql,(channelId,))
    extracted_data=cursor.fetchone()
    print(extracted_data[0],len(extracted_data))
    
    
    if extracted_data[0]!=0:
      sql="""SELECT * FROM videosmetadata where video_id=%s"""
      cursor.execute(sql,(video_id,))
      extracted_data_c=cursor.fetchall()
      print(extracted_data_c,len(extracted_data_c))
    
      if(len(extracted_data_c)==0):
        sql="""INSERT into videos(id,videolink,thumbnail_url,channel_id) value(%s,%s,%s,%s)"""
        val=(video_id,video_link,thumbnail_url,channelId)
        cursor.execute(sql,val)
        
        # sql="""select id from videos"""
        # #cursor.execute(sql,(video_link))
        # cursor.execute(sql)
        # extracted_video_id=cursor.fetchone()
        # video_id=extracted_video_id[0]
        # print("video_id",video_id)
        # cursor = connection.cursor(buffered=True)
        
        sql="""INSERT into videosmetadata(video_id,video_tittle,video_Description,video_type,video_tags) value(%s,%s,%s,%s,%s)"""
        val=(video_id,video_tittle,video_description,video_type,video_tags)
        cursor.execute(sql,val)
        connection.commit()
        
        
        sql="""INSERT into videosfeature(video_id,likes,dislikes,views) value(%s,%s,%s,%s)"""
        val=(video_id,likes,dislikes,views)
        cursor.execute(sql,val)
        connection.commit()
        
        
        sql="""Select id,channel_id from videos where channel_id=%s"""
        cursor.execute(sql,(channelId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
          response_da=dict(zip(fields,row))
          result.append(response_da)
        response_data={'message':'video Added',
                      'data':result}
        cursor.close()
        #return http response 
        #return utils.response("Passed",response_data)
      
      else:
        sql="""Select * from videosmetadata where video_tittle=%s"""
        cursor.execute(sql,(video_tittle,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
          response_da=dict(zip(fields,row))
          result.append(response_da)
        response_data={'message':'video already exist for channel',
                      'data':result}
        cursor.close()
        
    else:
      cursor.close()
      response_data={'message':'user not exist','data':[]}
    return utils.response("Passed",response_data)
    
    
def updateVideo(decodedBody,connection):
    print("Received update Video request")
    
    cursor = connection.cursor()  # get the cursor object
    
    channelId=decodedBody["channel_id"]
    userId = decodedBody["user_id"]
    video_tittle = decodedBody["video_tittle"]
    video_description = decodedBody["video_Description"]
    video_type= decodedBody["video_type"]
    video_link = decodedBody["video_link"]
    thumbnail_url = decodedBody["thumbnail_url"]
    category_description = decodedBody["category_description"]
    video_tags = decodedBody["video_tags"]
    #my_string = ','.join(map(str, video_tags)) 
    video_id=decodedBody["video_id"]
    #my_string = ','.join(map(str, video_tags))
    result=[]
    fields=['id','channel_id','user_id','video_tittle','video_Description','video_link','thubnail_url','category_description','video_tags']

    sql="""SELECT EXISTS(SELECT * FROM channel where id=%s)"""
    cursor.execute(sql,(channelId,))
    extracted_data=cursor.fetchone()
    print(extracted_data[0],len(extracted_data))
    
    
    if extracted_data[0]!=0:
      sql="""SELECT * FROM videosmetadata where video_id=%s"""
      cursor.execute(sql,(video_id,))
      extracted_data_c=cursor.fetchall()
      print(extracted_data_c,len(extracted_data_c))
    
      if(len(extracted_data_c)==0):
        sql="""UPDATE videos SET thumbnail_url=%s where id=%s"""
        val=(thumbnail_url,video_id)
        cursor.execute(sql,val)
        
        # sql="""select id from videos"""
        # #cursor.execute(sql,(video_link))
        # cursor.execute(sql)
        # extracted_video_id=cursor.fetchone()
        # video_id=extracted_video_id[0]
        # print("video_id",video_id)
        # cursor = connection.cursor(buffered=True)
        
        sql="""UPDATE videosmetadata SET video_tittle=%s,video_Description=%s,video_type=%s,video_tags=%s where video_id=%s"""
        val=(video_tittle,video_description,video_type,video_tags,video_id)
        cursor.execute(sql,val)
        connection.commit()
        
        
        
        sql="""Select id,channel_id from videos where channel_id=%s"""
        cursor.execute(sql,(channelId,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
          response_da=dict(zip(fields,row))
          result.append(response_da)
        response_data={'message':'video Added',
                      'data':result}
        cursor.close()
        #return http response 
        #return utils.response("Passed",response_data)
      
      else:
        sql="""Select * from videosmetadata where video_tittle=%s"""
        cursor.execute(sql,(video_tittle,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
          response_da=dict(zip(fields,row))
          result.append(response_da)
        response_data={'message':'video already exist for channel',
                      'data':result}
        cursor.close()
        
    else:
      cursor.close()
      response_data={'message':'user not exist','data':[]}
    return utils.response("Passed",response_data)