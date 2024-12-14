from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .froms import RommForm


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Python'},
#     {'id': 2, 'name': 'Design With me'},
#     {'id': 3, 'name': 'FrontEnd Developers'},
# ]

def home(request):
    rooms = Room.objects.all()
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id = pk)
    context =  {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RommForm()
    if request.method == 'POST':
        form = RommForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RommForm(instance=room)
    if request.method == 'POST':
        form = RommForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request, 'base/delete.html', context)