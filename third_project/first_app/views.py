from django.shortcuts import render

def contact(request):
    courses = [
        {'id': 1, 'course_name': 'Introduction to Django', 'teacher_name': 'John Doe'},
        {'id': 2, 'course_name': 'Django Models', 'teacher_name': 'Jane Smith'},
        {'id': 3, 'course_name': 'Django Views', 'teacher_name': 'Alex Johnson'},
        {'id': 4, 'course_name': 'Django Template', 'teacher_name': 'Alex Johnson'},
        {'id': 5, 'course_name': 'Django Forms', 'teacher_name': 'Emily White'},
        {'id': 6, 'course_name': 'Django Admin', 'teacher_name': 'David Brown'},
        {'id': 7, 'course_name': 'RESTful APIs with Django', 'teacher_name': 'Sophia Miller'},
        {'id': 8, 'course_name': 'Django Middleware', 'teacher_name': 'Ethan Davis'},
        {'id': 9, 'course_name': 'Testing in Django', 'teacher_name': 'Olivia Wilson'},
        {'id': 10, 'course_name': 'Django Security Best Practices', 'teacher_name': 'Samuel Thomas'},
        {'id': 11, 'course_name': 'Django Deployment', 'teacher_name': 'Emma Anderson'},
        {'id': 12, 'course_name': 'Django Performance Optimization', 'teacher_name': 'Nathan Clark'},
    ]

    context = {
        'topic': 'Django',
        'author': 'MD. Nur Hasan',
        'courses': courses,
        'age': 17,
    }

    return render(request, 'first_app/index.html', context)
