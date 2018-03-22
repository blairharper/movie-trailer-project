import webbrowser
import time


print("[x] Started: "+time.ctime())
for x in range (0, 3):
    time.sleep(10)
    url = 'https://www.youtube.com/watch?v=cpx3q5J7Tzc'
    webbrowser.get("chrome").open_new(url)
    
