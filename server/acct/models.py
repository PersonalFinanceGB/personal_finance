from django.db import models
from users.models import User


class Type_acct(models.Model):
	type_acct = models.CharField(max_length=128)

	def __str__(self):
		return self.type_acct


class User_acct(models.Model):
	
	id_user = models.ForeignKey(
		User, on_delete=models.CASCADE,
		default=None,
	)
	id_acct = models.ForeignKey(
		Type_acct, on_delete=models.CASCADE,
		default=None,
	)
	sum = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		default=0,
	)

