from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Choice, Question


# A shortcut: render()
# It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provides a shortcut. Here’s the full index() view, rewritten:
# Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context={
#         'latest_question_list':latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, question_id):
    # refactor line 37-41
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html')

    # response = "You're looking at results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

    # return HttpResponse("You're voting on question %s." % question_id)