import os
import cat_service
import subprocess
import platform


def main():
	print_header()
	folder = get_or_create_output_folder()
	print("Found or created folder {}".format(folder))
	cat_downloader(folder)
	display_cats(folder)



def print_header():
	print("------------------------------------")
	print("------------CAT FACTORY-------------")
	print("------------------------------------")


def get_or_create_output_folder():
	base_folder = os.path.dirname(__file__)
	folder = 'cat_pics'
	full_path = os.path.join(base_folder, folder)

	if not os.path.exists(full_path) or not os.path.isdir(full_path):
		print("Creating a directory at {} ".format(full_path))
		os.mkdir(full_path)

	return full_path


def cat_downloader(folder):
	print("Contacting server to download cats....")
	cat_count = 8
	for i in range(1, cat_count+1):
		name = "lolcat_{}".format(i)
		print("Downloading cat..." + name)
		cat_service.get_cat(folder, name)

	print("Done!")


def display_cats(folder):
	print("Displaying cats in OS window ")
	if platform.system() == 'Darwin':
		subprocess.call(['open', folder])
	elif platform.system() == 'Linux':
		subprocess.call(['xdg-open', folder])
	elif platform.system() == 'Windows':
		subprocess.call(['explorer', folder])
	else:
		print("We don't support your OS : " + platform.system())


if __name__ == '__main__':
	main()