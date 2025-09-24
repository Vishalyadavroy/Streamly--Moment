from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index(request):
      return render(request, 'index.html')

#sare ke sare tweet ek page per list ho jaye
def tweet_list(request):
  tweets = Tweet.objects.all().order_by('-created_at')
  return render(request, 'tweet_list.html',{'tweets':tweets})


def tweet_create(request):
   
    if request.method =="POST": #kya data aa rha hai 
      form =  TweetForm(request.POST, request.FILES)
      if form.is_valid():
          tweet = form.save(commit = False)
          tweet.user = request.user
          tweet.save() 
          return redirect('tweet_list')
    else:
        form =TweetForm()
    return render(request, 'tweet_form.html',{'form':form})

def tweet_edit(request,tweet_id ):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user=request.user)
    if request.method =='POST':
      form =  TweetForm(request.POST, request.FILES,
      instance=tweet)
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('tweet_list')
     
    else:
        form = TweetForm(instance = tweet)
    return render(request, 'tweet_form.html',{'form':form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return redirect('tweet_list')

