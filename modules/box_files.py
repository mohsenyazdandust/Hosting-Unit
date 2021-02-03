def get_files():
	import os 
	import time
	import pathlib

	files = []
	directory = os.path.join(pathlib.Path().absolute(), "box")

	for file in os.listdir(directory):
		file_dir = os.path.join(directory, file)
		file_size = os.path.getsize(file_dir)
		size_m = "B"
		if file_size >= 1024 * 1024:
			file_size /= 1024 * 1024
			size_m = "MB"
		elif file_size >= 1024:
			file_size /= 1024
			size_m = "KB"
		file_dict = {'Name': file,
			"Date": time.strftime('%Y/%d/%m',time.gmtime(os.path.getmtime(file_dir))),
			"Size": round(file_size),
			"Size_m": size_m}
		files.append(file_dict)

	return files
