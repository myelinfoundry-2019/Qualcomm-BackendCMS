import mysql.connector

connection = mysql.connector.connect(

  host="videocms.cxiqoa7uqghb.ap-south-1.rds.amazonaws.com",
    #port=3306,
    user="admin",
    password="dx9MoHmSoEEz",
    database="videoCMS"

)
def showCommentsbyUserId():
  cursor=connection.cursor()
  user_id=1
  result=[]
  fields=['user_id','comments','likes','dislikes']

  sql="""SELECT EXISTS(SELECT * FROM comments where user_id=%s)"""
  cursor.execute(sql,(user_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""SELECT user_id,comment,likes from comments where user_id=%s"""
    cursor.execute(sql,(user_id,))
    extracted_data_ex=cursor.fetchall()

    for row in extracted_data_ex:
      response_data=dict(zip(fields,row))
      result.append(response_data)
      response_data={'message':'COMMENTS','data':result}
      print(response_data)
  else:
    cursor.close()
    response_data={'message':'comment not exist for user','data':[]}
  print("result->",result)

showCommentsbyUserId()



def addComments():
  cursor=connection.cursor()
  user_id=2
  video_id=2
  comment='Hello'
  result=[]
  #fields=['user_id','comments','replies','likes','dislikes']

  sql="""SELECT EXISTS(SELECT * FROM comments where user_id=%s and video_id=%s)"""
  cursor.execute(sql,(user_id,video_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]==0:
    sql="""INSERT INTO comments(comment,user_id,video_id) VALUES(%s,%s,%s) """
    val = (comment,user_id,video_id)
    cursor.execute(sql,val)
    connection.commit()
    
  else:
    cursor.close()
    response_data={'message':'comment already exist for user','data':[]}
    print(response_data)
  
  #print("result->",result)
 
addComments()

def updateComment(id):
  cursor=connection.cursor()
  
  comment="Hie"
  result=[]
  #fields=['user_id','comments','replies','likes','dislikes']

  sql="""SELECT EXISTS(SELECT * FROM comments where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""UPDATE comments SET comment=%s where id=%s"""
    val = (comment,id)
    cursor.execute(sql,val)
    connection.commit()
    
updateComment(1)

def deleteComment(id):
  cursor=connection.cursor()
  
  sql="""SELECT EXISTS(SELECT * FROM comments where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""DELETE from comments where id=%s"""
    cursor.execute(sql,(id,))
    print("comment deleted")
    connection.commit()
deleteComment(2)

def commentCount(video_id):
  cursor = connection.cursor()
  sql="""SELECT EXISTS(SELECT * FROM videos where id=%s)"""
  cursor.execute(sql,(video_id,))
  extracted_data=cursor.fetchone()
  if(extracted_data[0]!=0):

    sql="""select count(comment) from comments where video_id=%s"""
    cursor.execute(sql,(video_id,))
    extract_commnet_count=cursor.fetchall()
    count = [i[0] for i in extract_commnet_count]
    print("comment count",count[0])
    connection.commit()

commentCount(3)

def addLikes(id):
  cursor=connection.cursor()
  
  #fields=['user_id','comments','replies','likes','dislikes']
  sql="""SELECT EXISTS(SELECT * FROM comments where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  sql="""select likes from comments where id=%s"""
  cursor.execute(sql,(id,))
  extract_likes=cursor.fetchone()
  # print("hi",len(extract_likes),extract_likes[0])
  likes=extract_likes[0]
  
  if(likes==None):
    likes="0"
  if extracted_data[0]!=0:
    sql="""UPDATE comments SET likes=%s  WHERE id=%s"""
    val = ((int(likes)+1),id)
    cursor.execute(sql,val)
    connection.commit()
    
  # else:
  #   cursor.close()
  #   response_data={'message':'reply already exist for user','data':[]}
  #   print(response_data)
  
  #print("result->",result)
 
addLikes(4)

def adddisLikes(id):
  cursor=connection.cursor()
  
  #fields=['user_id','comments','replies','likes','dislikes']
  sql="""SELECT EXISTS(SELECT * FROM comments where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  sql="""select dislikes from comments where id=%s"""
  cursor.execute(sql,(id,))
  extract_likes=cursor.fetchone()
  # print("hi",len(extract_likes),extract_likes[0])
  dislikes=extract_likes[0]
  
  if(dislikes==None):
    dislikes="0"
  if extracted_data[0]!=0:
    sql="""UPDATE comments SET dislikes=%s  WHERE id=%s"""
    val = ((int(dislikes)+1),id)
    cursor.execute(sql,val)
    connection.commit()
    
  # else:
  #   cursor.close()
  #   response_data={'message':'reply already exist for user','data':[]}
  #   print(response_data)
  
  #print("result->",result)
 
adddisLikes(3)

def viewComments(video_id):
  cursor=connection.cursor()
  result=[]
  fields=['user_id','comments','likes','dislikes']

  sql="""SELECT EXISTS(SELECT * FROM comments where video_id=%s)"""
  cursor.execute(sql,(video_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""SELECT comment,likes,dislikes from comments where video_id=%s"""
    cursor.execute(sql,(video_id))
    extracted_data_ex=cursor.fetchall()

    for row in extracted_data_ex:
      response_data=dict(zip(fields,row))
      result.append(response_data)
      response_data={'message':'COMMENTS','data':result}
      print(response_data)
  else:
    cursor.close()
    response_data={'message':'comment not exist for user','data':[]}
  print("result->",result)
viewComments(1)

