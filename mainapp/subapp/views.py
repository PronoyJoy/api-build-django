from django.shortcuts import render
from .serializers import PersonSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person,Region

from rest_framework.viewsets import ModelViewSet

@api_view(['GET','POST'])
def index(request):
    courses = {
            'course' : 'Python',
            'website': 'Udemy'
        }

    if request.method == 'GET':
        return Response(f'GeT it Bro -{courses}')
      

    elif request.method == 'POST':
        data = request.data

        return Response(f'Post it Bro -{courses} and You Got it Too {data}')
    



#crud using apiview

@api_view(['GET','POST','PUT','PATCH','DELETE']) #patch partial update
def person_crud(request):

    if request.method == 'GET':
        person_list = Person.objects.filter(country__isnull = False)
        serializer = PersonSerializer(person_list, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        person_id =  Person.objects.get(name = data['name']) 
        serializer = PersonSerializer(person_id,data=data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT': #no partial sob field lagbe
        data = request.data
        
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        person_id = Person.objects.get(name = data['name'])
        person_id.delete()

        return Response('Person Deleted')









class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

       

   