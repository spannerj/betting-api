unittest:
	python3 manage.py unittest

# Run this with 'make unittest2' or 'make report="true" unittest2' 
unittest2:
	if [ -z ${report} ]; then python3 manage.py unittest; else python3 manage.py unittest -r; fi

integrationtest:
	python3 manage.py integrationtest

run:
	python3 manage.py runserver
