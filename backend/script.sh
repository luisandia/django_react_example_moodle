#python rest_api/manage.py collectstatic --no-input --clear
python rest_api/manage.py makemigrations
python rest_api/manage.py migrate
python rest_api/manage.py runserver 0.0.0.0:8000
# python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess rest_api/manage.py runserver --noreload --nothreading 0.0.0.0:8000
# python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess rest_api/manage.py runserver  0.0.0.0:8000