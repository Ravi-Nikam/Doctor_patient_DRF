from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name,email,phone_number,user_type,password=None,**extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not name:
            raise ValueError('Name is required')
        if not phone_number:
            raise ValueError('Phone Number is required')
        email = self.normalize_email(email)
        user=self.model(
            email=email,
            name=name,
            phone_number=phone_number,
            user_type=user_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,name,email,phone_number,user_type,password=None,**extra_fields):
        user=self.create_user(
            email=email,
            name=name,
            password=password,
            phone_number=phone_number,
            user_type=user_type
        )
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        user.save(using=self._db)
        return user