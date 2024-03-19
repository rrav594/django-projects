from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    'january': 'This is Jan.',
    'february': 'This is Feb.',
    'march': 'This is March.',
    'april': 'This is April.',
    'may': None,
    'june': 'This is June',
    'july': 'This is July',
    'august': 'This is August',
    'september': 'This is September',
    'october': 'This is October',
    'november': 'This is November',
    'december': 'This is December'
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_url = reverse('month-challenge', args=[redirect_month])
        # return HttpResponseRedirect('/challenges/'+redirect_month)
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound('<h1>This is not a valid number.</h1>')


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # respnose_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(respnose_data)
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text, "month": month
        })
    except:
        # respose_data = render_to_string('404.html')
        # return HttpResponseNotFound(respose_data)
        raise Http404()
