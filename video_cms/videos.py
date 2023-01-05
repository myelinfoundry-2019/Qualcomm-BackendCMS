import utils

def videoList(channelId,connection): 
    print("received video request")
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM video where channel_id=%s )"""
    cursor.execute(sql,(channelId,))
    extracted_data=cursor.fetchone()
    
    fields=['id','videolink','thumbnail_url','created_at','channel_id']
    #field_tournament=['tournament_name']
    result=[]

    if extracted_data[0]!=0:
        sql="""select id,videolink,thumbnail_url,created_at,channel_id from video where channel_id=%s"""
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


def deleteVideo(channelId,videoId,connection):
    cursor=connection.cursor()
    sql="""SELECT EXISTS(SELECT * FROM video where id=%s and channel_id=%s)"""
    cursor.execute(sql,(videoId,channelId,))
    extracted_data=cursor.fetchone()
    print("hello")
    if extracted_data[0]!=0:
        sql="""SELECT * from video where id=%s"""
        cursor.execute(sql,(videoId,))
        extracted_data=cursor.fetchall()
        
        sql="""DELETE from video where id=%s"""
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
    sql="""SELECT EXISTS(SELECT * FROM video)"""
    cursor.execute(sql)
    extracted_data=cursor.fetchone()
    
    fields=['id','videolink','thumbnail_url','created_at','channel_id']
    #field_tournament=['tournament_name']
    result=[]

    if extracted_data[0]!=0:
        sql="""select id,videolink,thumbnail_url,created_at,channel_id from video where channel_id=%s LIMIT """
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