import sys


def reverse_txt(file_name):
	f = open(file_name, "r")
	lines = f.readlines()
	f.close()
	f = open(file_name, "w")
	for i in range(len(lines) - 1, -1, -1):
		f.write(lines[i])
	f.close()


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 reverse_and_overwrite_txt.py <txt_file>")
	else:
		file = sys.argv[1]
		reverse_txt(file)
