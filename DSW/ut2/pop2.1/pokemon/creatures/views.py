from django.shortcuts import render

from .models import Creature

# Create your views here.


def creatures_list(request):
    creatures = Creature.objects.all()
    return render(request, 'creatures/creature/list.html', {'creatures': creatures})


def creature_detail(request, creature_slug):
    creature = Creature.objects.get(slug=creature_slug)
    return render(request, 'creatures/creature/detail.html', {'creature': creature})
