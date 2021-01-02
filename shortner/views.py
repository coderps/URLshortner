from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shortner.models import short_URL
from shortner.serializers import shortUrlSerializer
from django.views.decorators.csrf import csrf_exempt
import random, string

class urlView(APIView):
	def get(self, request):
		return Response( shortUrlSerializer(short_URL.objects.all(), many=True).data )

	def post(self, request):
		try:
			short_URL.objects.filter(complete_url = str(request.data["complete_url"])).update(visits = int(request.data["visits"]) + 1)
			return redirect('/')
		except Exception as e:
			url = str(request.data["complete_url"])
			if any(url in x["complete_url"] for x in short_URL.objects.values('complete_url')):
				shortened_url = [x["shortened_url"] for x in shortUrlSerializer(short_URL.objects.all(), many=True).data if x["complete_url"] == url][0]
				return Response("This URL already has a shortened URL: " + shortened_url)
			shortened_url = self.shorten(url)
			data_to_store = {
				"complete_url": url,
				"shortened_url": shortened_url
			}
			serializer = shortUrlSerializer(data=data_to_store)
			if serializer.is_valid():
				serializer.save()
				return redirect('/')	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def shorten(self, url):
		base_url = "https://tier.app/"
		shortened_urls = short_URL.objects.values('shortened_url')
		extention_url = shortened_urls[0]["shortened_url"]
		while any(extention_url in x["shortened_url"] for x in shortened_urls):
			extention_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		return base_url + extention_url

@csrf_exempt
def index(request):
    return render(request,'index.html')