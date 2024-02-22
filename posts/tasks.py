from celery import shared_task
import logging

@shared_task
def async_log(message):
    logger = logging.getLogger(__name__)
    logger.info(message)
