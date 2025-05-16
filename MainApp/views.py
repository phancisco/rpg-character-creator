from django.shortcuts import render
from MainApp.models import Character, Weapon
from MainApp.forms import CharacterForm, WeaponForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    Characters = Character.objects.all().order_by('-created_at')
    context = {
        'Characters': Characters,
    }
    return render(request, 'index.html', context)

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    context = {
        'character': character,
    }
    return render(request, 'character_selected.html', context)

def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CharacterForm()
    return render(request, 'character_creator.html', {'form': form})

def weapon_create(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WeaponForm()
    return render(request, 'weapon_creator.html', {'form': form})

def weapon_list(request):
    weapons = Weapon.objects.all()
    context = {
        'Weapons': weapons
    }
    return render(request, 'weapon_list.html', context)