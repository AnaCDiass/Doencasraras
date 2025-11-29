from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    laudo = models.FileField(upload_to='laudos/')
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome_completo


class Profile(models.Model):
    TIPOS_USUARIO = (
        (0, "Administrador"),
        (1, "Paciente"),
        (2, "Usuário"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPOS_USUARIO, default=2)

    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_usuario_display()}"

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def criar_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def salvar_profile(sender, instance, **kwargs):
        instance.profile.save()