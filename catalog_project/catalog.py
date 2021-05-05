import os
from shutil import copyfile

directories={
	'audio': [
		'rough',
		'ddp',
		'wav',
		],
	'art': [
		'lookbook',
		'draft',
		'assets',
		'final',
		],
	'info': [
		'photos',
		'press',
		]
	}

catalog_number = input("catalog number : ").replace(" ", "_")
artist_name = input("artist_name : ").replace(" ", "_")
catalog_name = input("catalog name : ").replace(" ", "_")

if artist_name:
	root = f"{catalog_number}_{artist_name}_{catalog_name}"
else:
	root = f"{catalog_number}_{catalog_name}"

""" Make root directory. """
os.mkdir(root)

for directory in directories:
	path = os.path.join(root, directory)
	# os.mkdir(path)
	for subdir in directories[directory]:
		path = os.path.join(root, directory, subdir)
		os.makedirs(path)

templates={
	'1': '12inch.psd',
	'2': '7inch.pdf',
	'3': 'digipack.pdf',
	'4': 'cassette.pdf',
	'psd': 'cover.psd',
}

print("12in...........[1]")
print("7in............[2]")
print("CD.............[3]")
print("Cass...........[4]")

options = input("Select options [seperate with space] : ")

for i in options:	
	copyfile(f"templates/{templates[i]}", f"{root}/art/draft/{templates[i]}")

