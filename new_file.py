import vk
session = vk.Session()
vk_api = vk.API(session, v='5.35')
vk_api.users.get(user_id=1)
session = vk.AuthSession('users_id', 'login', 'pass', scope='wall, messages, friends')
vk_api = vk.API(session, v='5.35')
vk_api.friends.getOnline(user_id=id, list_id = 1, online_mobile = 1)

