import utils
def removeFollower(channel_id,followerId,connection):
    cursor=connection.cursor()
    print("hello")
    sql="""SELECT EXISTS(SELECT * FROM followers where id=%s and channel_id=%s)"""
    cursor.execute(sql,(followerId,channelId,))
    extracted_data=cursor.fetchone()
    
    if extracted_data[0]!=0:
        sql="""SELECT * from followers where id=%s"""
        cursor.execute(sql,(followerId,))
        extracted_data=cursor.fetchall()
        
        sql="""DELETE from followers where id=%s"""
        cursor.execute(sql,(followerId,))
        connection.commit()
        
        response_data={'message':'follower removed','data':[]}
        cursor.close()
        print("result->",response_data)
    else:
        cursor.close()
        response_data={'message':'follower not exist for channel','data':[]}
        #print("result->",response_data)
    return utils.response("Passed",response_data)

    removeFollower(2,4,connection)