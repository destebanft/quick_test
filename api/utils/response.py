from rest_framework.response import Response
from rest_framework import status

def error_handler(func):
	def wrapper(*args, **kwargs):
		try:
			response = func(*args, **kwargs)
			if isinstance(response, ResponseSuccess):
				response_body = response.body
				response_status = response.status
			elif isinstance(response, ResponseError):
				if isinstance(response.cause, str):
					response_body = {
						'error': response.cause
					}
				else:
					response_body = {
						'validation': response.cause
					}
				response_status = response.status
			else:
				return response
		except Exception as exception:
			response_body = {
				'error': str(exception)
			}
			response_status = 500
		return Response(response_body, response_status)
	return wrapper

class ResponseSuccess:
	def __init__(self, body, status=status.HTTP_200_OK):
		self.body = body if body is not None else ""
		self.status = status

class ResponseError:
	def __init__(self, cause, status=status.HTTP_400_BAD_REQUEST):
		self.cause = cause if cause is not None else "unknown_error"
		self.status = status