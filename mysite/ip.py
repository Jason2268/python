# 高德地图地理编码api调用接口，具体方法请参考高德地图api（https://lbs.amap.com/api/webservice/guide/api/ipconfig）
import requests
gaodeiAPI_key = "a8ead224166cf315eaa25c40689da23d" # 输入高德地图密钥
def ipdinwei(ip): #参数
    params = {"key":gaodeiAPI_key,
              "ip":ip,
              "output":"json"
             }
    r = requests.get("https://restapi.amap.com/v3/ip?parameters",params=params)
    data = r.json() # 返回json数据
    del data['status']  # 删除 data数据中的字典['status']
    del data['info'] # 删除 data数据中的字典['info']

    return data 