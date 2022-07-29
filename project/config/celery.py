import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

app = Celery('config',
             include=['apps.core.celery_tasks'],
)

app.config_from_object('django.conf:settings', namespace="CELERY")

app.conf.beat_schedule = {
    'currency_control': {
        'task': 'apps.core.celery_tasks.currency_control',
        'schedule': crontab(hour="*/1"),
    },
    'sync_with_remote_table': {
        'task': 'apps.core.celery_tasks.sync_with_remote_table',
        'schedule': 10,
    },
    'delete_unnecessary_records': {
        'task': 'apps.core.celery_tasks.delete_unnecessary_records',
        'schedule': 25,
    },
}

app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
