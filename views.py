import os
import json

from dotenv import load_dotenv

from telegram import TelegramBotClient

load_dotenv()
CHAT_ID = os.getenv('CHAT_ID')
TG_CLIENT = TelegramBotClient()

def index (environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/html')]
	start_response(status, headers)

	with open('index.html', 'rb') as f:
		response = f.read()

	return [response]

def index_js (environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/javascript')]
	start_response(status, headers)

	with open('index.js', 'rb') as f:
		response = f.read()
		
	return [response]

def send_message (environ, start_response):
	if environ['REQUEST_METHOD'].upper() != 'POST':
		return resp_404(environ, start_response)

	body_len = int(environ.get('CONTENT_LENGTH', 0))
	body = environ['wsgi.input'].read(body_len).decode('utf-8')
	data = json.loads(body)

	TG_CLIENT.call_method('sendMessage', {'chat_id': CHAT_ID, 'text': data['message']})

	status = '200 OK'
	headers = [('Content-type', 'application/json')]
	start_response(status, headers)

	response = {'status': 'ok'}

	ret = [json.dumps(response).encode('utf-8')]
	return ret

def resp_404 (environ, start_response):
	start_response('404 Not Found', [])

	return []