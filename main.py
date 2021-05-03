from pyrogram import Client
import shelve
import random

api_id = 123456789
api_hash = 'your_hash'
phone_number = '+79*********'
public_chat = '*******'

text_message = [
    'Круто!',
    '5 баллов!',
    'Зачётный видос)',
    'Изи 😃 ',
    '🔥🔥🔥'
]

#список отработанных сообщений

processed_messages = shelve.open('processed_message.db', writeback=True)

with Client("python_cyberpunk", api_id, api_hash,
            phone_number=phone_number) as app:
    public = app.get_chat(public_chat) #Ищем паблик по нику
    print(public)       
    chat = public.linked_chat #Ищем прилинкованный чат к каналу

    for msg in app.get_history(chat.id, limit=5):
        if (msg.from_user is None and msg.forward_from_chat.id == public.id):
            if str(msg.forward_from_message_id) in processed_messages:
                print(f"Пропускаем уже отработанное message_id={msg.message_id}")
                continue

            processed_messages[str(msg.forward_from_message_id)] = True
            print(f"Обработка message_id={msg.message_id}") 
            text = random.choice(text_message)
            app.send_message(
                chat.id, text, reply_to_message_id=msg.message_id)
