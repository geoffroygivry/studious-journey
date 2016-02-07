from django.shortcuts import render


from django.http import HttpResponse
from .models import ChoreList

# Create your views here.
def index(request):
  lists = ChoreList.objects.all()
  return render(request, 'vfxremote/index.html', {'chorelists' : lists})

def details(request, chorelist_id):
  list = ChoreList.objects.get(pk=chorelist_id)
  return render(request, 'vfxremote/detail.html', {'chorelist' : list})

def chores(request, chorelist_id):
  return HttpResponse("This is the Chores of the list : #%s." % (chorelist_id))

def choreDetails(request, chorelist_id, chore_id):
  return HttpResponse("This is the Chore %s of the chore list : #%s." % (chore_id, chorelist_id))

