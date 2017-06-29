from django.db import models

# Create your models here.

class Person(models.Model):
    SHIRT_SIZES = (('S', 'Small'), ('M', 'Medium'), ('L', 'Large'),)
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name

class Perfil(models.Model):
    name = models.CharField(max_length=64)
    friends = models.ManyToManyField("self")

class Manufacter(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacter = models.ForeignKey(Manufacter, on_delete=models.CASCADE, related_name="cars")

class Cobertura(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    coberturas = models.ManyToManyField(Cobertura)

class CPF(models.Model):
    numero = models.CharField(max_length = 9)

    def calcular_dv(self):
        return '00'

    def __str__(self):
        return self.numero + '-' + self.calcular_dv()

class PessoaFisica(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.OneToOneField(CPF, related_name = 'pessoa_fisica')

    def __str__(self):
        return self.nome

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'person'))

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    inviter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="membership_invites", null=True)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Blog(models.Model):
    name = models.CharField(max_length=50)

class Entry(models.Model):
    headline = models.CharField(max_length=60)
    body_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="posts")
