import os
import pipenv2setup

if __name__ == '__main__':
	print(os.getcwd())
	pipenv2setup.pipfile2installRequires()