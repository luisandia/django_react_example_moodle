FROM python:3.7
LABEL Luis Andia

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY ./leadmanager /backend
# RUN python /backend/leadmanager/manage.py collectstatic --no-input --clear
# RUN python /backend/leadmanager/manage.py collectstatic --no-input --clear
# RUN python /backend/leadmanager/manage.py collectstatic --no-input --clear
# RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.count() == 0 and User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python /backend/leadmanager/manage.py shell
RUN python manage.py migrate
CMD ["gunicorn", "leadmanager.wsgi:application", "--workers=2", "--bind" ,"0.0.0.0:8000"]


RUN useradd -ms /bin/bash user
USER user