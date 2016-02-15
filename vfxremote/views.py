from django.shortcuts import get_object_or_404, render


from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import ChoreList, Chore

# Create your views here.
def index(request):
  lists = ChoreList.objects.all()
  return render(request, 'vfxremote/index.html', {'chorelists' : lists})

def details(request, chorelist_id):
  list = get_object_or_404(ChoreList, pk=chorelist_id)
  return render(request, 'vfxremote/detail.html', {'chorelist' : list})


def choreDetails(request, chorelist_id, chore_id):
  list = get_object_or_404(ChoreList, pk=chorelist_id)
  chore = get_object_or_404(Chore, pk=chore_id)
  return render(request, 'vfxremote/choredetail.html', {'chorelist' : list, 'chore' : chore})

def updatechore(request, chorelist_id, chore_id):
  chore = get_object_or_404(Chore, pk=chore_id)
  if 'complete' in request.POST:
    chore.complete = True
  else:
    chore.complete = False
  chore.save()
  return HttpResponseRedirect('/vfxremote/' + chorelist_id + '/chores/' + chore_id)

def newlist(request):
  if request.POST:
    list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
    list.save()
    return HttpResponseRedirect('/vfxremote')
  else:
    return render(request, 'vfxremote/newlist.html', {})