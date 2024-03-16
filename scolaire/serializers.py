from rest_framework import serializers
from .models import Professeurs
from .models import Eleves
from .models import Classes
from .models import Matieres
from .models import Niveau




class ProfesseurSerializers(serializers.ModelSerializer):

    class Meta:
        model = Professeurs
        fields = ['prenom', 'nom', 'date_naiss', 'lien_naiss', 'adress', 'diplome', 'matieres',
                  'classes', 'eleves', 'niveau']

class ElevesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleves

        fields = ['nom', 'prenom', 'lieu_naiss', 'date_naiss', 'email', 'telephone', 'sexe', 
                  'sexe', 'classes', 'matiere', 'professeurs']
        
class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau

        fields = ['code_niveau', 'professeur']

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matieres

        fields = ['nom_matiere', 'classes']

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes

        fields = ['nom_class', 'professeurs', 'niveau']