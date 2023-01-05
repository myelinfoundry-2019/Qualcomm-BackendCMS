import utils

def testFunction(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT first_name,last_name FROM users")
    
    extracted_data = cursor.fetchall()
    
    result=[]
    fields=['first_name','last_name']
    
    for row in extracted_data:
        response_data=dict(zip(fields,row))
        result.append(response_data)
        
    response_data={'message':'final results',
                        'data':result}

    cursor.close()

    #return http response 
    return utils.response("Passed",response_data)