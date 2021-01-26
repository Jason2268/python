# 高德地图地理编码api调用接口，具体方法请参考高德地图api（https://lbs.amap.com/api/webservice/guide/api/weatherinfo）
import requests,json
import pandas as pd # 调用pandas模块
def weather(key,city,extensions):  # 输入高德地图密钥
    url='https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    params={
       'key':key,
        'city':city,
        'extensions':extensions
    }
    response=requests.get(url,params)
    r=response.json() # 返回json数据
    return r

