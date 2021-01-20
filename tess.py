import hashlib
import hmac
path = '/api/v1/resource/queryResource'
query = {}
body = {"id":"c4f643f0-5717-11eb-b6e0-f7651d8dccc0"}

appId = '3387580',
appSecret = '1231d2054cfd4071abca74a668369ed2',
timestamp = 1611145395,
nonce = '5c3ec543-eff7-461f-9e43-152d59cf6767';

key = 'appId=%s&appSecret=%s&timestamp=%s&nonce=%s'%(appId,appSecret,timestamp,nonce)
# value = getSignString(path,query,body)
print(key)
# secret_key1 = b'This is my secret key'
# message1 = b'Hello world'
# hex_res1 = hmac.new(secret_key1, message1, digestmod="sha256").hexdigest()
# print(hex_res1) 

