from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)
from . import tasks
from .__init__ import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, SLACK_WEBHOOK_SECRET


# Create your views here.

def authenticate_slack(request):
    if request.POST['token'] != SLACK_WEBHOOK_SECRET:
        return False
    return True


@csrf_exempt
def josiah_button(request):
    from pprint import pprint
    import json
    from threading import Thread
    payload = json.loads(request.POST['payload'])
    headers = dict(request.headers)
    print("printing headers")
    pprint(headers)

    print('printing payload!')
    print(payload)


    t = Thread(target=tasks.tell_josiah_thread, kwargs={'form': payload})
    t.start()
    #tasks.tell_josiah.delay(json.loads(request.POST['payload']))
    return HttpResponse(status=200)


@csrf_exempt
def test_request(request):
    #if authenticate_slack(request) is not True:
    #    return HttpResponse(status='400', reason='slack token not matched')
    from pprint import pprint
    print("printing headers")
    pprint(dict(request.headers))

    print('printing body content!')
    pprint(request.POST['payload'])
    logger.info("this is a log from test_request!")

    return HttpResponse(status=200)



@csrf_exempt
def test_interactive(request):
    from pprint import pprint
    import json
    print("printing headers")
    pprint(dict(request.headers))

    print('printing body content!')
    print(json.loads((request.POST['payload'])))
    #request.POST
    logger.info("this is a log from test_request!")

    return HttpResponse(status=200)


def test_task(request):
    testing(request)
    return HttpResponse(status=200)
