import mysql.connector

connection = mysql.connector.connect(

  host="videocms.cxiqoa7uqghb.ap-south-1.rds.amazonaws.com",
    #port=3306,
    user="admin",
    password="dx9MoHmSoEEz",
    database="videoCMS"

)
def addChannels():
  cursor=connection.cursor()
  channel_user_id=2
  channel_name='mygamchannel'
  channel_description='my game channel '
  channel_profile_pic='none'
  category='public'
  result=[]
  fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id']

  sql="""SELECT EXISTS(SELECT * FROM channel where channel_name=%s)"""
  cursor.execute(sql,(channel_name,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]==0:
    sql="""INSERT into channel(channel_name,channel_description,channel_profile_pic,channel_user_id,category) value(%s,%s,%s,%s,%s)"""
    val=(channel_name,channel_description,channel_profile_pic,channel_user_id,category)
    cursor.execute(sql,val)
    connection.commit()
  else:
    cursor.close()
    response_data={'message':'channel already exist for user','data':[]}
    print(response_data)
    
addChannels()
def viewChannels():
  cursor=connection.cursor()
  channel_user_id=3
  result=[]
  fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id']

  sql="""SELECT EXISTS(SELECT * FROM channel where channel_user_id=%s)"""
  cursor.execute(sql,(channel_user_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""SELECT * from channel where channel_user_id=%s"""
    cursor.execute(sql,(channel_user_id,))
    extracted_data_ex=cursor.fetchall()

    for row in extracted_data_ex:
      response_data=dict(zip(fields,row))
      result.append(response_data)
      response_data={'message':'channel','data':result}
      #print(response_data)
  else:
    cursor.close()
    response_data={'message':'channel not exist for user','data':[]}
  print("result->",response_data)

    
viewChannels()
  


def updateChannel():
  cursor=connection.cursor()
  channel_user_id=3
  id=2
  channel_name='game'
  channel_description='Game'
  channel_profile_pic='Link'
  result=[]
  fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id']

  sql="""SELECT EXISTS(SELECT * FROM channel where channel_user_id=%s)"""
  cursor.execute(sql,(channel_user_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""UPDATE channel SET channel_name=%s,channel_description=%s,channel_profile_pic=%s, channel_user_id=%s where id=%s"""
    val = (channel_name,channel_description,channel_profile_pic,channel_user_id,id)
    cursor.execute(sql,val)
    
    connection.commit()
    
    
  else:
    cursor.close()
    response_data={'message':'channel not in use does not exist for user','data':[]}
    print("result->",response_data)
updateChannel()

def deleteChannel(channel_id,channel_user_id):
  cursor=connection.cursor()
  
  sql="""SELECT EXISTS(SELECT * FROM channel where id=%s and channel_user_id=%s)"""
  cursor.execute(sql,(channel_id,channel_user_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""SELECT * from channel where id=%s"""
    cursor.execute(sql,(channel_id,))
    extracted_data=cursor.fetchall()

    sql="""DELETE from channel where id=%s"""
    cursor.execute(sql,(channel_id,))
    connection.commit()
    
    response_data={'message':'channel deleted','data':[]}
    cursor.close()
    print("result->",response_data)

deleteChannel(2,3) 
def searchChannel():
  cursor=connection.cursor()
  channel_user_id=3
  result=[]
  fields=['id','channel_name','channel_description','channel_profile_pic','created_at','channel_user_id']

  sql="""SELECT EXISTS(SELECT * FROM channel where channel_user_id=%s)"""
  cursor.execute(sql,(channel_user_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""SELECT * from channel where channel_user_id=%s"""
    cursor.execute(sql,(channel_user_id,))
    extracted_data_ex=cursor.fetchall()

    for row in extracted_data_ex:
      response_data=dict(zip(fields,row))
      result.append(response_data)
      response_data={'message':'channel','data':result}
      #print(response_data)
  else:
    cursor.close()
    response_data={'message':'channel not exist for user','data':[]}
  print("result->",response_data)
searchChannel() 

def followChannel(id):
  cursor=connection.cursor()
  channel_id=id
  #fields=['user_id','comments','replies','likes','dislikes']
  sql="""SELECT EXISTS(SELECT * FROM followers where id=%s not in (SELECT id=%s from channel))"""
  cursor.execute(sql,(channel_id,id))
  extracted_data=cursor.fetchone()

  follow=extracted_data[0]
  
  if(follow==None):
    follow="0"
  if extracted_data[0]!=0:
    sql="""INSERT into followers(follow,channel_id) value(%s,%s)"""
    val = ((int(follow)+1),id)
    cursor.execute(sql,val)
    connection.commit()
    
  # else:
  #   cursor.close()
  #   response_data={'message':'reply already exist for user','data':[]}
  #   print(response_data)
  
  
  #print("result->",result)
  return
followChannel(1)