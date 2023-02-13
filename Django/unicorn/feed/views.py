from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    username = 'choom'
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
        element = "http://127.0.0.1:8000/profile"
        el_name = 'My profile'
    else:
        element = "http://127.0.0.1:8000/reg"
        el_name = 'Registration'
    return render(request, 'Unicorn.html', context={"username": username, "element": element, "el_name": el_name})


def about(request):
    return HttpResponse('<h1>About unicorn:</h1>'
                        'The Unicorn is a site with AI rendered art, that can be purchased')


def contact(request):
    return HttpResponse('<h1>Contact us:</h1>'
                        'Email: vladislav4ik.sib@gmail.com')


def profile(request):
    user = {'username': 'choom', 'age': 'unknown'}
    if 'username' and 'age' in request.COOKIES:
        user = {'username': request.COOKIES['username'], 'age': request.COOKIES['age']}
    return render(request, 'Profile.html', context=user)



def data(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Path: {path}</p>
    <p>User-agent: {user_agent}</p>
    <br>
    {request.META}
    """)


def catalog(request):
    return HttpResponse('Your shoplist')


def new(request):
    return HttpResponse('New products')


def top(request):
    return HttpResponse('Top products')


def product(request, id):
    return HttpResponse(f'About product {id}:')


def comments(request, id):
    return HttpResponse(f'Comments about product {id}:')


def questions(request, id):
    return HttpResponse(f'Questions about product {id}:')


def set_cookies(request):
    username = request.GET.get('username', 'choom')
    age = request.GET.get('age', 'unknown')
    response = HttpResponse(f'''<p1>Welcome {username}, your age is {age}!</p1>
                            <br>
                            <a href="http://127.0.0.1:8000">back home</a>''')
    response.set_cookie('username', username)
    response.set_cookie('age', age)
    return response


def get_cookies(request):
    username = request.COOKIES['username']
    return HttpResponse(f'You are {username}!')


def registration(request):
    return render(request, 'reg.html')
