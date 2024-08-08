from django.db import models
from django. contrib.auth.modells import(
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
class UsuarioManager(BaseUserManager):
    def create_user(self, email,password = none):
        usuario = self.model(
            email = self.normalize_email(email),
         )
        
         usuario.is_active = True
         usuario.is_staff = False
         usuario.is_superuser = False
         
         if password:
             usuario.set_password(password)
             
        usuario.save()
        return usuario
    
    def create_superuser(self, email,password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password,
         )
        
         usuario.is_active = True
         usuario.is_staff = False
         usuario.is_superuser = False
         
         
         usuario.set_password(password)
             
        usuario.save()
        return usuario
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models. EmailField(
        verbose_name = "E-mail do usuário",
        max_length =100,
        unique=True,
    )
    is_active = models.BooleanFied(
        verbose_name ="Usuário está ativo",
        default=True,
    )
    is_staff = models.BooleanFied(
        verbose_name ="Usuário é da equipe",
        default=False,
    )
    is_superuser = models.BooleanFied(
        verbose_name ="Usuário administrador",
        default = False,
    )
    
    objects = UsuarioManager()
    
    USERNAME_FIELD ="email"
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"
        
        def_str_(self):
            return self.email
        