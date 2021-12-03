from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from projects.models import ProjectRating ,Projects ,ProjectTags
from django.contrib.auth.decorators import login_required

<<<<<<< HEAD
@login_required
=======
@login_required()
>>>>>>> 4dfdc7fcbba1fb6c58b2f2ad419064b3e21c7d5d
def home(request):
    if (request.method == 'GET'):

        a=ProjectRating.objects.all().order_by('-rating')[:5]
        b = Projects.objects.all().order_by('-created')[:5]
        c = Projects.objects.filter(featured=True).order_by('-created')[:5]
        d = Projects.objects.filter(user=request.user)
        return render(request,'home/index.html',{"a": a ,"b":b ,"c":c ,"d":d})
    else:
        try:

            search = request.POST['search']
            l=[]
            for a in Projects.objects.all():
                l.append(a.title)
            result = list(filter(lambda project: search.lower() in project.lower(),l))
            title=Projects.objects.get(title=result[0]).id
            return redirect('pro/project/' + str(title))
        except:
            search = request.POST['search']
            l = []
            for a in ProjectTags.objects.all():
                l.append(a.tag)
            result = list(filter(lambda project: search.lower() in project.lower(), l))
            tag = ProjectTags.objects.get(tag=result[0]).id
            return redirect('pro/project/' + str(tag))
