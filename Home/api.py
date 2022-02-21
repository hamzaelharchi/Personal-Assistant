
#views
from .models import Task, Chat
from .serializer import  TaskSerializer, ChatSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

'''
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

'''
'''
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
'''


@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	print(serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		print(serializer.data)

	return Response('hi hi hi')

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')





@api_view(['POST', 'GET'])
def chatCreate(request):
	serializer = ChatSerializer(data=request.data)
	
	if serializer.is_valid():
		serializer.save()

		print(serializer.data)
	
	return Response(serializer.data)


@api_view(['GET'])
def chatList(request):
	chat = Chat.objects.all().order_by('-id')
	serializer = ChatSerializer(chat, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def chatDetail(request, pk):
	chat = Chat.objects.get(id=pk)
	serializer = ChatSerializer(chat, many=False)
	return Response(serializer.data)

'''
@api_view(['POST', 'GET'])
def chatCreate(request):
	serializer = ChatSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
	'''