from celery import shared_task
from .__init__ import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, SLACK_WEBHOOK_SECRET


@shared_task
def tell_josiah(form):
    import random
    from slackclient import SlackClient
    print('Im telling josiah!')
    slack_client = SlackClient(SLACK_BOT_TOKEN)
    channelID = form['channel']['id']
    target_user_id = form['message']['user']
    target_user_info = slack_client.api_call('users.info', user=target_user_id)['user']
    target_real_name = target_user_info['real_name']

    from_user_id = form['user']['id']
    from_user_info = slack_client.api_call('users.info', user=from_user_id)['user']
    from_user_real_name = from_user_info['real_name']
    messagePayload = {
        "method": "chat.postMessage",
		"text": f"Email sent to: Josiah.Zimmerman.hpinc.com\nReplyTime: {round(random.uniform(2, 15),2)} seconds\nMessage reply:\n>From: Josiah Zimmerman\n>Hello. Its me the boss. Thank you very much for the very worrying email.\n>*Jon, Can you go ahead and delete {target_real_name} account? Make sure he isnt paying attention.*\n>Thank you,\n>Enterprise Performance Lead",
        "channel":channelID
    }
    slack_client(**messagePayload)
    return


@shared_task
def testing(request):
    from pprint import pprint
    print("hello!")
    pprint(request)
    return


def tell_josiah_thread(form):
    import random
    from slackclient import SlackClient
    slack_bot_token = "xoxb-569602798086-613953847953-Ubg2wBy0xOLAW4wI0t00kt80"
    print('Im telling josiah!')
    slack_client = SlackClient(slack_bot_token)
    channelID = form['channel']['id']
    target_user_id = form['message']['user']
    target_user_info = slack_client.api_call('users.info', user=target_user_id)['user']
    target_real_name = target_user_info['real_name']
    if target_real_name[-1] == 's':
        target_real_name = target_real_name + "'"
    else:
        target_real_name = target_real_name + "'s"

    from_user_id = form['user']['id']
    from_user_info = slack_client.api_call('users.info', user=from_user_id)['user']
    from_user_real_name = from_user_info['real_name']

    messagePayload = {
        "method": "chat.postMessage",
        "text": (
            f"Thank you {from_user_real_name} for reporting a comment, and keeping this slack channel a wholesome -- as well as corporate friendly-- enviroment!\n"+
            f"\nReport sent to: Josiah.Zimmerman.hpinc.com\nWaiting on reply...\n...\n...\nReply Recieved!\n" +
            f"ReplyTime: {round(random.uniform(2, 15),2)} " +
            f"seconds\nMessage reply:\n>From: Josiah Zimmerman\n>Hello. Its me the boss. " +
            f"Thank you very much for the very worrying email.\n>*Jon, Can you go ahead and delete {target_real_name} "
            f"account? Make sure he isn't paying attention.*\n>Thank you,\n>Enterprise Performance Lead"),

        "channel": channelID
    }
    slack_client.api_call(**messagePayload)
    return