from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self,email,password,**extra_fields ):

        if not email: 
            raise ValueError('User must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        user=self.create_user(
            email,
            password=password,**extra_fields,

        )
        user.is_admin=True
        user.save(using=self._db)
        return user
       