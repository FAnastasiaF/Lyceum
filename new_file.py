import vk
import time
session = vk.Session()
vk_api = vk.API(session, v = '5.35')
session = vk.AuthSession('app_id', 'login', 'password', scope='wall, messages, friends')
vk_api = vk.API(session, v = '5.35')
f = vk_api.friends.getOnline(user_id = id, list_id = 1, online_mobile = 1)
vk_api = vk.API(session, v = '5.35')
b = f['online']
c = f['online_mobile']
a = b
a.extend(c)
i = len(a)
while i!=0:
r = vk_api.users.get(user_id = a[i-1])
h = r[0]
d = h['first_name']
e = h['last_name']
print(d, e)
i = i-1
time.sleep(1/3)
q = len(a)
while q!=0:
print ()
r = vk_api.users.get(user_id = a[q-1])
h = r[0]
d = h['first_name']
p = h['last_name']
print(d, p, ":")
print ()
session = vk.Session()
vk_api = vk.API(session, v = '5.35')
session = vk.AuthSession('app_id', 'login', 'password', scope='wall, messages, friends')
vk_api = vk.API(session, v = '5.35')
n = vk_api.friends.getOnline(user_id = a[q-1], list_id = 1, online_mobile = 1)
vk_api = vk.API(session, v = '5.35')
b = n['online']
c = n['online_mobile']
e = b
e.extend(c)
i = len(e)
while i!=0:
r = vk_api.users.get(user_id = e[i-1])
h = r[0]
d = h['first_name']
p = h['last_name']
print(d, p)
i = i-1
time.sleep(1/3)
q = q-1
