import uuid
import hashlib


def hash_password(username, password):
	hashboy = hashlib.new('sha512')
	salt = username[::-1]
	combined = salt + password
	hashboy.update(combined.encode('utf-8'))
	password_hash = hashboy.hexdigest()
	print (salt, password_hash)
	return (salt, password_hash)