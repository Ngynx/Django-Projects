from django.db import models

class user(models.Model):
	id = models.AutoField(primary_key=True)
	login = models.CharField(max_length=255, help_text='Escriba su nombre de usuario')
	email = models.EmailField(max_length=255, blank=False, null=False, help_text='Escriba su email verdadero')
	password = models.CharField(max_length=255, blank=False, null=False)

	class Meta:
	    verbose_name='user'
	    verbose_name_plural = 'users'
	    ordering = ['email']

	def __str__(self):
	    return self.email


class followers(models.Model):
	followerId = models.BigIntegerField(blank=False, null=False)
	followedId = models.BigIntegerField(blank=False, null=False)


class  user_status_updates(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=False, null=False)
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	body = models.TextField(null=False, blank=False, help_text='Escriba la descripción del Estado')
	date = models.DateField(help_text='Escriba la fecha de modificacion')


class hastag(models.Model):
	id = models.BigIntegerField(primary_key=True)
	hastag= models.CharField(max_length=20, help_text='Escriba su hashtag, debe contener menos de 20 caracteres')

	def __srt__(self):
	    return self.hastag


class user_status_updates_hastags(models.Model):
	hastag_id = models.ForeignKey(hastag, on_delete=models.CASCADE)
	user_status_updates_id = models.ForeignKey(user_status_updates, on_delete=models.CASCADE)

class user_status_update_comments(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=False, null=False)
	body = models.TextField(null=False, help_text='Escriba su comentorio')
	date = models.DateField(help_text='Fecha de la seccion de comentarios', blank=False, null=False)
	user_id = models.ForeignKey(user, on_delete = models.CASCADE)
	user_status_update_id = models.ForeignKey(user_status_updates, on_delete = models.CASCADE)

	def __str__(self):
	    return self.body


