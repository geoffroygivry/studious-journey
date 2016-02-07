from django.shortcuts import render


from django.http import HttpResponse
from .models import ChoreList
from django.template import loader, RequestContext

# Create your views here.
def index(request):
  lists = ChoreList.objects.all()
  template = loader.get_template('vfxremote/index.html')
  context = RequestContext(request, {
      'chorelists' : lists,
    })
  return HttpResponse(template.render(context))

def details(request, choreList_id):
  return HttpResponse("This is the Chore List #%s." % (choreList_id))

def chores(request, choreList_id):
  return HttpResponse("This is the Chores of the list : #%s." % (choreList_id))

def choreDetails(request, choreList_id, chore_id):
  return HttpResponse("This is the Chore %s of the chore list : #%s." % (chore_id, choreList_id))

