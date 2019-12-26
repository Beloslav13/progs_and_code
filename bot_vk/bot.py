import vk_api
import vk_api.bot_longpoll
import random
from _token import token

group_id = 190202400


class Bot:
    """Чат-бот группы Вконтакте."""

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск."""
        print('Бот запущен.')
        for event in self.long_poller.listen():
            try:
                self.on_run(event=event)
            except Exception as exc:
                print(f'Исключение - {exc}')

    def on_run(self, event):
        """Обработка событий."""
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            first_name_user, photo_user = self.info_user(event=event)
            self.reply_user(event=event, first_name_user=first_name_user, photo_user=photo_user)

        elif event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_REPLY:
            self.event_message_reply(event=event)

        elif event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_TYPING_STATE:
            print(f'Пользователь: id{event.object.from_id} печатает сообщение')

        else:
            print('не обрабатываю событие такого типа', event.type)

    def reply_user(self, event, first_name_user, photo_user):
        """Ответить пользователю"""
        message = f'Привет, {first_name_user}! Я умею пока что только здороваться и присылать фотку...'
        self.event_new_message(event=event)
        self.api.messages.send(message=message,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=event.message.peer_id,
                               attachment='photo' + photo_user)

    def info_user(self, event):
        """Информация о пользователе"""
        user_get = self.api.users.get(user_ids=event.message.peer_id, fields='photo_id, is_favorite, is_friend')
        # print(user_get)
        first_name_user = (user_get[0]['first_name'])
        photo_user = (user_get[0]['photo_id'])
        return first_name_user, photo_user

    def event_message_reply(self, event):
        """Событие ответ от бота."""
        print(f'Новый ответ от бота для id{event.object.peer_id}')
        print(f'Текст сообщения: {event.object.text}')

    def event_new_message(self, event):
        """Событие новое сообщение от id...."""
        print(f'Получено новое сообщение от: id{event.message.from_id}')
        print(f'Текст сообщения:\n{event.message.text}')


if __name__ == '__main__':
    bot = Bot(group_id=group_id, token=token)
    bot.run()
