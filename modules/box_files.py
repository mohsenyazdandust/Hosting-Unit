def get_files():
	from os import listdir
	from os.path import isfile, join
	import pathlib

	directory = join(pathlib.Path().absolute(), "box")
	files = [file for file in listdir(directory) if isfile(join(directory, file))]
	return files
