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


@post_only  # solving 'POST' issue
@json_response  # creating a response using the dict returned by function below
def register(request):
    try:
        user = User.objects.create_user(request.POST['username'],
                                        request.POST['email'],
                                        request.POST['password'])
        # optional fields
        for field in ['first_name', 'last_name']:
            if field in request.POST:
                setattr(user, field, request.POST[field])
        user.save()
        return {"success": True}
    except KeyError as e:
        return {"error": str(e) }