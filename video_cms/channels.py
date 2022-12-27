import utils

def channelAdd(userId,decodedBody,connection):
    print("Received channelAdd request")
    
    cursor = connection.cursor()  # get the cursor object
    
    channel_name = decodedBody["channel_name"]
    channel_description = decodedBody["channel_Description"]
    channel_profile_pic = decodedBody["channel_profile_pic"]
    channel_user_id = userId
    category = decodedBody["category"]

    
    
    result=[]
    fields=['id','channel_name','channel_description','channel_profile_pic','channel_user_id','created_at','category']

    sql="""SELECT EXISTS(SELECT * FROM users where id=%s)"""
    cursor.execute(sql,(userId,))
    extracted_data=cursor.fetchone()
    print(extracted_data[0],len(extracted_data))
    
    if extracted_data[0]!=0:
      sql="""SELECT * FROM channel where channel_name=%s"""
      cursor.execute(sql,(channel_name,))
      extracted_data_c=cursor.fetchall()
      print(extracted_data_c,len(extracted_data_c))
    
      if(len(extracted_data_c)==0):
        sql="""INSERT into channel(channel_name,channel_Description,channel_profile_pic,channel_user_id,category) value(%s,%s,%s,%s,%s)"""
        val=(channel_name,channel_description,channel_profile_pic,channel_user_id,category)
        cursor.execute(sql,val)
      
        connection.commit()
        
        sql="""Select id,channel_name,channel_description,channel_profile_pic,channel_user_id,created_at,category from channel where channel_name=%s"""
        cursor.execute(sql,(channel_name,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
          response_da=dict(zip(fields,row))
          result.append(response_da)
        response_data={'message':'Channel Added',
                      'data':result}
        cursor.close()
        #return http response 
        #return utils.response("Passed",response_data)
      
      else:
        sql="""Select id,channel_name,channel_description,channel_profile_pic,channel_user_id,created_at,category from channel where channel_name=%s"""
        cursor.execute(sql,(channel_name,))
        extracted_data_ch=cursor.fetchall()
        for row in extracted_data_ch:
          response_da=dict(zip(fields,row))
          result.append(response_da)
        response_data={'message':'Channel already exist for user',
                      'data':result}
        cursor.close()
        
    else:
      cursor.close()
      response_data={'message':'user not exist','data':[]}
    return utils.response("Passed",response_data)
    
    
