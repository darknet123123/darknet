import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create-every-30-minutes':{
        'task':'account.tasks.get_string_time',
        'schedule':60*30
    }
}


# celery -A config beat
# celery -A config worker

