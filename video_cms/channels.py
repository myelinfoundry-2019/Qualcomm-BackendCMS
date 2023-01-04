import utils

def channelAdd(decodedBody,connection):
    print("Received channelAdd request")
    
    cursor = connection.cursor()  # get the cursor object
    
    userId=decodedBody["user_id"]
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
    
def viewChannels(userId,connection):
  print("view channel request")
  cursor = connection.cursor()
  result=[]
  fields=['id','channel_name','channel_description','channel_profile_pic','channel_user_id','created_at','category']
  
  sql="""SELECT EXISTS(SELECT * FROM channel where channel_user_id=%s)"""
  cursor.execute(sql,(userId,))
  extracted_data=cursor.fetchone()
  
  if extracted_data[0]!=0:
    sql="""SELECT * from channel where channel_user_id=%s"""
    cursor.execute(sql,(userId,))
    extracted_data_ex=cursor.fetchall()

    for row in extracted_data_ex:
      response_data=dict(zip(fields,row))
      result.append(response_data)
      response_data={'message':'channel','data':result}
      #print(response_data)
  else:
    cursor.close()
    response_data={'message':'channel not exist for user','data':[]}
    #print("result->",response_data)
  
  #response_data={'message':'user not exist','data':[]}
  return utils.response("Passed",response_data)
  
  
def searchChannel(searchItem,connection):
  print("received search item request")
  cursor=connection.cursor()
  result=[]
  fields=['id','channel_name','channel_description','channel_profile_pic','channel_user_id','created_at','category']
  
  sql="""SELECT EXISTS(SELECT * FROM channel)"""
  cursor.execute(sql)
  extracted_data=cursor.fetchone()
  
  if extracted_data[0]!=0:
      sql="""SELECT * from channel where channel_name like %s"""
      cursor.execute(sql,("%"+searchItem+"%",))
      extracted_data_ex=cursor.fetchall()
      
      print("Length->",len(extracted_data_ex))
      
      if len(extracted_data_ex)!=0:
          for row in extracted_data_ex:
              response_data=dict(zip(fields,row))
              result.append(response_data)
          response_data={'message':'channel','data':result}   
          return utils.response("response_data",response_data)
      else:
          cursor.close()
          response_data={'message':'channel not exist for user','data':[]}
      
          return utils.response("Passed",response_data)     
  else:
      cursor.close()
      response_data={'message':'channel not exist for user','data':[]}
  
      return utils.response("Failed",response_data)


def updateChannel(decodedBody,connection):
  cursor=connection.cursor()
  result=[]
  channel_name = decodedBody["channel_name"]
  channel_description = decodedBody["channel_Description"]
  channel_profile_pic = decodedBody["channel_profile_pic"]
  userId=decodedBody["userId"]
  channelId=decodedBody["channelId"]
  category = decodedBody["category"]
  fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id','category']

  sql="""SELECT EXISTS(SELECT * FROM channel where channel_user_id=%s)"""
  cursor.execute(sql,(userId,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""UPDATE channel SET channel_name=%s,channel_description=%s,channel_profile_pic=%s, channel_user_id=%s where id=%s"""
    val = (channel_name,channel_description,channel_profile_pic,userId,channelId)
    cursor.execute(sql,val)
    connection.commit()
    
    sql="""Select id,channel_name,channel_description,channel_profile_pic,channel_user_id,created_at,category from channel where channel_name=%s"""
    cursor.execute(sql,(channel_name,))
    extracted_data_ch=cursor.fetchall()
    for row in extracted_data_ch:
      response_da=dict(zip(fields,row))
      result.append(response_da)
    response_data={'message':'channel updated','data':result}
    
    
  else:
    cursor.close()
    response_data={'message':'channel not in use does not exist for user','data':[]}
    print("result->",response_data)
  return utils.response("Passed",response_data)


def deleteChannel(userId,channelId,connection):
  cursor=connection.cursor()
  sql="""SELECT EXISTS(SELECT * FROM channel where id=%s and channel_user_id=%s)"""
  cursor.execute(sql,(channelId,userId,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""SELECT * from channel where id=%s"""
    cursor.execute(sql,(channelId,))
    extracted_data=cursor.fetchall()

    sql="""DELETE from channel where id=%s"""
    cursor.execute(sql,(channelId,))
    connection.commit()
    
    response_data={'message':'channel deleted','data':[]}
    cursor.close()
    print("result->",response_data)
  else:
    cursor.close()
    response_data={'message':'channel not exist for user','data':[]}
    #print("result->",response_data)
  return utils.response("Passed",response_data)
