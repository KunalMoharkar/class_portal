from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Question
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import Userform

curr_que = [1]*5
status = ['']*5
id = 0


def homepage(request):
    all_que = Question.objects.all
    global id
    id = int(id)
    context={'all_que': all_que, 'status': status, 'curr_que': curr_que, 'id': id }
    return render(request, 'quiz/home.html', context)


def details(request, que_id):
    global curr_que
    curr_que[int(que_id)] = 0
    global id
    id = int(que_id)
    selected_que = Question.objects.get(pk=que_id)
    context = {'selected_que': selected_que}
    return render(request, 'quiz/detail.html', context)


def check(request, que_id):

    answered_que = request.POST['ans']
    selected_que = Question.objects.get(pk=que_id)

    if request.method == 'POST' :
        global status
        status[int(que_id)] = "solved"


    context = {'answered_que': answered_que, 'selected_que': selected_que}
    return render(request, 'quiz/detail.html', context)


class UserFormView(View):
    form_class = Userform
    template_name = 'quiz/user_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:

                    login(request, user)
                    return redirect('quiz:homepage')




def userlogin(request):


    if request.method == "GET":
        return render(request,'quiz/login.html')


    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:

                login(request, user)
                return redirect('quiz:homepage')


def userlogout(request):
    logout(request)
    return redirect('quiz:login')












