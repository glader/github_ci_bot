# Github telegram bot

https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads

Бот для отправки в чат уведомлений о событиях в репозитории.

Как установить:
- создать функцию в Yandex.Cloud
- скопировать туда файлы index.py и requirements.txt
- добавить переменные окружения
  - CHAT_ID - идентификатор чата
  - BOT_TOKEN - идентификатор телеграм-бота, который есть в этом чате
- сделать функцию публично доступной
- скопировать адрес функции и прописать его в webhooks репозитория