from django.utils.translation import ugettext_lazy as _

WORKER_STATE_RUNNING = 'r'
WORKER_STATE_DEAD = 'd'

WORKER_STATE_CHOICES = (
    (WORKER_STATE_RUNNING, _(u'running')),
    (WORKER_STATE_DEAD, _(u'dead')),
)

JOB_STATE_PENDING = 'p'
JOB_STATE_PROCESSING = 'r'
JOB_STATE_ERROR = 'e'

JOB_STATE_CHOICES = (
    (JOB_STATE_PENDING, _(u'pending')),
    (JOB_STATE_PROCESSING, _(u'processing')),
    (JOB_STATE_ERROR, _(u'error')),
)

JOB_QUEUE_STATE_STOPPED = 's'
JOB_QUEUE_STATE_STARTED = 'r'

JOB_QUEUE_STATE_CHOICES = (
    (JOB_QUEUE_STATE_STOPPED, _(u'stopped')),
    (JOB_QUEUE_STATE_STARTED, _(u'started')),
)

DEFAULT_JOB_QUEUE_POLL_INTERVAL = 2
DEFAULT_DEAD_JOB_REMOVAL_INTERVAL = 5
DEFAULT_JOB_QUEUE_PRIORITY = 0
