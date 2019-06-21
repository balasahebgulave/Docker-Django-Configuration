from django.shortcuts import render
from Taskproject.settings import STATIC_ROOT
from django.http import HttpResponse
import pandas as pd
import os
import json

data = pd.read_csv('static/input_data.csv')
images = os.listdir('static/downloads')
local_path = ['/static/downloads/'+i for i in images]
data['local_path'] = local_path
data.to_csv('static/output_data.csv')
data = pd.read_csv('static/output_data.csv')


def homepage(request):
	return render(request,'filetable.html')

def jsondata(request):
	apidata = data.to_dict(orient='records')
	return HttpResponse(json.dumps(apidata))

def get_images():
	
	image_urls = data['image_url']
	for index, img_url in enumerate(image_urls):
		emp_name = f"emp{index}"
		try:
			urllib.request.urlretrieve(img_url, f"downloads/{emp_name}.jpg")
		except:
			print('Not Found')
