from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def menu(request):
    return render(request, 'student/menu.html', {})


def signin(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You are Logged out")
        return signin(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_superuser == 0:
            login(request, user)
            return menu(request)

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'signin.html', {})


@login_required
def profile(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.get(username=request.user.username)
            user.set_password(request.POST['password1'])
            user.save()
            messages.success(request, "Password updated.\n Log in again with new password")
            return render(request, 'signin.html', {})
    user = Student.objects.get(roll_num=request.user.id)
    context = {'roll_num': user.roll_num, 'name':str(user.first_name) + ' ' + str(user.last_name), 'mail':user.mail, 'student_contact_num':user.student_contact_num, 'guardian_contact_num':user.guardian_contact_num, 'room':user.room}
    print(context)
    return render(request, 'student/profile.html', context)





@login_required
def roomChangeRequest(request):

    if request.method == 'POST':
        reason = ChangeRoom()
        reason.reason = request.POST['reason']
        reason.student = Student.objects.get(roll_num=request.user.id)
        reason.save()
        messages.success(request, "Request submitted succesfully.")

    return render(request, 'student/room_change_request.html', {})


@login_required
def feedback(request):

    if request.method == 'POST':
        feedback = Feedback()
        feedback.feedback = request.POST['feedback']
        feedback.hostel = Student.objects.get(roll_num=request.user.id).room.hostel
        feedback.save()
        messages.success(request, "Feedback submitted succesfully.")

    return render(request, 'student/feedback.html', {})


@login_required
def complaint(request):

    if request.method == 'POST':
        complaint = Complaint()
        complaint.complaint = request.POST['complaint']
        complaint.student = Student.objects.get(roll_num=request.user.id)
        complaint.save()
        messages.success(request, "Complaint registered succesfully.")

    return render(request, 'student/complaint.html', {})

