# importing these to, do task as their names suggest
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render, HttpResponse

# importing models or tables
from .models import Contact,Register

# importing user, that will provide us authentication model
from django.contrib.auth.models import User

#this helps in encdoing the password 
from django.contrib.auth.hashers import check_password,make_password

# messages on returned pages are shown with the help of this module
from django.contrib import messages

#this helps us in getting date and time , whne user logged in, when signed up, when send us the message 
from datetime import datetime

# this helps un in loggin in, loggin out of the user ID.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .forms import *






# Create your views here.
def welcome(request):
    return HttpResponse('''<h1>Hello Django Home</h1> <a href="/home">home</a> <br> <a href="/courses">courses</a> <br> <a href="/login">login</a>''')

def home(request):
    # if user is logged in, Dont let him access this page, as this will have no use for him/her     
    if not request.user.is_anonymous:
        messages.success(request, "Already Logged in, Let's get started.")
        
        # and redirect to strted page....
        return redirect('/started')
    return render(request, 'home.html')


# loin system for user.....
def login(request):
    # if user hasn't logged in, it will not let anyone access the restricted pages pages
    if not request.user.is_anonymous:
        messages.success(request, "Already Logged in.")

        email = None
        email = request.user.get_username()
        user = Register.objects.get(email=email)
        return redirect('/started')

    # accessing form
    if request.method == "POST":
        loginID = request.POST.get('loginID')
        password = request.POST.get('password')
    

        email = loginID + "@pucit.edu.Pk"
        email = email.upper()
    
        # this is built-in authentication system by django, that checks if the user exists or not
        user = authenticate(username=email, password=password)

        # id user exists then proceed
        if user is not None:

            # built-in by django that requests user and log ins.
            auth_login(request, user)

            # requesting user object, which has just logged in
            user1 = request.user

            # getting user, in register-form/table/model
            user = Register.objects.get(email = user1.username)

            # all this was to set the user-main id in register form (foreign key wala seen )  
            user.userMain_id = user1.id

            # here we save the the object, (actually saving userMain ID)
            user.save()

            messages.success(request, "Welcome You've Successfully Logged-in tho theeta.com :)")
            return redirect('/started')
        else:
            messages.success(request, "Wrong Login ID or Password")
    return render(request, 'login.html')


def logout(request):
    # django built in logout functionality, if logs out user from session.
    auth_logout(request)
    messages.success(request, "Logged out successfully :)")
    return redirect("/home")

def started(request):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect('/login')


    user=None
    if request.user.is_authenticated:
        email = request.user.username
        user = Register.objects.get(email=email)
    params = {"user":user,}
    print(user.designation)
    return render(request, 'welcome.html', params)



def register(request):
    # checking if the user has logged in, don't let him access this age
    if not request.user.is_anonymous:
        messages.success(
            request, "Already Logged in, Logout to create other account.")
        email = None
        email = request.user.get_username()
        user = Register.objects.get(email=email)
        return redirect('/started')


    # now checking REGISTER FORM, and getting post requests from form
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        id = request.POST.get('roll')
        roll = id.upper()

        isRollValid = False

        # input validation on Roll no or INPUT ID
        if len(roll) == 10:
            if roll[0] == 'B' or roll[0] == 'M':
                if (roll.index("IT") == 1) or (roll.index("CS") == 1) or (roll.index("SE") == 1):
                    if roll[3] == 'F':
                        if int(roll[4:6]) > int(16) or int(roll[4:6]) < int(21):
                            if roll[6] == 'M' or roll[6] == 'A':
                                if int(roll[7:10]) > int(1) or int(roll[7:10]) < int(600):
                                    isRollValid = True

        if isRollValid is not True:
            messages.success(request, "Invalid College ID")
            return redirect('/register')

        email = roll + "@pucit.edu.pk"
        email = email.upper()
        # emial wil be saved in batabase CAPATILIZED

        # dealing with passwords
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            messages.success(
                request, "Passwords Don't Match, kindly Enter same password in both fields!")
            return render(request, 'register.html')

        # if len(password) < 8 or len(password) > 20:
        #     messages.success(
        #         request, "Passwords not in range of 8 - 20 characters!")
        #     return render(request, 'register.html')
        # designations

        joinas = request.POST.get('joinas')
        if joinas == "none":
            messages.success(
                request, "Kindly select why you wanna join theeta.com ")
            return render(request, 'register.html')

        # T & C
        if request.POST.get('chk', "off") == "off":
            messages.success(request, "Please agree to our terms and conditions.")
            return redirect('/login')

        # calling object og User (model / class/ table)
        if User.objects.filter(username=email).exists():
            messages.success(request, "User Already Exists")
            return redirect('/register')


        register= Register(email=email,first_name=fname, last_name=lname, password=password1, designation=joinas,date_registered = datetime.now())

        # saving to database, the validated response
        register.save()

        password1 = make_password(password)
        user = User(username=email, password=password1,first_name=fname, last_name=lname)
        user.save()



        messages.success(
            request, "Your Account has been created Successfully, Login HERE;)")
        return redirect('/login')
    return render(request, 'register.html')

def about(request):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    return render(request, 'about.html')


def contact(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if request.POST.get('selectPurpose') == "Choose...":
            messages.success(
                request, "Kindly Select Why you want to message us. :(")
            return render(request, 'contact.html')

        purpose = request.POST.get('selectPurpose')
        desc = request.POST.get('desc')
        user = Register.objects.get(email=request.user.get_username())
        myID = user.id

        # passing elements to contact class/model/table to set values
        contact = Contact(first_name=fname, last_name=lname, purpose=purpose, message=desc, date_registered=datetime.now(),register_id=myID)
        
        # saving contact 
        contact.save()
        messages.success(request, "Your Message has been sent Successfully ;)")
        


    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)
    params = {"user":user,}
    return render(request, 'contact.html', params)

def adminSite(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")

    countUser = Register.objects.all().count()

    last = Register.objects.last()
    totalRegUsers = last.id

    countContacted = Contact.objects.all().count()

    loginUsers = Register.objects.all()
    contactedUsers = Contact.objects.all()

    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)

    fname=None
    if request.user.is_authenticated:
        fname = request.user.get_short_name()
    params = {
            "first_Name":fname,
            "Total_registered_users":totalRegUsers,
            "Total_Active_users":countUser,
            "Total_Contacts":countContacted,
            "Display_Users":loginUsers,
            "Contacted_Users":contactedUsers,
            "user":user,
            }
    return render(request, 'adminSite.html', params)

def userProfile(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)
    params = {"user":user,}
    return render(request, 'userProfile.html', params)

def contribute(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")
    
    


    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)
        params = {"user":user,}

        if user.designation == 'Editor' or user.designation == 'Contributor':
            return render(request, 'contribute.html', params)
        else:
            messages.success(request, f"Sorry, your designation is {user.designation}, only 'Editors' and 'Contributors' can contribute here....")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 

# courses
def courses(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")

    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)
    params = {"user":user,}
    return render(request, 'courses.html', params)

# subjects
def calculus(request,pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    user=None
    contrib = None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)

        contrib = Contributions.objects.all().filter(courseTitle_id = 3)

    params = {
                "user":user,
                "contrib":contrib,
                }
    return render(request, 'calculus-1.html', params)

def emt(request, pk):
    if request.user.is_anonymous:

        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    #for showing name on lgogout button 
    user=None
    contrib = None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)

        contrib = Contributions.objects.all().filter(courseTitle_id = 2)

    params = {
                "user":user,
                "contrib":contrib,
                }
    return render(request, 'electricity-and-magnetism.html', params)

def itc(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    user=None
    contrib = None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)

        contrib = Contributions.objects.all().filter(courseTitle_id = 1)

    params = {
                "user":user,
                "contrib":contrib,
                }
    return render(request, 'Intro-to-Computing.html', params)

def statistics(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    user=None
    contrib = None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)

        contrib = Contributions.objects.all().filter(courseTitle_id = 5)

    params = {
                "user":user,
                "contrib":contrib,
                }
    return render(request, 'Prob-and-Statistics.html', params)

def ww(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    user=None
    contrib = None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)

        contrib = Contributions.objects.all().filter(courseTitle_id = 4)

    params = {
                "user":user,
                "contrib":contrib,
                }
    return render(request, 'writing-workshop.html', params)

def userProfileEdit(request,pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")


    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)
    params = {"user":user,}
    return render(request, 'userProfileEdit.html', params)

def userProfileEditAdmin(request,pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")

    user=None
    if request.user.is_authenticated:
        user = Register.objects.get(id=pk)
    params = {"user":user,}
    return render(request, 'userProfileEditAdmin.html', params)

def updateUserData(request, pk):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        pic = request.POST.get('profile_pic')
        print("Pic: ",pic)
        if pic != '':
            form = profilePic(request.POST, request.FILES) 
            if form.is_valid():
                user = Register.objects.get(id = pk)
                user.profile_pic = form.cleaned_data['profile_pic']
                print(user.profile_pic)
                print(user.profile_pic.url)
                user.save()

        # image dealing
        user = Register.objects.get(id=pk)

        user.first_name = fname
        user.last_name = lname
        user.password = password
        user.save()

        password = make_password(password)  

        userLogin = User.objects.get(username=user.email)
        userLogin.first_name = fname
        userLogin.last_name = lname
        userLogin.password = password
        userLogin.save()
        
        messages.success(request, "Updated Successfully. Log-in again to see updations..")
        return redirect(f'/login')
    return render(request, 'welcome.html')

def updateUserDataAdmin(request, pk):
    if request.method == 'POST':
        designation = request.POST.get('joinas')


        # image dealing
        user = Register.objects.get(id=pk)
        user.designation = designation
        user.save()

        
        messages.success(request, "Updated Successfully. Log-in again to see updations..")
        # return redirect(f'/login')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 
    return render(request, 'welcome.html')

def deleteUser(request, pk):
    if request.user.is_anonymous:
        messages.success(request, "Log-in First to Continue :)")
        return redirect("/login")
    

    # ask = input("Really Wanna Delete User ?(Y/n)")
    ask = 'Y'
    if ask == 'Y':
        user = Register.objects.get(id = pk)
        mail = user.email

        user2 = User.objects.get(username=mail)
        user2.delete()

        messages.success(request, f"User with ID {mail} has removed from the theeta.com's Database.")
        logout(request)

        return redirect('/home')
    return redirect('/started')


def delete(request, pk):
     
    user=None
    user = Register.objects.get(id=pk)
    params = {"user":user,}
    return render(request, 'delete.html', params)


def makeContribution(request, pk):
    if request.method == 'POST':

        author_name = request.POST.get('author_name')
        title = request.POST.get('title')
        content_type = request.POST.get('theItems')
        courseName = request.POST.get('selectCourse')
 
        # contributor_name = request.user.get_fullname()
        contribution_link = request.POST.get('contrib_link')



        print(content_type)
        print(courseName)



        cont = ContributionFileType.objects.get(contFileType=content_type)
        contCourse = Courses.objects.get(courseTitle=courseName)

        content = Contributions(author_name=author_name, contribution_title=title, contribFileType_id=cont.id,contribution_link=contribution_link, register_id=pk, courseTitle_id=contCourse.id)
        content.save()
       
        form = contributionFile(request.POST, request.FILES) 
        if form.is_valid():
            mail = request.user
            mail.username
            register = Register.objects.get(id = pk)
            contrib = register.contributions_set.last()
            contrib.contribution_file = form.cleaned_data['contribution_file']
            contrib.save()

        # content.save()

        

        messages.success(request, "Thanks for sharing, Your content is successfully added.")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 
    messages.success(request, "Contribution Failed.")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 



