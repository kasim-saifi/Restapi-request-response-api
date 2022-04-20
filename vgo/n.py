import threading
import requests
import time
import pprint

l=[]    #list globle
class Home(threading.Thread): 
    def index():
        URL="http://127.0.0.1:8000/" #restapi url
        res= requests.get(URL)
        rest=res.json()
        l.append(rest)
        print(l)
        count=len(l)
        print(count,"#####rest code######")
    def run():
        for i in l:
            print(i[0],"####") 
t1 = threading.Thread(target=Home.index, args=()) #first thread execute start
t2 = threading.Thread(target=Home.run, args=()) #thread execute after three second   start
t1.start() # start thread 
t1.join() # marge thread
time.sleep(3) # time count (second)
t2.start()#start second thread
t2.join()#marge thread
print("rest code") #rest code something


# def h():
#     start_time=time.time()
#     post_data=[]
#     for _ in range(10):
#         URL="http://127.0.0.1:8000/"
#         res=requests.get(URL)
#         data_all=res.json()
#         post_data.append(data_all)
#         print(post_data)
#         count=len(post_data)
#         total_time=time.time()-start_time
#         print(total_time)
# h()