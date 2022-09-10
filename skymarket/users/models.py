from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField


from skymarket.users.managers import UserManager


class UserRoles:
    # TODO закончите enum-класс для пользователя
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (ADMIN, ADMIN)
    )


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    first_name = models.CharField(
        max_length=64,
        verbose_name="имя",
        help_text="введите имя (максимум 64 символа)"
    )

    last_name = models.CharField(
        max_length=64,
        verbose_name="Фамилия",
        help_text="введите имя (максимум 64 символа)"
    )

    email = models.CharField(
        "email address",
        unique=True,
        help_text="укажите электроную почту"
    )

    phone = PhoneNumberField(
        verbose_name="телефон для связи",
        help_text="укажите телефон для связи"
    )

    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль"
    )

    is_active = models.CharField(
        verbose_name="аккаунт активен",
        help_text="укажите активен ли аккаунт"
    )

    image = models.CharField(
        upload_to='users_avatars/',
        verbose_name="Аватарка",
        help_text="выберете свой аватар"
    )

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, opp_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.USER

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ('id',)
