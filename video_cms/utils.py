import mysql.connector
import json


def response(status,response_data={}):
    response_data_final = {'status' : status}
    response_data_final.update(response_data)
    responseObject={}
    responseObject['statusCode']=200
    responseObject['headers']={}
    responseObject['headers']['Content-Type']="application/json"
    responseObject['body']=json.dumps(response_data_final,default = str)
    return responseObject
