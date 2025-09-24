from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, TweetFrom
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
      return render(request, 'index.html')

#sare ke sare tweet ek page per list ho jaye
def tweet_list(request):
  tweets =    Tweet.objects.all().order_by('-crated_at')
  return render(request, 'tweet_list.html',{'tweets':tweets})


def tweet_create(request):
   
    if request.method =="POST": #kya data aa rha hai 
        TweetForm(request.POST, request.FILES)
    else:
        form =TweetForm()
    return render(request, 'tweet_form.html',{'form':form})