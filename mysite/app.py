from flask import  Flask, render_template,request,escape # 调用flask模块中的功能
import requests                
import matplotlib.pyplot as plt
import json                
from tianqi import weather # 从tianqi模块中调用weathe函数
from dilibianma import gan # 从dilibianma模块中调用gan函数
from ip import ipdinwei    # 从ip模块中调用ipdiwei函数

app = Flask(__name__)

def log_request(req:"flask request",res:str):
	with open("vsearch.log","a") as log: # 添加文件方式
		print(req.form,req.host_url,req.remote_addr,file=log,sep="|") # 用“|”符号分割打印结果

# 登录页面的设置
@app.route("/login",methods=['get'])                         # 跳转路径为/login，执行方法为“get”
def index()-> 'html':
	title ='welcome' # 输入参数
	return render_template("login.html",the_title=title)     # 渲染页面，把参数传递给login.html文件

#主页面设置
@app.route('/entry',methods=['post','get'])                  # 跳转路径为/entry，执行方法为“post、get”
def hello_entry():
	return render_template('entry.html',the_title='天气查询') # 渲染页面，把参数传递给login.html文件

# 天气页面
@app.route("/tianqi",methods=["post"])                       # 路径为/tianqi，执行方法为“post”
def jt():
	key='a8ead224166cf315eaa25c40689da23d'     # 输入密钥参数
	city=request.form["tq"]                                 # 接收post方法的对象，来自entry.html文件
	extensions='base'                 # 高德地图的参数
	a=weather(key,city,extensions)       # 调用weather函数
	b=a['lives'][0]['city']                   # 索引值提取函数结果的字典内容
	c=a['lives'][0]['weather']
	d=a['lives'][0]['temperature']
	e=a['lives'][0]['winddirection']
	f=a['lives'][0]['windpower']
	g=a['lives'][0]['reporttime']
	return render_template('tianqi.html',city=str(b),weather=str(c),temperature=str(d),winddirection=str(e),windpower=str(f),reporttime=str(g)) # 渲染页面，把参数传递给tianqi.html文件

# 地理编码页面
@app.route("/dili",methods=["post"]) # 同上
def dili():
	address=request.form["dz"]       # 接收post方法的对象，来自tianqi.html文件
	city=request.form["cs"]          # 接收post方法的对象，来自tianqi.html文件
	h=gan(address,city)              # 调用函数功能
	i=h['geocodes'][0]['location']   # 字典提取
	return render_template('dili.html',city=str(i)) # 渲染页面，把参数传递给dili.html文件

# ip 定位页面
@app.route("/ipdinweis",methods=["post"])    # 同上
def ipdinweis():
	ip=request.form["ips"]       # 接收post方法的对象，来dili.html文件
	h=ipdinwei(ip)               # 同上
	a=h["province"]
	b=h["city"]
	c=h["adcode"]
	d=h["rectangle"]
	return render_template('ip.html',province=str(a),city=str(b),adcode=str(c),rectangle=str(d)) # 渲染页面，把参数传递给ip.html文件

# 名人分析页面
@app.route("/person",methods=["POST"]) # 同上
def person():
	image_url=request.form["person"]   # 接收post方法的对象，来ip.html文件
	# 下面可参考azure视觉人脸名人分析api示例代码地址：https://docs.microsoft.com/zh-cn/azure/cognitive-services/computer-vision/concept-detecting-domain-content
	subscription_key = "dd748cf10bf9404399e5416d9399e218"  # 输入azure视觉api密钥
	assert subscription_key 
	vision_base_url = "https://api-computervvsion-cyl.cognitiveservices.azure.com/vision/v2.1/" # azure 调用名人分析api的路径
	celebrity_analyze_url = vision_base_url + "models/celebrities/analyze" 
	headers = {'Ocp-Apim-Subscription-Key': subscription_key}
	params = {'model': 'celebrities'}
	data = {'url': image_url}
	response = requests.post(celebrity_analyze_url, headers=headers, params=params, json=data)
	response.raise_for_status()
	analysis = response.json()
	celebrity_name = analysis["result"]["celebrities"][0]["name"].capitalize()     # 提取字典
	confidence2=analysis["result"]["celebrities"][0]["confidence"]                 # 提取字典
	return render_template('mr.html',person=str(celebrity_name),confidence2=str(confidence2),img_url3=image_url) # 渲染页面，把参数传递给mr.html文件

# 日志页面
@app.route("/viewlog") # 同上
def view_log():
	contents=[] # 建立空列表
	with open("vsearch.log","r") as log: # 打开vsearch.log 文件
		for line in log:   # for循环并用“|”进行分割
			contents.append([])
			for item in line.split("|"):
				contents[-1].append(escape(item)) 
		titles= ["Formdata","Host_url","Remote_addr"]
	return render_template('view.html',the_data=contents,the_titles=titles) # 渲染页面，把参数传递给view.html文件
	

if __name__ == '__main__':
	app.run(debug= True) # debug开启调试功能