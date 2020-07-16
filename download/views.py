from pytube import YouTube
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class DownloadMovie(View):
	template_name = 'home.html'
	test='from views'

	def helloWorld(self):
		print('helloWorld!')

	def helloPost(self):
		print('This method is POST!!')

	def get(self, request, *args, **kwargs):
		# print(request)
		self.helloWorld()
		return render(request, self.template_name, {'test': self.test})

	def post(self, request, *args, **kwargs):
		number1=request.POST['num']
		url=request.POST['url']
		yt = YouTube(url)
		yt.streams[0].download()
		self.helloPost()
		return render(request, self.template_name, {'test': self.test, 'number2': number1})
