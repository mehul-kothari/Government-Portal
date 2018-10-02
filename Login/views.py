import json

from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core import serializers
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import validate_email
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from Login.models import GeneralProblems, Likes, Notifications,SpecificProblems,Likes1,Likes2
from forms import *
from forms import PasswordResetRequestForm
from government.settings import DEFAULT_FROM_EMAIL

#notifications function. top 5.
def notifs(user1):
    all_notif = Notifications.objects.filter(user_create=user1).filter(checked=False).order_by('created')
    all_notif1 = Notifications.objects.filter(user_create=user1).order_by('created')
    all_notif3 = Notifications.objects.values_list('message').filter(user_create=user1).order_by('created')
    all_notif2 = Notifications.objects.values_list('message').filter(user_create=user1).order_by('message')
    notif4 = list((all_notif3))
    print(notif4)
    print(all_notif)

    print(list(all_notif2))
    count1 = all_notif.count()
    print(count1)

    count2 = all_notif1.count()
    print(count2)
    if count1 > 5:
        all_notif = all_notif[:5]
    if count2 > 5:
        notif4 = all_notif1[:5]
    else:
        notif4 = all_notif1[:count2]
    return notif4,count1
#about us page
def aboutus(request):
    context = RequestContext(request)
    return render_to_response('Login/abtus.html',{},context)


def simple(request):
    context = RequestContext(request)

    return render_to_response('Login/simplemap.html', context)
#filter using area and locality
def filters(request,area,loc,id):
    context = RequestContext(request)
    print(id)
    print(area)
    a = SpecificLocality.objects.all().count()
    print(a)
    loc1=Localities.objects.values('id').get(localities1=loc)
    print(loc1)
    b = SpecificLocality.objects.values('pk').filter(locality=loc1['id'])
    print(b)
    b1=[]
    if id=='2' or id=='1':


        count1=[]


        count2=[]
        user1=[]
        photo3=[]
        for i in b:
            print(i['pk'])

            if(id=='1'):
                count2.append(Discussion.objects.filter(detail_id=i['pk']).filter(type="spec").count())


            count1.append(Likes1.objects.filter(comment_id=i['pk']).count())
            user1.append(SpecificLocality.objects.values('user').filter(pk=i['pk']))
            #photo3.append(UserProfile.objects.filter(pk=i['pk']))

        print(user1)
        #print(photo3)
        user2=[]
        for i in user1:
            print(i[0])
            user3=i[0]

            user2.append(User.objects.values('username').filter(pk=user3['user']))
        print(user2)
        user4 = []
        for i in user2:
            print(i[0])
            user3 = i[0]

            user4.append(user3['username'])
        print(user4)

        user4 = [x.encode('UTF8') for x in user4]
        print(user4)
        for i in user4:
            i1=User.objects.values('pk').get(username=i)
            print(i1)
            photo3.append(UserProfile.objects.filter(user=i1['pk']))
        print("here it is man 1")
        print(photo3)

        print(count1)
        print(count2)
        count3=count1
        if(id=='1'):
            print("inside 1")
            count4=count2
            count5=count2
            count6 = count2
            sort1 = (sorted(count2, key=int))
            print(sort1)
            g = [b for (count2, b) in sorted(zip(count2, b))]
            print(g)
            sort=[count1 for (count4, count1) in sorted(zip(count4, count1))]
            print(sort)
            sort2=[user4 for (count5, user4) in sorted(zip(count5, user4))]

            sort3 = [photo3 for (count6, photo3) in sorted(zip(count6, photo3))]
        else:
            print("inside 2")
            print(count1)
            count2=count1
            sort = (sorted(count1, key=int))
            sort2=[user4 for (count1, user4) in sorted(zip(count1, user4))]
            sort3 = [photo3 for (count2, photo3) in sorted(zip(count2, photo3))]
            g = [b for (count3, b) in sorted(zip(count3, b))]


        print(sort2)
        print("here it is man 2")
        print(sort3)
        p2=[]
        for i in sort3:
            p1=i[0]
            print(p1)
            p2.append(p1)
        print(p2)
        p2=list(reversed(p2))
        print(p2)



        print(g)
        details1=[]
        heading1=[]

        for i in g:
            print(i['pk'])
            heading1.append(SpecificLocality.objects.values('heading').get(pk=i['pk']))
            details1.append(SpecificLocality.objects.values('comment').get(pk=i['pk']))
            likes2 = Likes1.objects.filter(user1=request.user).values_list('comment', flat=True)

        print(likes2)
        details2=[]
        print(heading1)
        print(details1)
        for i in details1:
            details2.append(i['comment'])
        print(details2)
        details3=[x.encode('UTF8') for x in details2]


        print(likes2)

        print(details3)
        print(count1)
        print(g)

        list1=zip(details3,sort,g,sort2,heading1,p2)

        list2=list(reversed(list1))
        print(list2)
        notif4,count1=notifs(request.user)
        print("here it is man")
        print(sort3)

        return render_to_response('Login/filters.html',
                                  {'list':list1,'id':id,'area':area,'loc':loc,'likes2':likes2,'all_notif1':notif4,'count1':count1}, context)
    else:
        return HttpResponseRedirect('/login/home/%s/%s/'%(area,loc))


    if(id=='1'):
        print(id)
        print(area)
        count1=[]
        for i in b:
            print(i['pk'])
            count1.append(Discussion.objects.filter(detail_id=i['pk']).filter(type="spec").count())
        print(count1)
    if(id==2):
        print("hello")
    return HttpResponse("hello")



def done(request,id):
    print(list(form2.objects.values('done').all()))
    print(id)
    b=form2.objects.get(pk=id)
    print(b)
    b.done=True
    b.save()
    print(list(form2.objects.values('done').all()))

    a = 2
    data = json.dumps(a)

    return HttpResponse(data, content_type='application/json')


def checked(request):
    notif=Notifications.objects.filter(user_create=request.user)
    print(notif)
    for i in notif:
        print(i.checked)
        i.checked=True
        print(i.checked)
        i.save()

    checked1=Notifications.objects.values('checked').filter(user_create=request.user)
    print(checked1)

    a=2
    data = json.dumps(a)

    return HttpResponse(data, content_type='application/json')
"""def spec_locality_discuss(request,area,loc,id):
    context = RequestContext(request)
    all_count = []
    form_comment = DiscussionForm(request.POST or None)
    print(problem)
    print(discuss_id)
    print(request.user.id)
    form_comment = DiscussionForm(request.POST or None)
    if form_comment.is_valid():
        instance = form_comment.save(commit=False)
        instance1 = Notifications()

        instance.user_write = request.user
        instance1.user_write = request.user
        instance.detail_id = discuss_id
        user2 = form2.objects.values('user').get(pk=discuss_id)
        print(user2['user'])
        user2 = User.objects.get(pk=user2['user'])

        instance.user_create = user2
        instance1.user_create = user2
        instance.save()
        message1 = "%s commented on your %s" % (request.user, problem)
        instance1.message = message1
        # instance1.save()
        instance1.urls1 = "/login/home/%s/%s_discuss/" % (problem, discuss_id)
        print(instance1.urls1)
        instance1.save()

    likes2 = Likes2.objects.filter(user1=request.user).values_list('comment', flat=True)
    all_comments = Discussion.objects.filter(detail_id=discuss_id)
    # print(all_comments[0].user_create)
    # print(all_comments)

    for k in all_comments:
        print(Likes2.objects.filter(comment__comment=k.comment).count())

        all_count.append(Likes2.objects.filter(comment__comment=k.comment).count())
        print(all_count)
    print(all_comments)
    list = zip(all_comments, all_count)
    print(list)
    # user2=form2.objects.get(pk=discuss_id).values('user1')

    # all_comments=Discussion.objects.filter(detail_id=discuss_id)


    # current_brand = VehicleBrand.objects.get(code=brand)

    return render_to_response('Login/discuss1.html',
                              {'form_comment': form_comment, 'list': list, 'all_comments': all_comments,
                               'likes2': likes2,
                               'problem': problem}, context)"""


def likeUpdate(user,id,choice,select):
    print("hello eveyone")
    print(id)

    a=Notifications()
    a.user_write=user
    if(select=="normal"):
        prob = form2.objects.values_list('genproblems').get(pk=id)
        print(prob)
        prob1 = GeneralProblems.objects.get(pk=prob[0])
        user2 = form2.objects.values_list('user').get(pk=id)
        print(user2)
        user3 = user2[0]
        print(user3)
        user2 = User.objects.get(pk=user3)
        a.urls1="http://127.0.0.1:8000/login/home/"+str(prob1)+"/#"+id
        print(a.urls1)
        print(list(Notifications.objects.values('message').all()))
    elif(select=="discussnormal"):
        user3 = Discussion.objects.values('user_create').filter(detail_id=id).filter(type="normal")
        user4=user3[0]
        user2 = User.objects.get(pk=user4['user_create'])
        print(user2)
        #a.urls1 = "http://127.0.0.1:8000/login/home/" + str(prob1) + "/"+ id+"_discuss"
    elif (select == "discussspec"):
        user2 = Discussion.objects.values_list('user_create').filter(detail_id=id).filter(type="spec")
        print(user2)


        user2 = User.objects.get(pk=user2)
        print(user2)
    else:
        user2= SpecificLocality.objects.values_list('user').get(pk=id)
        print("inside the 3 else")
        print(user2)
        user3 = user2[0]
        print(user3)
        user2 = User.objects.get(pk=user3)
    #user2 = User.objects.get(pk=user3[0])

    a.user_create = user2
    if(choice=="like"):
        message1 = "%s liked your post out here " % (user)
        a.message = message1
    if user2==user:
        print("same")
    else:

        print("about to save")
        a.save()




def profile(request,user1):
    context = RequestContext(request)
    users=[]
    usernames=[]
    problems=[]
    problems1 = []
    user5=User.objects.values('pk').get(username=user1)
    print(user5)
    likes=Likes.objects.filter(user1=user5['pk'])
    print(likes)
    details=Likes.objects.values('details').filter(user1=user5['pk'])
    #print(details)
    for i in details:
        #print(i)
        problems.append(form2.objects.values('genproblems').get(pk=i['details']))
        users.append(form2.objects.values("user").get(pk=i['details']))
    #print(problems)
    for i in problems:
        user2 = i
        #print(user2)
        problems1.append(GeneralProblems.objects.get(id=user2['genproblems']))
    #print(problems1)
    for i in users:
        user2=i
        #print(user2)
        usernames.append(User.objects.get(id=user2['user']))
    #print(usernames)
    #print(users)

    #print(likes)
    list=zip(usernames,problems1,details)
    print(list)
    problems2=[]
    ##########################################################done regarding likeeesss #####################################3
    ###discussion###
    comments = Discussion.objects.values_list('comment').filter(user_write=user1).filter(type="normal")
    ids = Discussion.objects.values_list('detail_id').filter(user_write=user1).filter(type="normal")

    print(ids)
    for i in ids:
        user2 = i[0]
        print(user2)
        problems2.append(form2.objects.values('genproblems').get(id=user2))
    print(problems2)
    problems3=[]
    for i in problems2:
        print(i)
        problems3.append(GeneralProblems.objects.get(id=i['genproblems']))
    print(problems3)
    user3 = Discussion.objects.values_list('user_create').filter(user_write=user1).filter(type="normal")


    print(comments)
    print(user3)
    j = 0
    usernames1 = []
    for i in user3:
        user2 = i[0]
        print(user2)
        usernames1.append(User.objects.get(id=user2))

    print(usernames1)
    list1 = zip(usernames1, problems3, ids)

    #photo1=UserProfile.objects.get(user=user1)
    pk1=User.objects.values_list('pk').get(username=user1)
    print(pk1)
    photo1=UserProfile.objects.get(user=pk1)
    print(photo1)
    area=Area.objects.get(user=pk1)
    loc = Locality.objects.get(user=pk1)
    all_posts=form2.objects.filter(user=pk1)
    all_done=form2.objects.values('done').filter(user=pk1)
    print(all_done)
    print(all_posts)
    list3=zip(all_posts,all_done)
    print(user1)
    print(request.user)

    user5=request.user
    if str(user1) == str(user5):
        checking=False
    else:
        checking=True
    print(checking)
    return render_to_response('Login/profile.html',{'user':user1,'checking':checking,'photo':photo1,'list':list,'list3':list3,'all_done':all_done,'list1':list1,'area':area,'loc':loc,'all_posts':all_posts,'usernames':usernames},context)

def spec_problem(request,area,loc,prob):
    context = RequestContext(request)
    j = 0
    all_count=[]
    all_comments2 = []
    #form_comment = Spec_LocalityForm(request.POST or None)
    locality1 = Locality.objects.get(user=request.user)
    locality2=Localities.objects.get(localities1=locality1)
    comment=SpecificLocality.objects.values('comment').filter(locality=locality2)
    form_comment = Spec_LocalityForm(request.POST or None)

    if form_comment.is_valid():
        instance = form_comment.save(commit=False)
        #instance1=Notifications()
        form_heading = request.POST.get("heading")
        instance.user=request.user
        #instance1.user_write = request.user
        area1=Area.objects.get(user=request.user)
        area2=Areas.objects.get(areas1=area1)
        instance.area=area2
        #user2=form2.objects.values('user1').get(pk=discuss_id)
        #print(user2['user1'])
        #user2=User.objects.get(pk=user2['user1'])
        locality1 = Locality.objects.get(user=request.user)
        locality2=Localities.objects.get(localities1=locality2)
        instance.locality=locality2
        instance.heading=form_heading

        instance.save()
        print("hello inside form validation")
        return HttpResponseRedirect('/login/home/%s/%s/'%(area,loc))

    print(locality1)
    print(comment)
    all_comments1 = SpecificLocality.objects.filter(locality=locality2).filter(comment__icontains=prob)
    print(all_comments1)
    """user2=[]
    for i in all_comments1:
        print("hello")
        if problem1.lower() in i.comment.lower():
            print(i.comment)
            all_comments2.append(str(i.comment))
            user2.append(SpecificLocality.objects.values('user').get(comment=i.comment))
            j = j + 1"""

    #print(user2)
            # current_brand = VehicleBrand.objects.get(code=brand)

    #print(j)
    #print(all_comments2)
    likes2 = Likes1.objects.filter(user1=request.user).values_list('comment', flat=True)
    print(likes2)
    for k in all_comments1:
        print(Likes1.objects.filter(comment__comment=k.comment).count())

        all_count.append(Likes1.objects.filter(comment__comment=k.comment).count())
        print(all_count)
    photos = []
    for i in all_comments1:
        print("inside")
        print(i.user)
        photos.append(UserProfile.objects.get(user=i.user))
    print(photos)

    list = zip(all_comments1, all_count,photos)
    notif4,count1=notifs(request.user)
    photo2=[]
    if request.user.is_authenticated:
        photo2 = UserProfile.objects.get(user=request.user)
        print("here is the fuck up")
        print(photo2)
    return render_to_response('Login/spec_prob.html',
                              {'all_comments1': all_comments1,'likes2':likes2,'photo2':photo2,'all_notif1':notif4,'count1':count1,'list':list,'form_comment':form_comment,'area':area,'loc':loc}, context)

def forum(request):
    context = RequestContext(request)
    return render_to_response('Login/forum_page.html',context)



def logout_view(request):
  auth.logout(request)
  # Redirect to a success page.
  return HttpResponseRedirect("/login/login1/")


@login_required(login_url='/example url you want redirect/')
def goback(request):
    return HttpResponseRedirect('/login/login1/')


def all_json_models1(request, problem1):
    j=0
    all_comments2=[]
    print(problem1)
    locality1 = Locality.objects.get(user=request.user)

    print(locality1)
    all_comments1=SpecificLocality.objects.filter(locality=locality1)
    print(all_comments1)
    for i in all_comments1:
        print("hello")
        if problem1.lower() in i.comment.lower():
            print(i.comment)
            all_comments2.append(str(i.comment))
            j=j+1
#current_brand = VehicleBrand.objects.get(code=brand)


    print(j)
    print(all_comments2)

    json_models = json.dumps(all_comments2)
    return HttpResponse(json_models)

def spec_locality(request,area,loc):
    context = RequestContext(request)
    if request.user.is_authenticated():
        photo2 = UserProfile.objects.get(user=request.user)
        print("here is the fuck up")
        print(photo2)
        print(area)
        all_count=[]
        print(loc)
        all_prob=SpecificProblems.objects.all()
        form_comment = Spec_LocalityForm(request.POST or None)
        form_heading = request.POST.get("heading")
        print(form_heading)
        if form_comment.is_valid():
            instance = form_comment.save(commit=False)
            #instance1=Notifications()

            instance.user=request.user
            #instance1.user_write = request.user
            area1=Area.objects.get(user=request.user)
            area2=Areas.objects.get(areas1=area1)
            print("chnaged")
            print(area2)
            instance.area=area2
            instance.heading=form_heading
            #user2=form2.objects.values('user1').get(pk=discuss_id)
            #print(user2['user1'])
            #user2=User.objects.get(pk=user2['user1'])
            locality1 = Locality.objects.get(user=request.user)
            locality2=Localities.objects.get(localities1=locality1)
            instance.locality=locality2
            instance.save()
        else:
            print form_comment.errors


        all_comments = SpecificLocality.objects.filter(locality__localities1=loc)
        print("all_comments")
        count1=all_comments.count()
        likes2 = Likes1.objects.filter(user1=request.user).values_list('comment', flat=True)
        for k in all_comments:
            print(Likes1.objects.filter(comment__comment=k.comment).count())

            all_count.append(Likes1.objects.filter(comment__comment=k.comment).count())
            print(all_count)
        photos=[]
        for i in all_comments:
            print("inside")
            print(i.user)
            photos.append(UserProfile.objects.get(user=i.user))
        print(photos)



        list = zip(all_comments, all_count,photos)
        notif4,count4=notifs(request.user)
        return render_to_response('Login/spec_locality1.html',
                                  {'form_comment': form_comment,'photo2':photo2,'list':list,'all_notif1':notif4.reverse(),'all_prob':all_prob,'count1':count1,'likes2':likes2,'area':area,'loc':loc,'count1':count4, 'all_comments': all_comments,
                                   }, context)
    else:
        return HttpResponseRedirect('/login/login1/')


def discuss(request, problem,discuss_id):
    gen=GeneralProblems.objects.all()
    print(gen)
    qs = GeneralProblems.objects.filter( problem=problem).values_list('problem', flat=True)
    #print(qs)
    #print(qs[0])
    context = RequestContext(request)
    all_count=[]
    form_comment = DiscussionForm(request.POST or None)
    print(problem)
    print(discuss_id)
    print(request.user.id)
    form_comment=DiscussionForm(request.POST or None)
    if form_comment.is_valid():
        instance = form_comment.save(commit=False)
        instance1=Notifications()

        instance.user_write=request.user
        instance1.user_write = request.user
        instance.detail_id=discuss_id
        if(qs.exists()):
            print("in gen")
            user2=form2.objects.values('user').get(pk=discuss_id)
            print(user2['user'])
            user2=User.objects.get(pk=user2['user'])
        else:
            print("in spec")
            user2 = SpecificLocality.objects.values('user').get(pk=discuss_id)
            print(user2['user'])
            user2 = User.objects.get(pk=user2['user'])
            instance1.type="spec"
            instance.type="spec"
            print(instance)

        instance.user_create=user2
        instance1.user_create = user2
        instance.save()
        message1="%s commented on your %s" % (request.user,problem)
        instance1.message=message1
        #instance1.save()
        instance1.urls1="http://127.0.0.1:8000/login/home/" + str(problem) + "/"+ discuss_id+"_discuss/"
        print(instance1.urls1)
        print(instance1)
        if(user2==request.user):
            print("same")
        else:

            instance1.save()

    #likes2 = Likes2.objects.filter(user1=request.user).fil.values_list('comment', flat=True)
    if (qs.exists()):
        likes2 = Likes2.objects.filter(user1=request.user).filter(type="normal").values_list('comment', flat=True)
        print(likes2)
        all_comments = Discussion.objects.filter(detail_id=discuss_id).filter(type="normal")
        photo3=[]
        photo4=[]
        print("in normal")
        for i in all_comments:
            photo4=Discussion.objects.values('user_write').filter(comment=i)
            print(photo4)
            photo1=photo4[0]
            photo2=User.objects.values('pk').get(username=photo1['user_write'])
            print(photo2['pk'])
            photo3.append(UserProfile.objects.get(user=photo2['pk']))
            print(photo3)
    else:
        likes2 = Likes2.objects.filter(user1=request.user).filter(type="spec").values_list('comment', flat=True)
        print(likes2)
        all_comments = Discussion.objects.filter(detail_id=discuss_id).filter(type="spec")
        print(all_comments)
        print("in spec")
        photo3=[]
        for i in all_comments:
            photo1 = Discussion.objects.values('user_write').get(comment=i)
            print(photo1)

            photo2 = User.objects.values('pk').get(username=photo1['user_write'])
            print(photo2['pk'])
            photo3.append(UserProfile.objects.get(user=photo2['pk']))
            print(photo3)


    #print(all_comments[0].user_create)
    #print(all_comments)

    for k in all_comments:
        print("for spec")
        print(Likes2.objects.filter(comment__comment=k.comment).count())

        all_count.append(Likes2.objects.filter(comment__comment=k.comment).count())
        print(all_count)
    print(all_comments)
    list = zip(all_comments, all_count,photo3)
    print(list)
    if (qs.exists()):
        old=form2.objects.get(pk=discuss_id)
        print(old)
        old_head=form2.objects.values_list("heading").get(pk=discuss_id)
        print(old_head[0])
        user1 = form2.objects.values_list("user").get(pk=discuss_id)
        old_photo=form2.objects.values("photo").get(pk=discuss_id)

        print(old_photo)
    else:
        old = SpecificLocality.objects.get(pk=discuss_id)
        print(old)
        old_head = SpecificLocality.objects.values_list("heading").get(pk=discuss_id)
        print(old_head[0])
        user1=SpecificLocality.objects.values_list("user").get(pk=discuss_id)
        old_photo=[]
    print(user1)
    user2=User.objects.get(pk=user1[0])
    user3=User.objects.values('username').get(pk=user1[0])
    print("printing user3")
    print(user3)

    image=UserProfile.objects.get(user=user2)
    print(image)
    notif4,count1=notifs(request.user)
    if request.user.is_authenticated:
        photo2 = UserProfile.objects.get(user=request.user)
        print("here is the fuck up")
        print(photo2)
    us=User.objects.values('pk').get(username=user3['username'])
    print(us)
    loc=Locality.objects.get(user=us['pk'])
    print(loc)
    area=Area.objects.get(user=us['pk'])
    print(area)
    #user2=form2.objects.get(pk=discuss_id).values('user1')

    #all_comments=Discussion.objects.filter(detail_id=discuss_id)


#current_brand = VehicleBrand.objects.get(code=brand)

    return render_to_response('Login/discuss1.html',
                              {'form_comment': form_comment,'area':area,'loc':loc,'list':list,'photo2':photo2, 'all_comments': all_comments,'likes2':likes2,
                               'problem': problem,'old':old,'old_head':old_head[0],'image':image,'user3':user3,'old_photo':old_photo,'all_notif1':notif4.reverse(),'count1':count1}, context)


def all_json_model(request, like):
    context = RequestContext(request)
    if request.user.is_authenticated():
        print(request.user)


        likes1=Likes.objects.all()
        likes2=Likes.objects.filter(user1=request.user).values_list('details', flat=True)
        details = form2.objects.get(id=like)

        if details.id in likes2:
            data1={
                'liked':'liked'
            }
            data = json.dumps(data1)

            return HttpResponse(data , content_type='application/json')


#current_brand = VehicleBrand.objects.get(code=brand)
        else :
            #details = form2.objects.get(id=like)
            details1=form2.objects.all()
            print(details)
            a=Likes()
            print(details)
            a.details=details
            print(details)
            a.user1=request.user
            a.likes=True
            a.save()
            b=Likes.objects.all()
            print(b)
            likeUpdate(request.user,like,"like","normal")
            print("after return")
            z=Likes.objects.filter(details=details).count()
            print("counting the fucking likes")
            print(z)

            #print(details)

            data1 = {
                'liked': 'nliked',
                'z':z
            }
            data = json.dumps(data1)
            print(data)


            return HttpResponse(data, content_type='application/json')
            #json_models= serializers.serialize("json", details1)
            #print(details)


    else:
        print("didnt happen")
        data1 = {
            'liked': 'not logged in'

        }
        data = json.dumps(data1)

        return HttpResponse(data, content_type='application/json')
        HttpResponseRedirect('/login/login1')

def all_json_models2(request, like):
    if request.user.is_authenticated():
        print(request.user)


        likes1=Likes1.objects.all()
        likes2=Likes1.objects.filter(user1=request.user).values_list('comment', flat=True)
        details = SpecificLocality.objects.get(id=like)

        if details.id in likes2:
            data1={
                'liked':'liked'
            }
            data = json.dumps(data1)

            return HttpResponse(data , content_type='application/json')


#current_brand = VehicleBrand.objects.get(code=brand)
        else :
            #details = form2.objects.get(id=like)
            details1=form2.objects.all()
            print(details)
            a=Likes1()
            print(details)
            a.comment=details
            print(details)
            a.user1=request.user
            a.likes=True
            a.save()
            likeUpdate(request.user,like,"like","specific")
            z = Likes1.objects.filter(comment=details).count()
            print("counting the fucking likes")
            print(z)

            #print(details)

            data1 = {
                'liked': 'nliked',
                'z':z
            }
            data = json.dumps(data1)

            return HttpResponse(data, content_type='application/json')
            #json_models= serializers.serialize("json", details1)
            #print(details)


    else:
        print("didnt happen")
        data1 = {
            'liked': 'not logged in'
        }
        data = json.dumps(data1)

        return HttpResponse(data, content_type='application/json')
        HttpResponseRedirect('/login/login1')


def all_json_models3(request, like,problem):
    gen=GeneralProblems.objects.all()
    print(problem)
    qs = GeneralProblems.objects.filter(problem=problem)
    print(qs)



    if request.user.is_authenticated():
        print(request.user)


        likes1=Likes2.objects.all()
        if qs.exists():
            print("in gen")
            likes2=Likes2.objects.filter(user1=request.user).filter(type="normal").values_list('comment', flat=True)
            print(likes2)
            details = Discussion.objects.filter(id=like).filter(type="normal")
            type1="normal"
        else:
            likes2 = Likes2.objects.filter(user1=request.user).filter(type="spec").values_list('comment', flat=True)
            details = Discussion.objects.filter(id=like).filter(type="spec")
            print(likes2)
            print(details)



#current_brand = VehicleBrand.objects.get(code=brand)

        #details = form2.objects.get(id=like)
        details1=form2.objects.all()
        print(details)
        a=Likes2()
        print(details)
        b=Discussion.objects.get(comment=details[0])
        a.comment=b
        print(details)
        a.user1=request.user
        if qs.exists():
            a.type="normal"
        else:
            a.type="spec"
        a.likes=True

        a.save()
        if (qs.exists()):
            print("in gen")
            detail1 = Discussion.objects.values('detail_id').get(pk=like)
            print("here is the detail id")
            print(detail1['detail_id'])
            likeUpdate(request.user,detail1['detail_id'],"like","discussnormal")
            z = Likes2.objects.filter(comment=details).filter(type="normal").count()
        else:
            print("in speccc")
            detail1=Discussion.objects.values('detail_id').get(pk=like)
            print("here is the detail id")
            print(detail1['detail_id'])
            likeUpdate(request.user, detail1['detail_id'], "like", "discussspec")
            z = Likes2.objects.filter(comment=details).filter(type="spec").count()


        print("counting the fucking likes")
        print(z)
        #print(details)

        data1 = {
            'liked': 'nliked',
            'z':z
        }
        data = json.dumps(data1)
        print(data)

        return HttpResponse(data, content_type='application/json')
            #json_models= serializers.serialize("json", details1)
            #print(details)


    else:
        print("didnt happen")
        data1 = {
            'liked': 'not logged in'
        }
        data = json.dumps(data1)

        return HttpResponse(data, content_type='application/json')
        HttpResponseRedirect('/login/login1')





def all_json_models(request, area):

#current_brand = VehicleBrand.objects.get(code=brand)

    models = Localities.objects.all().filter(areas2__areas1=area)
    print(models[0])

    json_models = serializers.serialize("json", models)

    return HttpResponse(json_models)



def form3(request,problem):


    context = RequestContext(request)
    image1=None
    likes2=[]

    #selected_item=1
    link=False


    if request.is_ajax():
        c=form2()
        object_name = request.POST.get('detail')
        print(object_name)
        c.likes="True"
        c.user1=request.user
        c.save()
        print(c.user1)
        return HttpResponse("hello")
    #selected_item = get_object_or_404(GeneralProblems, problem=request.POST.get('id_1'))
   # details_list = form2.objects.all().filter(genproblems=selected_item)
    #selected_item = get_object_or_404(GeneralProblems, problem=request.POST.get('id_1'))
    #details_list=form2.objects.all().filter(generalproblems=selected_item)
    #if request.method=="POST":
    form_details = form2form(request.POST)
    form_heading=request.POST.get("heading")
    print(form_heading)

    if form_details.is_valid():
        if request.user.is_authenticated():
            instance = form_details.save(commit=False)
            image1=request.FILES.get("problem_image")
            instance.photo=image1
            #form_details.save(commit=False)
            #selected_item = get_object_or_404(GeneralProblems, problem=request.POST.get('id_1'))
            #details_list = form2.objects.all().filter(genproblems=selected_item)

            #selected_item=str(selected_item)
            instance.heading=form_heading
            print(problem)
            a=GeneralProblems.objects.get(problem=problem)
            instance.genproblems=a
            instance.user=request.user
            instance.save()

            #a=form2()
            #a.details=form_details.details
            #selected_item = GeneralProblems.objects.get(problem=selected_item)
            #instance.genproblems=selected_item
            #print(instance.genproblems)
            #a.save()
            #instance.save()
            #form_details.genproblems=a.genproblems
            #print(form_details.genproblems)
            #form_details.save()
            #form_details.save()

    likes2 =[]
    notif4=[]

    if request.user.is_authenticated():
        likes2 = Likes.objects.filter(user1=request.user).values_list('details', flat=True)
        notif4,count1=notifs(request.user)
        print(count1)
        photo2 = UserProfile.objects.get(user=request.user)
        print("here is the fuck up")
        print(photo2)
    #selected_item = get_object_or_404(GeneralProblems, problem=request.POST.get('id_1'))
    all_details1=GeneralProblems.objects.values('pk').filter(problem=problem)

    likes1=Likes.objects.all()
    #likes2=Likes.objects.filter(user1=request.user).values_list('details', flat=True)

    print(likes1)

    print(all_details1)
    all_details = form2.objects.all().filter(genproblems=all_details1).order_by("-created")
    print(all_details)

    #likes2 = Likes.objects.filter(user1=request.user).values_list('details', flat=True)
    #print(Likes.objects.filter(details=all_details[]).count())
    print("trying")
    all_done = form2.objects.values("done").filter(genproblems=all_details1).order_by("-created")
    print(all_done)
    photos=[]
    j=0
    all_count=[]
    paginator = Paginator(all_details, 10)
    page = request.GET.get('page')
    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_details = paginator.page(paginator.num_pages)

    """count=all_details.count()
    limit = 5
    if count>=5:
        link=True
        all_details = all_details[count - limit:]
        all_done=all_done[count-limit:]"""

    for i in all_details:
        print("inside")
        print(i.user)
        photos.append(UserProfile.objects.get(user=i.user))
    print(photos)

    #all_counts=form2.objects.all().filter(genproblems=all_details1).annotate(num=Likes.objects.count())
    #print(all_counts[2].num)
    for k in all_details:
        print(k.id)
        print(Likes.objects.filter(details=k.id).count())

        all_count.append(Likes.objects.filter(details=k.id).count())
        print("all count")
        print(all_count)


    list = zip(all_details, all_count,photos,all_done)

    if request.user.is_authenticated():
        loc=Locality.objects.get(user=request.user)
        area=Area.objects.get(user=request.user)
    else:
        area="guest"
        loc="guest"
        photo2=[]
        count1=0



    #all_details = form2.objects.all()
    return render_to_response('Login/forum_page.html',
                              {'form_details': form_details,'area':area,'loc':loc,'photo2':photo2,'all_details':all_details,'all_count':all_count,'all_notif1':notif4.reverse(),'count1':count1,'list':list,'link':link,'problem':problem,'likes2':likes2,'user':request.user,'photos':photos,'image1':image1}, context)





def home(request):
    context = RequestContext(request)

    problems = GeneralProblems.objects.all()
    count3=Discussion.objects.all().count()
    print(count3)
    count4=form2.objects.all().count()
    count5=SpecificLocality.objects.all().count()
    count4=count4+count5
    print(count5)
    count6=User.objects.all().count()
    print(count6)
    count7=form2.objects.filter(genproblems=1).count()
    count8 = form2.objects.filter(genproblems=2).count()
    count9 = form2.objects.filter(genproblems=3).count()

    # Use Django's machinery to attempt to see if the username/password
    # combination is valid - a User object is returned if it is.

    if request.user.is_authenticated():
        all_notif=Notifications.objects.filter(user_create=request.user).filter(checked=False).order_by('created')
        all_notif1 = Notifications.objects.filter(user_create=request.user).order_by('created')
        all_notif3 = Notifications.objects.values_list('message').filter(user_create=request.user).order_by('created')
        all_notif2 = Notifications.objects.values_list('message').filter(user_create=request.user).order_by('message')
        notif4=list((all_notif3))
        print(notif4)

        print(all_notif)
        photo2=UserProfile.objects.get(user=request.user)
        #print("here is the fuck up")
        print(photo2)



        print(list(all_notif2))

        count1=all_notif.count()
        print(count1)

        count2 = all_notif1.count()
        print(count2)
        if count1>5:
            all_notif = all_notif[:5]
        if count2>5:
            notif4 = all_notif1[:5]
        else:
            notif4=all_notif1[:count2]
        current_user=request.user
        #problems=GeneralProblems.objects.all()
        area=Area.objects.filter(user=request.user)
        #print(area[0])
        loc=Locality.objects.get(user=request.user)
        print(loc)
        print("please send it please")
        return render_to_response('Login/home.html',
                                      {'username': current_user, 'p_all': problems, 'all_notif': all_notif.reverse(),'all_notif1': notif4.reverse(),
                                       'count1': count1, 'area': area[0], 'loc': loc,'count4':count4,'count3':count3,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'photo2':photo2}, context)

    else:
        current_user="Guest"
        all_notif=[]
        count1=0
        area="guest"
        loc="guest"
        photo2=[]
        return render_to_response('Login/home.html',
                                      {'username': current_user, 'p_all': problems, 'all_notif': all_notif.reverse(),
                                       'count1': count1, 'area': area, 'loc': loc,'count4':count4,'count3':count3,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'photo2':photo2}, context)



    #return render_to_response('Login/home.html',
                              #{'username': current_user, 'p_all':problems,'all_notif':all_notif.reverse(),'count1':count1,'area':area[0],'loc':loc}, context)

@csrf_exempt
def register_once(request):
    context = RequestContext(request)
    error_select = False
    error_select1 = False
    user_form=UserForm
    profile_form=UserProfileForm

    area_list=Areas.objects.all()
    object_name="hiiii"
    registered = False

    return render_to_response(
        'Login/register.html',
        {'user_form': user_form,'profile_form': profile_form, 'error_select':error_select,'error_select1':error_select1, 'registered': registered,'area_list':area_list},context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    register1=False

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(request.POST or None)
        profile_form = UserProfileForm(request.POST , request.FILES)
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        se=request.POST["area"]
        print(se)
        if(se=='Z'):
            error_select=True
            area_list = Areas.objects.all()
            return render_to_response('Login/register.html',
                                      {'user_form': user_form,'error_select':error_select ,'area_list':area_list,'registered': registered}, context)


        se2=request.POST["model"]
        print(se2)
        if(se2=='Z'):
            error_select1=True
            area_list = Areas.objects.all()
            return render_to_response('Login/register.html',
                                      {'user_form': user_form, 'error_select1':error_select1,'area_list':area_list,'registered': registered}, context)


        #area_form = AreaForm(request.POST or None)
        #ocality_form = LocalityForm(request.POST or None)


        #area = area_form.save(commit=False)
        print("some")

       # locality_form.save(commit=False)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            #profile_form = UserProfileForm(request.FILES['avatar'])
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            print("some")
            # Save the user's form data to the database.

            area=Area.objects.create(area1=se,user=user)
            se=Area.objects.get(user=user)
            locality=Locality.objects.create(area2=se,user=user,locality1=se2)
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
           # if 'picture' in request.FILES:
                #profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            #area.save()



            # Update our variable to tell the template registration was successful.
            registered = True
            register1=False
            return HttpResponseRedirect('/login/login1')
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors
            return render_to_response( 'Login/register.html',{'user_form': profile_form,'profile_form': user_form, 'registered': registered},context)


    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        area_form = AreaForm()
        locality_form=LocalityForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.



def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    next='login/home/'
    register1=False
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/login/home/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            register1=True
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            template=loader.get_template('Login/login1.html')
            return HttpResponse(template.render({'register1':register1},request))
            #return HttpResponseRedirect('/login/login1/')
            #return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('Login/login1.html', {'register1':register1,'next':next}, context)




class ResetPasswordRequestView(FormView):
    template_name = "Login/test_template.html"    #code for template is given below the view's code
    success_url = '/login/login1'
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):
        '''
        This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
        '''
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, *args, **kwargs):
        '''
        A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).
        '''
        form = self.form_class(request.POST)
        if form.is_valid():
            data= form.cleaned_data["email_or_username"]
        if self.validate_email_address(data) is True:                 #uses the method written above
            '''
        If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
            '''
            associated_users= User.objects.filter(Q(email=data)|Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                        c = {
                            'email': user.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': 'your site',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                            }
                        subject_template_name='Login/password_reset_subject.txt'
                            # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                        email_template_name='Login/password_reset_email.html'
                            # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                        subject = loader.render_to_string(subject_template_name, c)
                            # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'No user is associated with this email address')
            return result
        else:
            '''
            If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
            '''
            associated_users= User.objects.filter(username=data)
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        'email': user.email,
                        'domain': 'http://127.0.0.1:8000', #or your domain
                        'site_name': 'example',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
                    subject_template_name='Login/password_reset_subject.txt'
                    email_template_name='Login/password_reset_email.html'
                    subject = loader.render_to_string(subject_template_name, c)
                        # Email subject *must not* contain newlines
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'This username does not exist in the system.')
            return result
        messages.error(request, 'Invalid Input')

class PasswordResetConfirmView(FormView):
    template_name = "Login/test_template.html"
    success_url = '/admin/'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(request, 'The reset password link is no longer valid.')
            return self.form_invalid(form)

# Create your views here.
