from celery import Celery
import requests

from dataactcore.config import CONFIG_DB, CONFIG_SERVICES, CONFIG_JOB_QUEUE
from dataactcore.utils.cloudLogger import CloudLogger


def enqueue(jobID):
    """POST a job to the validator"""
    CloudLogger.log("Adding job {} to the queue".format(str(jobID)))
    validatorUrl = '{validator_host}:{validator_port}'.format(
        **CONFIG_SERVICES)
    if 'http://' not in validatorUrl:
        validatorUrl = 'http://' + validatorUrl
    validatorUrl += '/validate/'
    params = {
        'job_id': jobID
    }
    response = requests.post(validatorUrl, params)
    CloudLogger.log("Job {} has completed validation".format(str(jobID)))
    CloudLogger.log("Validator response: {}".format(str(response.json())))
    return response.json()


class JobQueue:
    def __init__(self, job_queue_url="localhost"):
        # Set up backend persistent URL
        backendUrl = ('db+{scheme}://{username}:{password}@{host}'
                      '/{job_queue_db_name}').format(**CONFIG_DB)

        # Set up url to the job queue to establish connection
        queueUrl = ('{broker_scheme}://{username}:{password}@{host}:{port}'
                    '//').format(host=job_queue_url, **CONFIG_JOB_QUEUE)

        # Create remote connection to the job queue
        self.jobQueue = Celery('tasks', backend=backendUrl, broker=queueUrl)
        self.jobQueue.config_from_object('celeryconfig')

        self.enqueue = self.jobQueue.task(name='jobQueue.enqueue')(enqueue)

if __name__ in ['__main__', 'jobQueue']:
    jobQueue = JobQueue()
    queue = jobQueue.jobQueue
