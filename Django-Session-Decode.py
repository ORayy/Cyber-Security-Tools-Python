#!/usr/bin/python3

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# session key from as seen in browser/django session table
session_key = (input('Paste Session Key here: '))

s = Session.objects.get(pk=f'{session_key}')

# decoding session to get data inside
s.get_decoded()

# extracting users unique id and hash key
uid = s.get_decoded().get('_auth_user_id', '_auth_user_hash')
user = User.objects.get(pk=uid)

print(user.username, user.get_full_name(), user.email)