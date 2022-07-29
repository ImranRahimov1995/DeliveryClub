import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery('config',
             include=['apps.core.celery_tasks'],
)

app.config_from_object('django.conf:settings', namespace="CELERY")

app.conf.beat_schedule = {

}

app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()