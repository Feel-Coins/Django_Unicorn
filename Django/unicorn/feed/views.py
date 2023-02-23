from django.shortcuts import render
from django.http import HttpResponse


def data(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>User-agent: {user_agent}</p>
    <br>
    {request.META}
    """)


def context(request):
    username = 'choom'
    age = 'unknown'
    cities = 'no location'
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
        age = request.COOKIES['age']
        cities = request.COOKIES['cities']
        element = "http://127.0.0.1:8000/profile"
        el_name = 'My profile'
    else:
        element = "http://127.0.0.1:8000/reg"
        el_name = 'Registration'
    return {"username": username, "element": element, "el_name": el_name, "age": age, "cities": cities}


def index(request):
    return render(request, 'unicorn.html', context=context(request))


def about(request):

    return render(request, 'about.html', context=context(request))


def contact(request):
    return render(request, 'contacts.html', context=context(request))


def registration(request):
    return render(request, 'reg.html')


def profile(request):
    return render(request, 'profile.html', context=context(request))


def catalog(request):
    return render(request, 'catalog.html', context=context(request))


def new(request):
    return render(request, 'new_prods.html', context=context(request))


def top(request):
    return render(request, 'top_prods.html', context=context(request))


def product(request, id):
    return HttpResponse(f'About product {id}:')


def comments(request, id):
    return HttpResponse(f'Comments about product {id}:')


def questions(request, id):
    return HttpResponse(f'Questions about product {id}:')


def set_cookies(request):
    username = request.GET.get('username', 'choom')
    age = request.GET.get('age', 'unknown')
    cities = request.GET.getlist('cities', 'no location')
    response = HttpResponse(f'''<p1>Welcome {username}, your age is {age} and your cities is {cities}</p1>
                            <br>
                            <a href="http://127.0.0.1:8000">back home</a>''')
    response.set_cookie('username', username)
    response.set_cookie('age', age)
    response.set_cookie('cities', cities)
    return response


def get_cookies(request):
    username = request.COOKIES['username']
    age = request.COOKIES['age']
    cities = request.COOKIES['cities']
    return HttpResponse(f'You are {username}!'
                        f'Your age is {age}'
                        f'Your cities is {cities}')
