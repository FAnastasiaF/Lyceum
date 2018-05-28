import time
import vk
id1 = 252486807
id2 = 54890996
ii = 1
qq = 'Нет в друзьях 3 степени'
session = vk.Session()
vk_api = vk.API(session, v = '5.35')
session = vk.AuthSession('6092811', 'login', 'pass', scope='wall, messages, friends')
vk_api = vk.API(session, v = '5.35')
r = vk_api.users.get(user_id = id1)
f = vk_api.friends.get(user_id = id1 , order = "name", name_case = "nom")
vk_api = vk.API(session, v = '5.35')
a = f['items']
i = len(a)
A = str(id1)
while i != 0:
    print(i)
    r = vk_api.users.get(user_id = a[i-1])
    B = a[i-1]
    i = i-1
    time.sleep(1/3)
    if(B == id2):
        qq = 'Друг'
        ii = 0
        i = 0
q = len(a)
print(ii)
if(ii != 0):
    q = len(a)
    print(a[q - 1])
    while q != 0:
        try:
            A1 = a[q - 1]
            n = vk_api.friends.get(user_id=a[q - 1], order="name", name_case="nom")
            vk_api = vk.API(session, v='5.35')
            r = vk_api.users.get(user_id=a[q - 1])
            print(r)
            e = n['items']
            i = len(e)
            while i != 0:
                time.sleep(1 / 3)
                B1 = e[i - 1]
                q1 = len(e)
                while (q1 != 0):
                    try:
                        A2 = e[q1 - 1]
                        if (A2 == id2):
                            ii = 2
                        if(ii != 2):
                            n2 = vk_api.friends.get(user_id=e[q1 - 1], order="name", name_case="nom")
                            vk_api = vk.API(session, v='5.35')
                            r1 = vk_api.users.get(user_id=e[q1 - 1])
                            print(r1)
                            e1 = n2['items']
                            i1 = len(e1)
                            print(i)
                            while (i1 != 0):
                                time.sleep(1 / 3)
                                print(i1)
                                B2 = e1[i1 - 1]
                                print(B2)
                                i1 = i1 - 1
                                if(B2 == id2):
                                    qq = 'Друг друга друга'
                                    i1 = 0
                    except:
                        print("banned1")
                    q1 = q1 - 1
                i = i - 1
                i = 0
        except:
            print("banned")
        q = q - 1
        if(ii == 2):
            q = 0
print()
if(ii == 2):
    print("Друг друга")
else:
    print(qq)
        

