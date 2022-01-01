import telegram
import os
import json


def handler(event, context):
    payload = json.loads(event["body"])

    token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_ID"]

    bot = telegram.Bot(token=token)

    if "issue" in payload and "comment" in payload and payload['action'] == "created":
        text = (
            f"🗣 Комментарий от @{ payload['comment']['user']['login'] } " 
            f"в [{ payload['issue']['title'] }]({ payload['issue']['html_url'] }) "
            f"- { payload['comment']['body'] }"
        )

    elif "issue" in payload and payload['action'] == "opened":
        text = (
            f"👾 Задач привалило: [{ payload['issue']['title'] }]({ payload['issue']['html_url'] }) "
            f"от @{ payload['issue']['user']['login'] }"
        )

    elif "issue" in payload and payload['action'] == "reopened":
        text = (
            f"♻️ Что-то не доделали в задаче, снова открыта: "
            f"[{ payload['issue']['title'] }]({ payload['issue']['html_url'] })"
        )

    elif "pull_request" in payload and payload['action'] in ("opened", "reopened"):
        text = (
            f"🛠 @{ payload['pull_request']['user']['login'] } прислал новый PR: "
            f"[{ payload['pull_request']['title'] }]({ payload['pull_request']['html_url'] })"
        )

    elif "pull_request" in payload and payload['action'] == "ready_for_review":
        text = (
            f"✅ PR [{ payload['pull_request']['title'] }]({ payload['pull_request']['html_url'] }) готов к просмотру"
        )

    elif "pull_request" in payload and payload['action'] == "review_requested":
        text = (
            f"❗️Требуется ревью для PR: [{ payload['pull_request']['title'] }]({ payload['pull_request']['html_url'] })"
        )

    elif "pusher" in payload and payload['ref'] == "refs/heads/master" and payload['repository']['owner']['login'] == 'vas3k':
        text = (
            "💚 Пуш в мастер от { payload['head_commit']['author']['username'] }: [{ payload['head_commit']['message'] }]({ payload['head_commit']['url'] })"
        )

    elif "discussion" in payload and "comment" in payload:
        text = (
            f"🗣 Комментарий от @{ payload['comment']['user']['login'] } " 
            f"в [{ payload['discussion']['title'] }]({ payload['comment']['html_url'] }) "
            f"- { payload['comment']['body'] }"
        )

    elif "discussion" in payload and payload['action'] == "created":
        text = (
            f"🙋 @{ payload['sender']['login'] } хочет обсудить " 
            f"[{ payload['discussion']['title'] }]({ payload['discussion']['html_url'] }) "
        )

    else:
        print(str(payload.keys()) + " : " + str(payload["action"]))

    if text:
        bot.sendMessage(
            chat_id=chat_id,
            text=text,
            parse_mode='markdown',
            disable_web_page_preview=True,
        )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'ok',
        }),
    }
