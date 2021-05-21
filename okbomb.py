import threading

okstr = " ok "

def okay():
    global okstr
    print(okstr)
    okstr = okstr + okstr
    x = threading.Thread(target=okay)
    y = threading.Thread(target=okay)
    x.start()
    y.start()
    
okay()