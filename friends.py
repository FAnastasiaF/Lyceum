import time
import vk
import graphviz as gv
id1 = 452546933
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
a4 = gv.Graph(format='svg')
q = len(a)
print(a[q-1])
while q != 0:
    try:
        A1 = str(a[q - 1])
        n = vk_api.friends.get(user_id=a[q - 1], order="name", name_case="nom")
        vk_api = vk.API(session, v='5.35')
        r = vk_api.users.get(user_id=a[q - 1])
        print(r)
        e = n['items']
        i = len(e)
        while i != 0:
            time.sleep(1 / 3)
            B1 = str(e[i - 1])
            a4.edge(A1, B1)
            q1 = len(e)
            while (q1 != 0):
                try:
                    A2 = str(e[q1 - 1])
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
                        B2 = str(e1[i1 - 1])
                        print(B2)
                        a4.edge(A2, B2)
                        i1 = i1 - 1
                except:
                    print("banned1")
                q1 = q1 - 1
            i = i - 1
            i = 0
    except:
        print("banned")
    q = q-1
filename = a4.render(filename='img/a8')
print (filename)
