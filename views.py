def index (environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/html')]
	start_response(status, headers)

	with open('index.html', 'rb') as f:
		response = f.read()

	return [response]

def resp_404 (environ, start_response):
	start_response('404 Not Found', [])

	return []