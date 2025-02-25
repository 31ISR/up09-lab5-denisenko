from django.shortcuts import render, redirect
from .models import Community
from django.contrib.auth.decorators import login_required
from . import forms

def communities_list(req):
    communities = Community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html',  {'communities': communities})

def communities_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'community': community})
# Create your views here.


@login_required(login_url="/users/login/")
def community_new(request):
    if request.method == 'POST': 
        form = forms.CreateCommunity(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            return redirect('communities:list')
    else:
        form = forms.CreateCommunity()
    return render(request, 'communities/community_new.html', { 'form': form })