from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('new_user'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('new_user'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware