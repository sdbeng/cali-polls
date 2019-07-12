from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


# A shortcut: render()
# It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provides a shortcut. Here’s the full index() view, rewritten:
# Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)