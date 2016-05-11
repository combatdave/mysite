from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

from .models import Greeting


def home(request):
   context = RequestContext(request,
                           {'user': request.user})
   return render_to_response('mysite/home.html',
                             context_instance=context)


def db(request):
	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	text = "</br>".join([str(g.when) for g in greetings])

	return HttpResponse('<pre>' + text + '</pre>')
	#return render(request, 'db.html', {'greetings': greetings})