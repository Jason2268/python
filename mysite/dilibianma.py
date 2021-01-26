# 高德地图地理编码api调用接口，具体方法请参考高德地图api（https://lbs.amap.com/api/webservice/guide/api/georegeo）
import requests
import json
gaodeiAPI_key = "a8ead224166cf315eaa25c40689da23d" # 输入高德地图密钥
def gan(address:" ",city:" "): #参数
    params = {"key":gaodeiAPI_key,
              "city":city,
              "citylimit":True,
              "address":address,
              "output":"json"
             }
    response = requests.get("https://restapi.amap.com/v3/geocode/geo?parameters",params=params)
    r=response.json() # 返回json数据
    return r 