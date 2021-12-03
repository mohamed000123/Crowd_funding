from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProjectsSer, ImageSer, TagsSer, RatingSer
from projects.models import Projects, ProjectTags, ProjectImages, ProjectRating, Comments, Replies, ReportProject, ReportComment
from django.db.models import Avg, Sum
from django.db.models import Q


# Create your views here.
def getRatingDonations(project):
    rating = ProjectRating.objects.filter(
        project=project).aggregate(Avg('rating'))['rating__avg']
    if not rating:
        rating = 0
    donations = ProjectRating.objects.filter(
        project=project).aggregate(Sum('donations'))['donations__sum']
    if not donations:
        donations = 0
    return {'rating': rating, 'donations': donations}


class AddProjects(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'projects/addprojects.html')
        else:
            return HttpResponseRedirect('/accounts/login')

    def post(self, request):
        if request.user.is_authenticated:
            data = request.POST
            imgs = request.FILES.getlist('images')
            project = Projects.objects.create(title=data['title'], details=data['details'], category=data['category'],
                                              totalTarget=data['totaltarget'], start=data['start'], end=data['end'], user=request.user)
            tags = data['tags'].split(',')[:-1]
            for tag in tags:
                ProjectTags.objects.create(project=project, tag=tag.strip().lower())
            for img in imgs:
                ProjectImages.objects.create(project=project, image=img)
            return HttpResponseRedirect('/pro')
        else:
            return HttpResponseRedirect('/accounts/login')


class ViewProjects(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = []
            projects = Projects.objects.all()
            for project in projects:
                get = getRatingDonations(project)
                data.append(
                    {'project': project, 'rating': get['rating'], 'donations': get['donations']})
            return render(request, 'projects/projects.html', {'data': data})
        else:
            return HttpResponseRedirect('/accounts/login')


class ProjectsApi(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            projects = Projects.objects.all()
            images = ProjectImages.objects.all()
            tags = ProjectTags.objects.all()
            ratings = ProjectRating.objects.all()
            projectsser = ProjectsSer(projects, many=True).data
            imagesser = ImageSer(images, many=True).data
            tagsser = TagsSer(tags, many=True).data
            ratingser = RatingSer(ratings, many=True).data
            return Response({'projects': projectsser, 'images': imagesser, 'tags': tagsser, 'rating': ratingser})
        else:
            return HttpResponseRedirect('/accounts/login')


def getsimilar(project):
    ptags = []
    result = []

    projecttags = ProjectTags.objects.filter(project=project)
    alltags = ProjectTags.objects.filter(~Q(project=project))

    for tag in projecttags:
        ptags.append(tag.tag.strip())

    for tag in alltags:
        if tag.tag.strip() in ptags:
            result.append(tag.project)
    result = list(dict.fromkeys(result))
    if len(result) > 4:
        result = result[0:4]
    return result



class Project(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            project = Projects.objects.get(id=id)
            images = ProjectImages.objects.filter(project=project)
            urating = ProjectRating.objects.filter(
                project=project, user=request.user)
            if not urating:
                urating = None
            else:
                urating = urating[0].rating
            get = getRatingDonations(project)
            cancel = False
            if get['donations'] <= (project.totalTarget/4) and request.user == project.user:
                cancel = True
            commenting = []
            comments = Comments.objects.filter(project=project)
            for comment in comments:
                replies = Replies.objects.filter(comment=comment)
                commenting.append({'comment': comment, 'replies': replies})
            similars = getsimilar(project)
            return render(request, 'projects/project.html', {'project': project, 'images': images,
                                                             'rating': get['rating'], 'donations': get['donations'],
                                                             'comments': commenting, 'urating': urating,
                                                             'cancel': cancel, 'similars': similars})
        else:
            return HttpResponseRedirect('/accounts/login')

    def post(self, request, id):
        if request.user.is_authenticated:
            project = Projects.objects.get(id=id)
            rating = ProjectRating.objects.filter(
                project=project, user=request.user)
            if rating:
                rate = request.POST['rate']
                rating.update(rating=int(rate))
            else:
                ProjectRating.objects.create(
                    project=project, user=request.user, rating=request.POST['rate'])
            return HttpResponseRedirect(f'/pro/project/{id}')
        else:
            return HttpResponseRedirect('/accounts/login')


class Donate(View):
    def post(self, request):
        if request.user.is_authenticated:
            id = request.POST['id']
            project = Projects.objects.get(id=id)
            donations = ProjectRating.objects.filter(
                project=project, user=request.user)
            if donations:
                donate = request.POST['donate']
                if donate:
                    donations.update(donations=donations[0].donations+int(donate))
            else:
                ProjectRating.objects.create(
                    project=project, user=request.user, donations=request.POST['donate'])
            return HttpResponseRedirect(f'/pro/project/{id}')
        else:
            return HttpResponseRedirect('/accounts/login')


class Comment(View):
    def post(self, request):
        id = request.POST['project']
        project = Projects.objects.get(id=id)
        Comments.objects.create(
            user=request.user, project=project, comment=request.POST['comment'])
        return HttpResponseRedirect(f'/pro/project/{project.id}')


class Reply(View):
    def post(self, request):
        id = request.POST['comment']
        comment = Comments.objects.get(id=id)
        Replies.objects.create(
            user=request.user, comment=comment, reply=request.POST['reply'])
        return HttpResponseRedirect(f'/pro/project/{request.POST["project"]}')


class Cancel(View):
    def post(self, request):
        Projects.objects.get(id=request.POST['project']).delete()
        return HttpResponseRedirect('/pro')


class Report(View):
    def get(self, request, typ, id):
        return render(request, 'projects/report.html', {'type': typ})

    def post(self, request, typ, id):
        if typ == 'project':
            project = Projects.objects.get(id=id)
            ReportProject.objects.create(user=request.user, project=project, msg=request.POST['msg'],
                                         type=request.POST['type'])
        else:
            comment = Comments.objects.get(id=id)
            ReportComment.objects.create(user=request.user, comment=comment, msg=request.POST['msg'],
                                         type=request.POST['type'])
        return HttpResponseRedirect(f'/pro/project/{id}')
