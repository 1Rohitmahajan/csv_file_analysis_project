from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from allmembers.models import New_User

class Signup(View):
    return_url = None

    def get(self, request):

        return render(request, 'authenticate/signup.html') 

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        user = New_User(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)
        error_message = self.validateCustomer(user)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            user.password = make_password(user.password)
            user.register()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'anthenticate/signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 characters long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 characters long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 characters long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 characters long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 characters long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        return error_message

class Loginuser(View):
    return_url = None

    def get(self, request):
        Loginuser.return_url = request.GET.get('return_url')
        return render(request, 'authenticate/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = New_User.get_newuser_by_email(email)
        error_message = None
        if user:
            flag = check_password(password, user.password)
            if flag:
                request.session['new_user'] = user.id

                if Loginuser.return_url:
                    return HttpResponseRedirect(Loginuser.return_url)
                else:
                    Loginuser.return_url = None
                    return redirect('index')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'authenticate/login.html', {'error': error_message})

def logoutuser(request):
    request.session.clear()
    return redirect('index')
