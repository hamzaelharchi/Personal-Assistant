#views
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def user_list_api(request):
    all_users= User.objects.all()
    data=UserSerializer(all_users, many=True).data
    return Response({'data':data})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_detail_api(request, id):
    user_detail=User.objects.get(id=id)
    data=UserSerializer(user_detail).data
    return Response({'data':data})