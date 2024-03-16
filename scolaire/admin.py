from django.contrib import admin
from .models import Eleves
from .models import Classes
from .models import Professeurs
from .models import Matieres
from .models import Niveau




admin.site.register(Eleves)
admin.site.register(Classes)
admin.site.register(Professeurs)
admin.site.register(Matieres)
admin.site.register(Niveau)