from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, full_name, password):
        if not email:
            raise ValueError('Users must have email')
        if not full_name:
            raise ValueError('Users must have full_name')

        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
