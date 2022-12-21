import utils
import time
        
def channelAdd(decodedBody,connection):
    print("Received channelAdd request")
    
    cursor = connection.cursor()  # get the cursor object
    
    channel_name = decodedBody["channel_name"]
    channel_Description = decodedBody["channel_Description"]
    channel_profile_pic = decodedBody["channel_profile_pic"]
    created_at = decodedBody["created_at"]
    channel_user_id = decodedBody["channel_user_id"]
    sql="""SELECT EXISTS(SELECT * FROM channel WHERE channel_name = %s)"""
    cursor.execute(sql,(channel_name,))
    extracted_data = cursor.fetchone()
    
    if extracted_data[0]==0:
        sql = "INSERT INTO channel (channel_name,channel_Description,channel_profile_pic,created_at,channel_user_id) VALUES (%s,%s,%s,%s,%s)"
        val = (channel_name,channel_Description,channel_profile_pic,created_at,channel_user_id)
        cursor.execute(sql,val)
        connection.commit()
    
    else :
        
        cursor.close()
        
        response_data={'message':'channel name already exist',
                        'data':[]}
        
        #return http response 
        return utils.response("Failed",response_data)
    
    
    sql="""SELECT id,channel_name,channel_Description,channel_profile_pic,created_at,channel_user_id FROM channel WHERE channel_name = %s"""
    cursor.execute(sql,(channel_name,))
    extracted_data = cursor.fetchall()
    
    result = []
    fields = ['channel_id','channel_name', 'channel_description', 'channel_profile_pic','created_at','channel_user_id']
    result = dict(zip(fields,extracted_data[0]))
    
    channel_id=result['channel_id']
    
    sql = "INSERT INTO videos (channel_id) VALUES (%s)"
    val = (channel_id)
    cursor.execute(sql,val)
    
    sql = "INSERT INTO subscribers (channel_id) VALUES (%s)"
    val = (channel_id)
    cursor.execute(sql,val)
    
    cursor.close()
    
    #return http response 
    return utils.response("Passed",response_data) 

