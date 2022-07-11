

#文字charをi文字分進める
def change_char_of_alphabet(char, i):
	char_ord = ord(char)
	if(char_ord >= ord('a') and char_ord <= ord('z')):
		char_idx = char_ord - ord('a')
		new_char_ord = ((char_idx + i) % 26) + ord('a')
	elif(char_ord >= ord('A') and char_ord <= ord('Z')):
		char_idx = char_ord - ord('A')
		new_char_ord = ((char_idx + i) % 26) + ord('A')
	else:
		new_char_ord = char_ord
	new_char = chr(new_char_ord)
	return new_char

#[TODO]出力を折り返して見やすくする
#[TODO]数字に対応する
def cipher(string):
	except_chars = [' ', '.', '\n']
	for i in range(-26, 26):
		print("------------")
		print("|i: {:>5}  |".format(i))
		#print("------------")	
		for char in string:
			if(char in except_chars):
				print(char, end = '')
			else:
				new_char = change_char_of_alphabet(char, i)
				print(new_char, end='')
		print("\n------------\n\n")


if __name__ == "__main__":
	string = input()
	cipher(string)