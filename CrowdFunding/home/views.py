from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from projects.models import ProjectRating ,Projects ,ProjectTags
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if (request.method == 'GET'):

        a=ProjectRating.objects.all().order_by('-rating')[:5]
        b = Projects.objects.all().order_by('-created')[:5]
        c = Projects.objects.filter(featured=True).order_by('-created')[:5]
        d = Projects.objects.filter(user=request.user)
        return render(request,'home/index.html',{"a": a ,"b":b ,"c":c ,"d":d})
    else:
        search = request.POST['search']
        l = []
        for a in Projects.objects.all():
            l.append(a.title)
        ltag = []
        for a in ProjectTags.objects.all():
            ltag.append(a.tag)
        resultTile = list(filter(lambda project: search.lower() in project.lower(), l))
        resultTag = list(filter(lambda project: search.lower() in project.lower(), ltag))
        print(resultTag)
        ids = []

        for i in resultTile:
            ids.append(Projects.objects.get(title=i))
        for i in resultTag:
            ids.append(ProjectTags.objects.get(tag=i).project)
        a = ProjectRating.objects.all().order_by('-rating')[:5]
        b = Projects.objects.all().order_by('-created')[:5]
        c = Projects.objects.filter(featured=True).order_by('-created')[:5]
        d = Projects.objects.filter(user=request.user)
        ids = list(dict.fromkeys(ids))
        return render(request, 'home/index.html', {"a": a, "b": b, "c": c, "d": d, "ids": ids})

