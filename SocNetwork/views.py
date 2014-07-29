from django.contrib.auth.models import User
from SocNetwork.models import UserLink
from django.template import Context, loader 
from django.http import HttpResponse 
from django.shortcuts import render

def user_list(request):
  user_list = User.objects.all()
  t = loader.get_template ('SocNetwork/user_list.html')
  c = Context({'user_list': user_list, })
  return HttpResponse(t.render(c))

def followers(request, myusername):
  user = User.objects.get(username=myusername)
  follower_list = UserLink.objects.all().filter(from_user = user)
  t = loader.get_template ('SocNetwork/followers.html')
  c = Context({'follower_list': follower_list})
  return HttpResponse(t.render(c))

def following(request, myusername):
  user = User.objects.get(username=myusername)
  follower_list = UserLink.objects.all().filter(to_user = user)
  t = loader.get_template ('SocNetwork/following.html')
  c = Context({'follower_list': follower_list})
  return HttpResponse(t.render(c))
# Create your views here.
