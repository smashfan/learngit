const util = require("util")
const crypto = require('crypto');

// 提取参数，拼接待计算签名的字符串
function getSignString(path,query,body){
    const newObj = Object.assign(query,body);
    if (Object.keys(newObj).length===0){
        return path;
    }
    const sortObj = Object.keys(newObj).sort();
    let signString='' ;
    for (let i=0;i<sortObj.length;i++){
        const key = sortObj[i],
            value = newObj[sortObj[i]];
        const ps = util.format('%s=%s',key,value);
        if (i<sortObj.length-1){
            signString = signString +ps+'&';
            continue;
        }
        signString = signString + ps;
    }
    if (path && signString !== ''){
        return path+'?'+signString;
    }
}

// 计算签名
function genSignature(key,value){
    return crypto.createHmac('sha256', key)
        .update(value, 'utf8')
        .digest('hex');
}

const path = '/api/v1/resource/queryResource'
const query = {}
const body = {"id":"c4f643f0-5717-11eb-b6e0-f7651d8dccc0"}

const appId = '3387580',
appSecret = '1231d2054cfd4071abca74a668369ed2',
timestamp = 1611145395,
nonce = '5c3ec543-eff7-461f-9e43-152d59cf6767';

const key = util.format('appId=%s&appSecret=%s&timestamp=%s&nonce=%s',
    appId,appSecret,timestamp,nonce);
const value = getSignString(path,query,body)

console.log(key);
console.log(value);
console.log('签名sign：')
console.log(genSignature(key,value));



