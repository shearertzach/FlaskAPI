from flask import make_response

def returnResponse(type, message = '', data = ''):
  response = make_response()
  response.status_code = 200 if type == 'OK' else 400
  response.set_data(data)

  return response