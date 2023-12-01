from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('''
                        <h1>This is courses page</h1>
                        <a href='/second_app/courses/'>Courses </a>
                        <a href='/first_app/contact/'> contact </a> 
                        <a href='/first_app/about/'> About </a> 
                        '''
                        )

def feedback(request):
    return HttpResponse('''
                         <h1>This is courses page</h1>
                        <a href='/second_app/feedback/'>feedback </a>
                        <a href='/first_app/contact/'> contact </a> 
                        <a href='/first_app/about/'> About </a> 
                        ''')