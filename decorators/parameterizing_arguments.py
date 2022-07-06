def post_only(f):  # The request.method must be 'POST'. If not, @post_only will solve this issue
    """ Ensures a method is post only """
    def wrapped_f(request):
        if request.method != "POST":
            response = HttpResponse(json.dumps(
                {"error": "this method only accepts posts!"}))
            response.status_code = 500
            return response  # The Problem is solved
        return f(request)  # We are using f() function if there is no problem with request.method
    return wrapped_f

# If there was no 'POST' error then we are able go next
def json_response(f):  # creating a json_response
    """ Return the response as json, and return a 500 error code if an error exists """
    def wrapped(*args, **kwargs):
        result = f(*args, **kwargs)
        response = HttpResponse(json.dumps(result))
        if type(result) == dict and 'error' in result:
            response.status_code = 500
        return response
    return wrapped

def parameterize_request(types=("POST",)):
    """
    Parameterize the request instead of parsing the request directly.
    Only the types specified will be added to the query parameters.

    e.g. convert a=test&b=cv in request.POST to
    f(a=test, b=cv)
    """
    def wrapper(f):
        def wrapped(request):
            kw = {}
            if "GET" in types:
                for k, v in request.GET.items():
                    kw[k] = v
            if "POST" in types:
                for k, v in request.POST.items():
                    kw[k] = v
            return f(request, **kw)
        return wrapped
    return wrapper


@post_only  # solving 'POST' issue
@json_response  # creating a response using the dict returned by function below
@parameterize_request(["POST"])  # parameterized the arguments
def register(request, username, email, password,
             first_name=None, last_name=None):
    user = User.objects.create_user(username, email, password)
    user.first_name=first_name
    user.last_name=last_name
    user.save()
    return {"success": True}