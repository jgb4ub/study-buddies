from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import User, Post, Message, Course, Group, Score, GroupMember

def index(request):
    return render(request, 'studyforum/index.html')

def post(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)

def groups(request):
    group_list = Group.objects.all()
    member_list = GroupMember.objects.all()
    context = {'group_list' : group_list, 'member_list' : member_list}
    return render(request, 'studyforum/groupings.html',context)

def profile_page(request, id):
    profile = User.objects.get(id=id)
    group_list = Group.objects.all()
    member_list = GroupMember.objects.all()
    context = {'profile': profile, 'group_list' : group_list, 'member_list' : member_list}
    return render(request, 'studyforum/profile_page.html', context)

def editprofile(request):
    return render(request, 'studyforum/edit_profile.html')

def editgroup(request,group_id):
    group = Group.objects.get(id=group_id)
    context = {'group': group}
    return render(request, 'studyforum/edit_group.html', context)

def profile_editor(request, id):
    profile = User.objects.get(id=id)
    username = request.POST.get("username", False)
    major = request.POST.get("major", False)
    phone = request.POST.get("phone", False)
    email = request.POST.get("email", False)
    discord_id = request.POST.get("discord", False)
    profile.username = username
    profile.major = major
    profile.phone = phone
    profile.email = email
    profile.discord_id = discord_id
    profile.save()
    return render(request, 'studyforum/profile_page.html', {'profile': profile})

def group_editor(request, group_id):
    new_group = Group.objects.get(id=group_id)
    new_group_name = request.POST.get("groupname", False)
    new_group_description = request.POST.get("groupdescription", False)
    new_group_discord_id = request.POST.get("groupdiscord", False)
    new_group.group_name = new_group_name
    new_group.group_description = new_group_description
    new_group.discord_link = new_group_discord_id
    new_group.save()
    group = Group.objects.get( id=group_id)
    member_list = GroupMember.objects.all()
    context = {'group' : group,'member_list' : member_list}
    return render(request, 'studyforum/grouppage.html', context)

def postsubmit(request):
    return render(request, 'studyforum/posting_submission.html')


def groupsubmit(request):
    return render(request, 'studyforum/group_submission_form.html')



def addpost(request, id):
    new_post_content = request.POST.get("question",False)
    new_post_subject = request.POST.get("submitter", False)
    new_post_discord = request.POST.get("discord", False)
    new_post_category = request.POST.get("category", False)
    new_user = User.objects.get(id=id).username
    new_post = Post(content = new_post_content, subject = new_post_subject, discord_link = new_post_discord, user_id = id, category = new_post_category, username = new_user)
    new_post.save()
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)

def addgroup(request, user_id):
    new_group_name = request.POST.get("groupname",False)
    new_course_name = request.POST.get("coursename",False)
    new_post_discord = request.POST.get("discord", False)
    new_phone = request.POST.get("phone", False)
    new_group_description = request.POST.get("groupdescription", False)
    new_creator = user_id
    new_group = Group(group_name = new_group_name, course = new_course_name, group_description = new_group_description, discord_link = new_post_discord, phone = new_phone, creator = new_creator)
    new_group.save()
    group_list = Group.objects.all()
    member_list = GroupMember.objects.all()
    #joingroup(request, user_id, new_group.id)
    context = {'group_list' : group_list, 'member_list' : member_list}
    return render(request,'studyforum/groupings.html',context)

def joingroup(request, user_id, group_id):
    group_members = GroupMember.objects.all()
    group = Group.objects.all().get(id = group_id)
    phone_send = group.phone
    state = False
    user_list = User.objects.all().get(id = user_id)
    new_name = user_list.username
    new_first_name = user_list.first_name
    new_last_name = user_list.last_name
    new_phone = user_list.phone
    new_discord = user_list.discord_id 
    new_email = user_list.email
    message_send = "Hello, " + new_first_name + " "+ new_last_name + " just joined your group! Phone: "+ new_phone+ " Discord ID: " + new_discord +" Email: " + new_email

    for e in GroupMember.objects.all():
        if(e.member_id == user_id and group_id == e.group_id):
            state = True
    if(state == False):
        new_group_member = GroupMember(first_name = new_name, group_id = group_id, member_id = user_id, user_first= new_first_name, user_last = new_last_name)
        new_group_member.save()
        new_score = Score(result = 20, message = message_send, phone = phone_send)
        new_score.save()
    group_list = Group.objects.all()
    member_list = GroupMember.objects.all()
    context = {'group_list' : group_list, 'member_list' : member_list}
    return render(request,'studyforum/groupings.html',context)

def postpage(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'studyforum/postpage.html',{'post': post})

def grouppage(request, group_id):
    group = Group.objects.get( id=group_id)
    member_list = GroupMember.objects.all()
    context = {'group' : group,'member_list' : member_list}
    return render(request, 'studyforum/grouppage.html', context)

def chat(request):
    return render(request, 'studyforum/chat.html')

def messages(request):
    user_messages = Message.objects.all()
    username_list = User.objects.all()
    context = {'username_list': username_list}
    return render(request, 'studyforum/sendchat.html', context)

def sendmessage(request):
    message_content = request.POST.get("message",False)
    new_message = Message(content = message_content)
    new_message.save()
    message_list = Message.objects.all()
    context = {'message_list': message_list}
    return render(request, 'studyforum/postings.html',context)

def messageReceived(request, user_id):
    user_messages = Message.objects.filter(recipient=user_id)
    message_list = user_messages.order_by('-time')
    return render(request, 'studyforum/receivechat.html', {'messages': message_list})

def coursesubmit(request):
    return render(request, 'studyforum/course_submission.html')

def addcourse(request, id):
    rating = request.POST.get("rating", False)
    new_course_name = request.POST.get("name",False)
    new_course_professor = request.POST.get("professor", False)
    new_course_time = request.POST.get("time", False)
    try:
        new_course = Course(name = new_course_name, professor = new_course_professor, time=new_course_time)
        new_course.save()
        user = get_object_or_404(User, id=id)
        user.courses.add(new_course)
        user.save
        if (rating == "5"):
            user.fives.add(new_course)
        elif (rating == "4"):
            user.fours.add(new_course)
        elif (rating == "3"):
            user.threes.add(new_course)
        elif (rating == "2"):
            user.twos.add(new_course)
        else:
            user.ones.add(new_course)
        return render(request, 'studyforum/index.html')
    except:
        return render(request, 'studyforum/course_enrollment.html')

def courseremoval(request):
    return render(request, 'studyforum/course_removal.html')

def removecourse(request, id):
    course_name = request.POST.get("name", False)

    try:
        course = get_object_or_404(Course, name=course_name)
        user = get_object_or_404(User, id=id)
        user.courses.remove(course)
        for i in user.fives.all():
            if i.name == course_name:
                user.fives.remove(i)
        for i in user.fours.all():
            if i.name == course_name:
                user.fours.remove(i)
        for i in user.threes.all():
            if i.name == course_name:
                user.threes.remove(i)
        for i in user.twos.all():
            if i.name == course_name:
                user.twos.remove(i)
        for i in user.ones.all():
            if i.name == course_name:
                user.ones.remove(i)
        return render(request, 'studyforum/index.html')
    except:
        return render(request, 'studyforum/index.html')


def courseenrollment(request):
    return render(request, 'studyforum/course_enrollment.html')

def enrollcourse(request, id):
    rating = request.POST.get("rating", False)
    course_name = request.POST.get("name", False)
    try:
        course = get_object_or_404(Course, name=course_name)
        user = get_object_or_404(User, id=id)
        user.courses.add(course)
        if (rating == "5"):
            user.fives.add(course)
        elif (rating == "4"):
            user.fours.add(course)
        elif (rating == "3"):
            user.threes.add(course)
        elif (rating == "2"):
            user.twos.add(course)
        else:
            user.ones.add(course)
        return render(request, 'studyforum/index.html')
    except:
        return render(request, 'studyforum/course_submission.html')
        #something new
        
def delete_post(request,id):
    post_to_delete=Post.objects.filter(id=id).delete()
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)