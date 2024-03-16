from django.db import models

# model Professeur

class Professeurs(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=100)
    date_naiss = models.DateTimeField()
    lien_naiss = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    diplome = models.CharField(max_length=200)

    matieres = models.ManyToManyField('Matieres')
    classes = models.ManyToManyField('Classes', related_name='professeurs_classes')
    eleves = models.ManyToManyField('Eleves', related_name='professeurs_eleves')
    niveau = models.ManyToManyField('Niveau', related_name='professeurs_niveau')

# model niveau

class Niveau(models.Model):
    code_niveau = models.CharField(max_length=30)
    professeur = models.ManyToManyField(Professeurs, related_name='niveau_professeurs')

class Classes(models.Model):
    nom_class = models.CharField(max_length=30)
    professeurs = models.ManyToManyField(Professeurs, related_name='classes_professeurs')
    niveau = models.ForeignKey(Niveau, null=True, on_delete=models.SET_NULL)

class Matieres(models.Model):
    nom_matiere = models.CharField(max_length=100)
    classes = models.ManyToManyField(Classes)

class Eleves(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=200)
    lieu_naiss = models.CharField(max_length=100)
    date_naiss = models.DateTimeField()
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    sexe = models.CharField(max_length=30)

    classes = models.ForeignKey(Classes, null=True, on_delete=models.SET_NULL)
    matiere = models.ManyToManyField(Matieres)
    professeurs = models.ManyToManyField(Professeurs, related_name='eleves_professeurs')
