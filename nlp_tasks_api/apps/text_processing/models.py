from django.db import models

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Documento(CommonInfo):
    file = models.FileField(upload_to='documentos')

    def __str__(self):
        return "[{}] {}".format(self.created_at, str(self.file))
