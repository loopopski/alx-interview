#!/usr/bin/python3
"""
0-pascal_triangle
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
def print_triangle(triangle):
	"""
	print the triangle
	"""
	for row in triangle:
		print("[{}]".format(",".join([str(n) for n in row])))

if __name__ = "__pascal__":
	print_triangle(pascal_triangle(5))
