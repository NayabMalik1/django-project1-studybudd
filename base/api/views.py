from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer



@api_view(['GET'])  # ✅ list with square brackets
def getRoute(request):
    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)



@api_view(['GET'])  # This is a list with a string inside
def getRooms(request):
    rooms=Room.objects.all()
    serializer=RoomSerializer(rooms, many=True)
    return Response(serializer.data)




@api_view(['GET'])  # This is a list with a string inside
def getRoom(request, pk):
    rooms=Room.objects.get(id=pk)
    serializer=RoomSerializer(rooms, many=False)
    return Response(serializer.data)


