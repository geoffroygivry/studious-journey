from django.shortcuts import get_object_or_404, render


from django.http import HttpResponse, Http404
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

