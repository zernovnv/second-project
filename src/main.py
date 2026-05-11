#!/usr/bin/env python3



def print_author():
	from dotenv import load_dotenv
	import os
	load_dotenv(dotenv_path='./.env')
	author = os.getenv('AUTHOR')
	print(f"Автор проекта: {author}")



print_author()
