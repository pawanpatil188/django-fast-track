from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>My Django Task Manager</h1>
        <p>Welcome! My first Django page is working.</p>
    """)