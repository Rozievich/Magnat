from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    phone_validator = RegexValidator(
        regex=r'^\+998[123456789]\d{8}$',
        message='Telefon raqamingizni to\'g\'ri kiriting, masalan: +998901234567',
        code='invalid_phone_number'
    )
    try:
        phone_validator(value)
    except ValidationError as e:
        raise ValidationError(e.messages)


class Client(models.Model):
    class RateChoice(models.IntegerChoices):
        INS = 1, "Kutishda"
        OLM = 2, "Olmadi",
        TIK = 3, "Rad etilgan"
        YOU = 4, "Qo'ng'iroq qilingan"
        BOSH = 5, "Boshqa"
    ism = models.CharField(max_length=80)
    tel_nomer = models.CharField(max_length=13, validators=[
                                 validate_phone_number])
    tex_zadacha = models.FileField(
        upload_to="user_texzadacha", blank=True, null=True)
    status = models.PositiveIntegerField(
        choices=RateChoice.choices, default=RateChoice.INS)
    sabab = models.CharField(max_length=128, blank=True, null=True)
    sana = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_status_display_text(self):
        return dict(self.RateChoice.choices)[self.status]

    class Meta:
        ordering = ["-created_at", "-update_at"]

    def __str__(self) -> str:
        return self.ism


class MediaCategory(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Media(models.Model):
    media = models.FileField(upload_to="portfolio/", blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-update_at"]

    def __str__(self) -> str:
        return self.title

    def clean(self):
        if not self.media and not self.youtube_url:
            raise ValidationError(
                _("Siz yana media yoki YouTube URL kiritishingiz kerak"))
        elif self.media and self.youtube_url:
            raise ValidationError(
                _("Siz faqatgina media yoki faqatgina YouTube URL kiritishingiz mumkin"))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Worker(models.Model):
    class RateChoice(models.IntegerChoices):
        INS = 1, "SMM"
        OLM = 2, "Director"
        TIK = 3, "Programmer"
        YOU = 4, "Project Manager"
        BOS = 5, "Graphic Designer"
    picture = models.FileField(upload_to="worker/")
    name = models.CharField(max_length=80)
    familiya = models.CharField(max_length=80, blank=True, null=True)
    sohasi = models.PositiveIntegerField(
        choices=RateChoice.choices, default=RateChoice.TIK)
    created_at = models.DateTimeField(auto_now=True)

    def get_status_display_text(self):
        return dict(self.RateChoice.choices)[self.sohasi]

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    ism = models.CharField(max_length=80)
    summary = models.CharField(max_length=400)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.summary
