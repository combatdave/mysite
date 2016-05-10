from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


def db(request):
	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	text = "</br>".join([str(g.when) for g in greetings])

	return HttpResponse('<pre>' + text + '</pre>')
	#return render(request, 'db.html', {'greetings': greetings})