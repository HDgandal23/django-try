from django.http import JsonResponse
from .models import Professeurs
from .models import Eleves
from .models import Classes
from .models import Niveau
from .models import Matieres
from .serializers import ProfesseurSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST



# CRUD pour la section professeur

@api_view(['GET', 'POST'])
def list_prof(request, format=None):

    if request.method == 'GET':
        #get all data
        prof = Professeurs.objects.all()
        #serialize them
        serializer = ProfesseurSerializers(prof, many= True)
        #return json
        return JsonResponse(serializer.data, safe=False )
    
    if request.method == 'POST':

        serialize =  ProfesseurSerializers(data = request.data)
        
        if serialize.is_valid():
            serialize.save()

            return Response(serialize.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def details_prof(request, id, format=None):

    try:
        profs = Professeurs.objects.get(pk=id)
    except:
        return Response(status = HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serialize = ProfesseurSerializers(profs)
        return Response(serialize.data, safe= False)
    
    elif request.method == 'PUT':
        serialize =   ProfesseurSerializers(profs, data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status = HTTP_201_CREATED)
        
# CRUD Eleve
