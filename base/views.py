from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.
# rooms = [
 #   {'id': 1, 'name': 'lets learn python!'},
 #   {'id': 2, 'name': 'Design with me'},
 #   {'id': 3, 'name': 'Frontend developer'},] 



def home(request):
    rooms=Room.objects.all()
    context={'rooms': rooms}
    return  render(request, 'base/home.html',context )


def room(request,pk):
    rooms=Room.objects.get(id=pk) 
    # room=None
    # for i in rooms:
     #     if i['id']==int(pk):
      #         room=i
    context={'room': room}
    return  render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context={'form': form}
    return render(request,'base/room_form.html', context)