import utils

def followChannel(decodedBody,connection):
    print("add follow request")
    cursor=connection.cursor()
    
    channelId=decodedBody['channelId']
    userId=decodedBody['userId']
    fields=['user_id','followers','views','channel_id']
    result=[]
    
    sql="""SELECT EXISTS(SELECT * FROM channel where id=%s)"""
    cursor.execute(sql,(channelId,))
    extracted_data=cursor.fetchone()
    print(extracted_data[0])
    
    if extracted_data[0]!=0:
        sql="""SELECT EXISTS(SELECT * FROM followers where channel_id=%s)"""
        cursor.execute(sql,(channelId,))
        extracted_data_views=cursor.fetchone()
    
    #sql="""select followers from followers where user_id=%s"""
    #cursor.execute(sql,(userId,))
    # extract_followers=cursor.fetchone()
    # print("hi",len(extract_followers),extract_followers[0])
    # follow=extract_followers[0]
    # print(follow)
    # if(len(extract_followers[0])==0):
    
        
        if extracted_data_views[0]==0:
            views=1
            sql="""SELECT first_name from users where id=%s"""
            cursor.execute(sql,(userId,))
            extracted_data_user=cursor.fetchone()
            print(extracted_data_user[0])
            sql="""INSERT INTO followers(followers,views,user_id,channel_id) values(%s,%s,%s,%s)"""
            val = (extracted_data_user[0],views,userId,channelId)
            cursor.execute(sql,val)
            connection.commit()
            
            sql="""Select * from followers where channel_id=%s"""
            cursor.execute(sql,(channelId,))
            extracted_data_ch=cursor.fetchall()
            for row in extracted_data_ch:
                response_data_body=dict(zip(fields,row))
                result.append(response_data_body)
            response_data={'message':'followers','data':result}
        else:
            sql="""SELECT first_name from users where id=%s"""
            cursor.execute(sql,(userId,))
            extracted_data_user=cursor.fetchone()
            print(extracted_data_user[0])
            
            sql="""select max(views) from followers where channel_id=%s"""
            cursor.execute(sql,(channelId,))
            extracted_data_views=cursor.fetchone()
            print(extracted_data_views[0])
            sql="""INSERT INTO followers(followers,views,user_id,channel_id) values(%s,%s,%s,%s)"""
            val = (extracted_data_user[0],extracted_data_views[0]+1,userId,channelId)
            cursor.execute(sql,val)
            connection.commit()
            print('hello else')
            cursor.close()
            response_data={'message':'followed already','data':[]}
    else:
        cursor.close()
        response_data={'message':'channel not found','data':[]}
        
    return utils.response("Passed",response_data)

def getChannelViews(channelId,connection):
    print("channel views request")
    cursor = connection.cursor()
    result=[]
    #fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id','category']
    feilds=['views']
    sql="""SELECT EXISTS(SELECT * FROM channel where id=%s)"""
    cursor.execute(sql,(userId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT views from followers where channel_id=%s"""
        cursor.execute(sql,(channelId,))
        extracted_data_ex=cursor.fetchall()
        
        for row in extracted_data_ex:
            response_data=dict(zip(fields,row))
            result.append(response_data)
            response_data={'message':'channel','data':result}
            #print(response_data)
    
    return utils.response("Passed",response_data)