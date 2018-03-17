import vk
import time
print('Если хотите увидеть друзей онлайн, то сначала введите 1, а потом id человека про которого вы хотите узнать')
print('Если вам нужны и друзья онлайн и друзья онлайн друзей онлайн, то сначала введите 2, а потом id человека про которого вы хотите узнать')
print('Если только друзья онлайн друзей онлайн, то сначала введите 3, а потом id человека про которого вы хотите узнать')
w =  int(input())
ids = input()
session = vk.Session()
vk_api = vk.API(session, v = '5.35')
session = vk.AuthSession('6092811', '+79161963528', 'zoloto1997', scope='wall, messages, friends')
vk_api = vk.API(session, v = '5.35')
r = vk_api.users.get(user_id = ids)
h = r[0]
d = h['first_name']
p = h['last_name']
print(d, p, ":")
print ()
f = vk_api.friends.getOnline(user_id = ids, list_id = 1, online_mobile = 1)
vk_api = vk.API(session, v = '5.35')
b = f['online']
c = f['online_mobile']
a = b
a.extend(c)
i = len(a)
if w != 3:
    while i != 0:
        r = vk_api.users.get(user_id = a[i-1])
        h = r[0]
        d = h['first_name']
        e = h['last_name']
        print(d, e)
        i = i-1
        time.sleep(1/3)    
if w != 1:
    q = len(a)
    while q!=0:
        print ()
        r = vk_api.users.get(user_id = a[q-1])
        h = r[0]
        d = h['first_name']
        p = h['last_name']
        print(d, p, ":")
        print ()
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
            time.sleep(1/2)
        q = q-1
    

