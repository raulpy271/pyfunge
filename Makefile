
unit-test-degub:
	python3 -m unittest discover -f -v -s tests -p test_*.py

unit-test:
	python3 -m unittest discover -s tests -p test_*.py
