from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

from UserInfo.models import Fraternity

class Party(models.Model):
	"""
		Model to represent a party.
	"""

	# NOTE: In the future, this path should be changed to be in protected file space so it is not
	# accessible to the public.

	name = models.CharField(max_length=100)
	date = models.DateField()
	guycount = models.IntegerField(default=0)
	girlcount = models.IntegerField(default=0)
	fraternity = models.ForeignKey(Fraternity)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def isPartyMode(self):
		# Find out if we are in party mode
		closedatetime = datetime(self.date.year, self.date.month, self.date.day, 20)
		return closedatetime < datetime.now()

	#Setup meta info about this model
	class Meta:
		verbose_name_plural = "Parties"
		verbose_name = "Party"
		permissions = (
            ("manage_parties", "Can manage Parties"),
        )

class Guest(models.Model):
	"""
		Model to represent a party guest
	"""
	name = models.CharField(max_length=100, db_index=True)
	birthDate = models.DateField(blank=True,auto_now=True)
	gender = models.CharField(max_length=100)
	cardID = models.CharField(max_length=100, blank=True)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def __iter__(self):
		"""return a ** iterator of field,value"""
		for i in self._meta.get_all_field_names():
			yield (i, getattr(self,i))

	def __cmp__(self,other):
		pass
		#apparently django does not use this during the order_by query

	#Setup meta info about this model
	class Meta:
		verbose_name_plural = "Guests"
		verbose_name = "Guest"

class PartyGuest(models.Model):
	"""
		Model to represent a guest for a specific party.
	"""
	party = models.ForeignKey(Party, related_name="party_for_guest", default=1)
	guest = models.ForeignKey(Guest, related_name="guest", default=1, db_index=True)
	addedBy = models.ForeignKey(User, related_name="added_by", default=1)
	createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
	signedIn = models.BooleanField(default=False)
	everSignedIn = models.BooleanField(default=False)
	timeFirstSignedIn = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.guest.name

	def __str__(self):
		return self.guest.name

	def __iter__(self):
		"""return a ** iterator of field,value"""
		for i in self._meta.get_all_field_names():
			yield (i, getattr(self,i))

	#Setup meta info about this model
	class Meta:
		verbose_name_plural = "Party Guests"
		verbose_name = "Party Guest"

	def toJSON(self):
		data = {}
		data['id'] = self.id
		data['name'] = self.guest.name
		data['addedByName'] = self.addedBy.first_name + " " + self.addedBy.last_name
		data['addedByID'] = self.addedBy.id
		data['signedIn'] = self.signedIn

		return data
