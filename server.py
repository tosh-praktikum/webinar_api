from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

import views

ROUTING = {
	"/":         views.index,
	"/send":     views.send_message,
	"/index.js": views.index_js,
}

def simple_app(environ, start_response): # must return list of byte-strings (unicode_string.encode())
	setup_testing_defaults(environ)
	
	# environ['QUERY_STRING'] - query string of HTTP request
	# environ['CONTENT_LENGTH'] - length of body of HTTP request (in bytes)
	# environ['wsgi.input'] - body of HTTP request
	# environ['REQUEST_METHOD'] - method of HTTP request
	# environ['PATH_INFO'] - URL path of HTTP request
	# environ['REMOTE_ADDR'] - IP address of user which sent the request

	print(f"Received request for path {environ['PATH_INFO']}")
	path = environ['PATH_INFO']
	view_func = ROUTING.get(path)

	if view_func:
		return view_func(environ, start_response)

	return views.resp_404(environ, start_response)

if __name__ == "__main__":
	port = 8000
	httpd = make_server('', port, simple_app)
	print("Serving on port {0}...".format(port))
	httpd.serve_forever()