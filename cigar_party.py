"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""

def cigar_party(cigars: int, is_weekend: bool) -> bool:
	pass

def main():
 	# How many tests do we need to do
	# to ensure that our function
	# is correct?
	print(cigar_party(20, True))
	print(cigar_party(20, False))

	print(cigar_party(40, True))
	print(cigar_party(40, False))

	print(cigar_party(48, True))
	print(cigar_party(48, False))

	print(cigar_party(60, True))
	print(cigar_party(60, False))

	print(cigar_party(70, True))
	print(cigar_party(70, False))


if __name__ == '__main__':
	main()