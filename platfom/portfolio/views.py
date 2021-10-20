from django.db.models.fields import files
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth.models import User
from .models import Profile , Project
from portfolio.forms import ProfileForm , ProjectForm

# Create your views here.
def indexpage(request):

    users = User.objects.all().order_by('-date_joined')

    context = {'users': users}
    return render(request, 'index.html' ,context)


def dashboard(request):
    return render(request, 'dashboard.html')

def detail_profil(request, id=None):
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=user)
    context = {'profile': profile }
    return render(request, 'profil.html' ,context)

#eseye jwenn yon solution poum ka fe user lan we projet li yo
def InfosPage(request):
    
    return render(request, 'infos.html')

# sa se pou lhr moun nan se yon user 
# yon user ki konekte
@login_required(login_url='authentificate')
def viewByUser(request):
    mypros = request.user.projects.all()

    context = {'mypros': mypros}
    return render(request, 'template_project.html', context)

@login_required(login_url='authentificate')
def deleteProj(request, id=None):

    Project.objects.get(id=id).delete()
    return redirect("dash")



# sa se pou lhr moun nan pa yon user 
# men li ka toujou we project yon 
def detail_project(request, id=None):
    project = get_object_or_404(Project, id=id)
    context = {'project': project}
    return render(request, 'project.html', context)

@login_required(login_url='authentificate')
def newProfile(request):

    if request.method == "POST":
        myprofil = ProfileForm(data=request.POST, files=request.FILES)
        if myprofil.is_valid: # si profil lan valid
            mypro = request.user.profile
            mypro.name = request.POST.get("name")
            mypro.last_name = request.POST.get("last_name")
            mypro.email = request.POST.get("email")
            mypro.photo = request.FILES.get("photo")
            mypro.phone = request.POST.get("phone")
            mypro.save()
            return redirect("dash")
        
        else:
            print("profile ou an pa ajoute patiza")
    else:
        myprofil = ProfileForm()
    context = {'myprofil': myprofil}
    return render(request, 'my_profile.html', context)

@login_required(login_url="authentificate")
def newProjects(request):
    if request.method == "POST":
        myprojects = ProjectForm(data=request.POST, files=request.FILES)
        if myprojects.is_valid():
            myprojects.cleaned_data.get('category')
            myprojects.cleaned_data.get('title')
            myprojects.cleaned_data.get('description')
            myprojects.cleaned_data.get('photo')
            
            mypro = myprojects.save(commit=False)
            mypro.user = request.user
            mypro.save()

            myprojects.save_m2m()
            #projects.category.add(category)
            

            return redirect("dash")
        else:
            print("project w lan pa ajoute nan base de donne an patizan")
        
    else:
        myprojects = ProjectForm()
    context = {'myprojects': myprojects}
    return render(request, 'allprojects.html', context)



