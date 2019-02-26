from bottle import route, run, response, request, redirect


login_user = {} # 用来存储登录状态的字典

@route('/login')
def login():
    key = hash("test password")
    login_user[key] = "test password"
    response.set_cookie('login', str(key))
    return 'login successfully!'

@route('/logout')
def logout():
    key = request.get_cookie('login')
    login_user.pop(int(key), None)
    return 'logout successfully!'

@route('/logintest')
def logintest():
    key = request.get_cookie('login')
    if key is not None and int(key) in login_user:
        return 'login test successfully!'
    else:
        return redirect('/beforelogin')

@route('/beforelogin')
def beforelogin():
    return 'please login!'

run(host='localhost', port=8082, debug=True)