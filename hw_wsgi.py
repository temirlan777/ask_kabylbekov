def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html')
    ]
    body = 'Hello, world!<br>'

    body += '<br>Method: ' + environ['REQUEST_METHOD'].upper() + '<br>'

    body += '<br>Params:<br>' + parse_query_string(environ['QUERY_STRING'])

    start_response(status, headers)
    return [ body ]

def parse_query_string(query_string):
    query_string_array = query_string.split('&')
    query_string = ''
    for param in query_string_array:
        query_string += param + '<br>'
    return query_string
