from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse('<h1>Hello from the VFXRemote App!</h1>')

def details(request, choreList_id):
  return HttpResponse("This is the Chore List #%s." % (choreList_id))

def chores(request, choreList_id):
  return HttpResponse("This is the Chores of the list : #%s." % (choreList_id))

def choreDetails(request, choreList_id, chore_id):
  return HttpResponse("This is the Chore %s of the chore list : #%s." % (chore_id, choreList_id))

