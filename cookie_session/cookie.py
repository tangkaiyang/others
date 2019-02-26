from bottle import route, run, response, request


@route('/hello')
def hello():
    count = request.get_cookie('visited')
    if count:
        increment = int(count) + 1
        response.set_cookie("visited", str(increment))
        return str(increment)
    else:
        response.set_cookie("visited", '0')
        return "Hello, World"

run(host="localhost", port=8081, debug=True)