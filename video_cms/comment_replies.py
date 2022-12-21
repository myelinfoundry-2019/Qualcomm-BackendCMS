import mysql.connector

connection = mysql.connector.connect(

  host="videocms.cxiqoa7uqghb.ap-south-1.rds.amazonaws.com",
    #port=3306,
    user="admin",
    password="dx9MoHmSoEEz",
    database="videoCMS"

)


def addReplies(comment_id):
  cursor=connection.cursor()
  user_id=2
  replies='Hello user3'
  likes=0
  dislikes=0
  #fields=['user_id','comments','replies','likes','dislikes']

  sql="""SELECT EXISTS(SELECT * from comments where id=%s)"""
  cursor.execute(sql,(comment_id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    
    sql="""SELECT id,replies from comment_replies where replies=%s"""
    cursor.execute(sql,(replies,))
    extracted_data_r=cursor.fetchall()

    if(len(extracted_data_r)==0):
      sql = """INSERT into comment_replies(replies,comment_id,user_id,likes,dislikes) value(%s,%s,%s,%s,%s)"""
      val = (replies,comment_id,user_id,likes,dislikes)
      cursor.execute(sql,val)
      connection.commit()
    
    else:
      cursor.close()
      response_data={'message':'reply already exist for user','data':[]}
      print(response_data)
  else:
    cursor.close()
    response_data={'message':'comment not exist for user','data':[]}
    print(response_data)
  #print("result->",result)
 
addReplies(4)

def addLikestoReplies(id):
  cursor=connection.cursor()
  
  #fields=['user_id','comments','replies','likes','dislikes']
  sql="""SELECT EXISTS(SELECT * FROM comment_replies where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  sql="""select likes from comment_replies where id=%s"""
  cursor.execute(sql,(id,))
  extract_likes=cursor.fetchone()
  # print("hi",len(extract_likes),extract_likes[0])
  likes=extract_likes[0]
  
  if(likes==None):
    likes="0"
  if extracted_data[0]!=0:
    sql="""UPDATE comment_replies SET likes=%s  WHERE id=%s"""
    val = ((int(likes)+1),id)
    cursor.execute(sql,val)
    connection.commit()
    
  # else:
  #   cursor.close()
  #   response_data={'message':'reply already exist for user','data':[]}
  #   print(response_data)
  
  #print("result->",result)
 
addLikestoReplies(17)

def adddisLikestoReplies(id):
  cursor=connection.cursor()
  
  #fields=['user_id','comments','replies','likes','dislikes']
  sql="""SELECT EXISTS(SELECT * FROM comment_replies where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  sql="""select dislikes from comment_replies where id=%s"""
  cursor.execute(sql,(id,))
  extract_likes=cursor.fetchone()
  # print("hi",len(extract_likes),extract_likes[0])
  dislikes=extract_likes[0]
  print(dislikes)
  if(dislikes==None):
    dislikes="0"
  if extracted_data[0]!=0:
    sql="""UPDATE comment_replies SET dislikes=%s  WHERE id=%s"""
    val = ((int(dislikes)+1),id)
    cursor.execute(sql,val)
    connection.commit()
    
  # else:
  #   cursor.close()
  #   response_data={'message':'reply already exist for user','data':[]}
  #   print(response_data)
  
  #print("result->",result)
 
adddisLikestoReplies(17)

def updateCommentReplies(id):
  cursor=connection.cursor()
  
  replies="Hie"
  result=[]
  #fields=['user_id','comments','replies','likes','dislikes']

  sql="""SELECT EXISTS(SELECT * FROM comment_replies where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""UPDATE comment_replies SET replies=%s where id=%s"""
    val = (replies,id)
    cursor.execute(sql,val)
    connection.commit()
    
updateCommentReplies(1)

def deleteCommentReplies(id):
  cursor=connection.cursor()
  
  sql="""SELECT EXISTS(SELECT * FROM comment_replies where id=%s)"""
  cursor.execute(sql,(id,))
  extracted_data=cursor.fetchone()

  if extracted_data[0]!=0:
    sql="""DELETE from comment_replies where id=%s"""
    cursor.execute(sql,(id,))
    print("Reply deleted")
    connection.commit()
deleteCommentReplies(2)



def commentrepliesCount(comment_id):
  cursor = connection.cursor()
  sql="""SELECT EXISTS(SELECT * FROM comments where id=%s)"""
  cursor.execute(sql,(comment_id,))
  extracted_data=cursor.fetchone()
  if(extracted_data[0]!=0):

    sql="""select count(replies) from comment_replies where comment_id=%s"""
    cursor.execute(sql,(comment_id,))
    extract_commnet_count=cursor.fetchall()
    count = [i[0] for i in extract_commnet_count]
    print("comment replies count",count[0])
    connection.commit()

commentrepliesCount(4)