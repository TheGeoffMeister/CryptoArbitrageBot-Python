import httplib, base64, json, hashlib, hmac, time, urllib

def main():
    
    pair1 = 'BTC'
    pair2 = 'USD'
    
    pair = pair1+pair2
    
    side = "sell"
    
    get_price = Get(pair1, pair2)
    price = get_price.Send_Get()[side]
    
    size = '{0:f}'.format(0.00001)
    
    fees = Post("account_infos").Sign(Post("account_infos").Get_Info())
   

    
def API_Keys():
    key = 'os50Un8kHgctOD7jmNQVhUTabaniIbhQRWlcWCGXPdI'
    secret = 'LmID1xpEJBUhHyT7nYyF47O4brBt1pw1yohKpR4hTSI'
    return {"Key":key, "Secret":secret}

def Nonce():
    return str(round(time.time()-1398621111,1)*10)   

    
class Post(object):    
    
    def __init__(self,request):
        self.request = request
    
    def Get_Info(self):
        
        api_v = '/v1/'        
        post_type = self.request    
        address = api_v + post_type
            
        params = {"request": address,              
                  "nonce": Nonce()}
                  
        return (address, params)  
 
    def Send_Order(self, pair, size, price, side):
        self.pair = pair
        self.size = size
        self.price = price
        self.side = side
        
        api_v = '/v1/'
        post_type = "order/new"    
        address = api_v + post_type
        
        params = {"request": address,
                  "symbol": self.pair,
                  "amount": self.size,
                  "price": self.price,
                  "side": self.side,
                  "type": "market",
                  "nonce": Nonce()}
        
        return (address, params)
        
    def Sign(self, path, params):   
        
        post_data = urllib.urlencode(params)
        
        body = '%s%c%s' % (path, 0x00, post_data)
        privkey_bin = base64.b64decode(self.secKey)
        signature_bin = hmac.new(privkey_bin, body, hashlib.sha512).digest()
        signature = base64.b64encode(signature_bin)
        headers = [ 'Rest-Key: %s' % self.pubKey, 'Rest-Sign: %s' % signature ]
        
        conn = httplib.HTTPSConnection("https://api.bl3p.eu/1/")
        conn.request("POST", address, headers)
        
        response = conn.getresponse()
        print(response.status,response.reason)
        
        resp = json.load(response)
        
        return resp    
        
class Get(object):
    
    def __init__(self,pair1, pair2):
        self.pair1 = pair1
        self.pair2 = pair2
        
    def Send_Get(self):
        
        api_v = '/v1/'
        
        if self.pair2.lower() == 'usd':               
          
            conn = httplib.HTTPSConnection("https://api.bl3p.eu/1/")
            conn.request("GET", api_v+"/pubticker/"+self.pair1.lower()+self.pair2.lower())
            
            response = conn.getresponse()
            print(response.status, response.reason)
            
            resp = json.load(response)
            result = resp            
                        
            bfx_buy = result['ask']
            bfx_sell = result['bid']
            
            print 'Bitfinex '+self.pair1+'/'+self.pair2, bfx_buy,'/',bfx_sell
        else:
            print 'Bitfinex only accepts usd'
        
        return {"buy":bfx_buy, "sell":bfx_sell}                
        
   
    

        
    
if __name__ == "__main__":
    main()



