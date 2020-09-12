import json
import os
from pprint import pprint
from dotenv import load_dotenv
import telegram


load_dotenv()
CHAT_ID = os.getenv('CHAT_ID')


def index (environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/html')]
	start_response(status, headers)

	with open('index.html', 'rb') as f:
		response = f.read()

	return [response]


def send_message(environ, start_response):
	method = environ['REQUEST_METHOD'].upper()
	if method != 'POST':
		return resp_404(environ, start_response)

	status = '200 OK'
	headers = [('Content-type', 'application/json')]
	start_response(status, headers)

	body_len = int(environ.get('CONTENT_LENGTH', 0))
	body = environ['wsgi.input'].read(body_len).decode('utf-8')

	data = json.loads(body)
	pprint(data)
	text = data['text']

	client = telegram.TelegramBotClient()
	client.call_method('sendMessage', {'chat_id': CHAT_ID, 'text': text})

	response = '{"status": "ok"}'.encode()
	return [response]


def resp_404(environ, start_response):
	start_response('404 Not Found', [])

	return []
