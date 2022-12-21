import mysql.connector

connection = mysql.connector.connect(

  host="videocms.cxiqoa7uqghb.ap-south-1.rds.amazonaws.com",
    #port=3306,
    user="admin",
    password="dx9MoHmSoEEz",
    database="videoCMS"

)
def addVideoMetadata(video_id):
  cursor=connection.cursor()
  result=[]
  video_Metadata_tittle='NewStateXYz'
  video_Description='NewState tournament'
  stream_Description='My Stream'
  category_Description='Games Tournament'
  game_info_id=1
  tournament_info_id=1
  round_info_id=1
  video_type='Live'
  views=0
  report='Voilation'
  video_uploader_user_id=1

  sql="""SELECT EXISTS(SELECT * FROM videos where id=%s)"""
  cursor.execute(sql,(video_id,))
  extracted_data=cursor.fetchone()
  print(extracted_data)

  if extracted_data[0]!=0:
    # check in metadata validation
    sql="""SELECT id,video_Metadata_tittle FROM video_metadata where video_Metadata_tittle=%s"""
    cursor.execute(sql,(video_Metadata_tittle,))
    extracted_data1=cursor.fetchall()
    
       
         #if not exist in metadata
    if(len(extracted_data1)==0):
        print("hello inserting")
        #extracting into var 
        sql="""INSERT INTO video_metadata(video_Metadata_tittle,video_Description,stream_Description,category_Description,game_info_id,tournament_info_id,round_info_id,video_type,views,report,videouploader_user_id,video_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
        val = (video_Metadata_tittle,video_Description,stream_Description,category_Description,game_info_id,tournament_info_id,round_info_id,video_type,views,report,video_uploader_user_id,video_id)
        cursor.execute(sql,val)
        connection.commit()
    else:
        cursor.close()
        response_data={'message':'video_metadata exist for user','data':[]}
        print(response_data)

    
  else:
    cursor.close()
    response_data={'message':'video not exist for user','data':[]}
    print(response_data)
  
  #print("result->",result)
 


addVideoMetadata(4)