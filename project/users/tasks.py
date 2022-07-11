from celery import shared_task
from celery.signals import task_postrun
from celery.utils.log import get_task_logger


LOGGER = get_task_logger(__name__)

@shared_task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y

@shared_task()
def sample_task(email):
    from project.users.views import api_call

    api_call(email)

@task_postrun.connect
def task_postrun_handler(task_id, **kwargs):
    from project.users.events import update_celery_task_status

    update_celery_task_status(task_id)

@shared_task()
def task_test_logger():
    LOGGER.info('test')