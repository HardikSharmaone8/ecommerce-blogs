from django.shortcuts import render,redirect, HttpResponse
from .models import DatabaseBlog, PublishBlog, Comments, Publish_Comments
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def show_blog(request):
    #display database blogs logic
    all_blog =[]
    blog_title = DatabaseBlog.objects.values('BlogTitle')
    blog_title_setComprehension = {item['BlogTitle'] for item in blog_title}

    # display user blog logic
    user_blog = PublishBlog.objects.values('Blogger_Title')
    # print("creating blog by the user",user_blog)
    user_posted_blog = user_blog.values()
    # print("adfasfdsjklfaskdhfdshhf",user_posted_blog)
    for cat in blog_title_setComprehension:
        get_all_blog_category_data = DatabaseBlog.objects.filter(BlogTitle=cat)
        # print(get_all_blog_category_data.values())

        all_blog.append([get_all_blog_category_data.values,user_posted_blog])


    # print("Value of all Blog0",all_blog)
    params = {
        "blogDetails" : all_blog
    }
    # print(params)
    return render(request,'blog/index.html',params)

def show_blog_details(request,myid):
    parti_blog = DatabaseBlog.objects.filter(id=myid)
    # print("jsdfkjs;kljaslfjlsdk;lsjf",parti_blog)

    # sending comment in conetentdetails.html file
    show_comment = Comments.objects.filter(Product_Id=myid,Parent=None)
    show_reply = Comments.objects.filter(Product_Id=myid).exclude(Parent=None)  #show_reply variable me only reply store honge means jha jha pr parent none hoga wo wala reply yha store hoga
    # print("show reply",show_reply)
    # print("show comment",type(show_comment))

    params ={"particular_blog":parti_blog,"show_comment":show_comment,"show_reply":show_reply}


    return render(request,'blog/contentdetails.html',params)

def show_user_blog_details(request,myid):
    parti_blog = PublishBlog.objects.filter(id=myid)
    # print("jsdfkjs;kljaslfjlsdk;lsjf", parti_blog)

    # sending comment in conetentdetails.html file
    show_comment = Publish_Comments.objects.filter(Product_Id=myid, Parent=None)
    show_reply = Publish_Comments.objects.filter(Product_Id=myid).exclude(Parent=None)  # show_reply variable me only reply store honge means jha jha pr parent none hoga wo wala reply yha store hoga
    # print("show reply", show_reply)
    # print("show comment", type(show_comment))

    params = {"particular_blog": parti_blog, "show_comment": show_comment,"show_reply":show_reply}

    return render(request,'blog/userContentDetails.html',params)

def search(request):

    blog_searched_value = request.GET.get('search','')
    all_blog = []

    # when user search blog in published blog database
    user_blog = PublishBlog.objects.values('Blogger_Title')
    user_blog_setComprehension = {item['Blogger_Title'] for item in user_blog}

    for blog in user_blog_setComprehension:
        get_all_userblog_data = PublishBlog.objects.filter(Blogger_Title=blog)
        # print("GET_ALL_USERBLOG_DATA",get_all_userblog_data[0].Author_Name)
        if blog_searched_value in get_all_userblog_data[0].Author_Name.lower() or blog_searched_value in get_all_userblog_data[0].Blogger_Content.lower() or blog_searched_value in get_all_userblog_data[0].Blogger_Title.lower():
            all_blog.append(get_all_userblog_data)

    # logic when user search blof in database
    blog_title = DatabaseBlog.objects.values('BlogTitle')
    blog_title_setComprehension = {item['BlogTitle'] for item in blog_title}
    for cat in blog_title_setComprehension:
        get_all_blog_data = DatabaseBlog.objects.filter(BlogTitle=cat)
        # print("Get_All_BLOG_DATA",get_all_blog_data[0].BlogAuthor)
        if blog_searched_value in get_all_blog_data[0].BlogDetails.lower() or blog_searched_value in get_all_blog_data[0].BlogTitle.lower() or blog_searched_value in get_all_blog_data[0].BlogMoral.lower() or  blog_searched_value in get_all_blog_data[0].BlogAuthor.lower():
            all_blog.append(get_all_blog_data)


    # print("Value of all Blog0", all_blog)

    # print(len(all_blog))
    if len(all_blog) == 0:
        check = True
        return render(request, 'blog/search.html', {"check":check})
    else:
        params = {
            "blogDetails": all_blog
        }
        # print(params)
        return render(request, 'blog/search.html', params)




def createblog(request):
    if request.method == "POST":
        author_name = request.POST.get('author_name','')
        email= request.POST.get('email','')
        blog_title = request.POST.get('title','')
        content = request.POST.get('content','')
        image = '/shop/image/' + request.POST.get('pic','')
        print("l;asjf;lasjf;lajsdf;lajsdfl;kjasflk;jsaddfkl;jklasdfjlj lkdsajf sdjafj aljfkfjlas;dj                               jasddfkl;sadfkl;jsdakljksdfjlkdfjfjksdjklfsdajaa            ;ajfjksdfjkajfkjk;lfj;kkfaljfk;lfasdfljf;lsdaj",image)
        postBlog = PublishBlog(Author_Name=author_name,Blogger_Email=email,Blogger_Title=blog_title,Blogger_Content=content,Blog_Image=image)
        postBlog.save()

        check = True
        return render(request, 'blog/createblog.html',{ "check" : check })


    return render(request,'blog/createblog.html')

def comment(request):
    if request.method == 'POST':
        # print("heeloo")
        comment_id = request.POST.get('product_comment_id','')
        # print("commentId",comment_id)
        comment_by_user = request.POST.get('comment_text','')
        active_user = request.user  #what particular user comment shows this line
        post = DatabaseBlog.objects.get(id = comment_id)  #this line shows all the post of that particular product in which user comment
        parentSno = request.POST.get('product_reply_id')
        # print("parentsno",parentSno)

        if parentSno == None:
            parentSno = 0
            comments = Comments(Product_Id=comment_id, Reply_id=parentSno, Comment=comment_by_user, User=active_user, Post=post)
            comments.save()
            messages.success(request, 'Your comment has been posted successfully')
            return redirect(f'/blog/contentdetails/{comment_id}')
        else:
            parent = Comments.objects.get(Sno = parentSno)
            # print("parent",parent)
            comments = Comments(Product_Id=comment_id, Reply_id=parentSno, Comment=comment_by_user, User=active_user, Post=post, Parent=parent)
            comments.save()
            messages.success(request, 'Your reply has been posted successfully')

            return redirect(f'/blog/contentdetails/{comment_id}')




def publish_comment(request):
    if request.method == 'POST':
        # print("heeloo")
        comment_id = request.POST.get('product_comment_id','')
        # print("commentId",comment_id)
        comment_by_user = request.POST.get('comment_text','')
        active_user = request.user  #what particular user comment shows this line
        user_post = PublishBlog.objects.get(id = comment_id)#this line shows all the post of that particular product in which user comment
        parentSno = request.POST.get('product_reply_id')
        # print("parentsno",parentSno)

        if parentSno == None:
            parentSno = 0
            comments = Publish_Comments(Product_Id=comment_id, Reply_id=parentSno, Comment=comment_by_user, User=active_user, Post_Comment_On_User_Blog=user_post)
            comments.save()
            messages.success(request, 'Your comment has been posted successfully')
            return redirect(f'/blog/userContentDetails/{comment_id}')
        else:
            parent = Publish_Comments.objects.get(Sno = parentSno)
            # print("parent",parent)
            comments = Publish_Comments(Product_Id=comment_id, Reply_id=parentSno, Comment=comment_by_user, User=active_user,Post_Comment_On_User_Blog=user_post, Parent=parent)
            comments.save()
            messages.success(request, 'Your reply has been posted successfully')


            return redirect(f'/blog/userContentDetails/{comment_id}')





def signup(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        confirmpassword = request.POST.get('confirmpassword','')

       # signup form validation at database

        if len(username) <= 6:
            messages.error(request,'User Name Must be greater than 6 charactors')
            return redirect('/blog/content')

        elif username.find('0') == -1  and username.find('1') == -1  and username.find('2') == -1  and username.find('3') == -1  and username.find('4') == -1  and username.find('5') == -1  and username.find('6') == -1 and username.find('7') == -1  and username.find('8') == -1  and username.find('9') == -1:
            messages.error(request,"Username Must be Unique So, use Digits with username and if contain than don't use space in username")
            return redirect('/blog/content')

        elif username.find(" ") >= 0:
            messages.error(request,"Create user name without space")
            return redirect('/blog/content')

        elif len(firstname) <= 2 or len(lastname) <= 2:
            messages.error(request,'First or Last name must be greater than two charactors')
            return redirect('/blog/content')

        elif firstname.find(" ") >=0 or lastname.find(" ") >=0:
            messages.error(request,'First or Last name must not contain any space')

        elif firstname.find('0') > -1 or firstname.find('1') >-1 or firstname.find('2') >-1 or firstname.find('3') >-1 or firstname.find('4') > -1 or firstname.find('5') > -1 or firstname.find('6') > -1 or firstname.find('7') > -1 or firstname.find('8') > -1 or firstname.find('9') > -1:
            messages.error(request,"First name must not contain any digit")
            return redirect('/blog/content')

        elif lastname.find('0') > -1 or lastname.find('1') > -1 or lastname.find('2') > -1 or lastname.find('3') > -1 or lastname.find('4') > -1 or lastname.find('5') > -1 or lastname.find('6') > -1 or lastname.find('7') > -1 or lastname.find('8') > -1 or lastname.find('9') > -1:
            messages.error(request,"Last name must not contain any digit")
            return redirect('/blog/content')

        elif password.isalnum() == True:
            messages.error(request,'Password must contains special charactors like !,@,#,%,$,,*,_,- ')
            return redirect('/blog/content')

        elif len(password) <= 5:
            messages.error(request,'Password must be greater than 5 charactors')
            return redirect('/blog/content')

        elif password != confirmpassword:
            messages.error(request,'Confirm passoword not match with password')
            return redirect('/blog/content')

        else:
            messages.success(request,'Your Form successfully Saved in our database')
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            return redirect('/blog/content')

    return HttpResponse('404 - Page Not Found')


def userLogin(request):
    if request.method == "POST":
        login_username = request.POST.get('loginusername','')
        login_password = request.POST.get('loginpassword','')

        loginUser = authenticate(username = login_username, password = login_password)
        #this login_user return none if username or password not match with our database

        if loginUser is not None:
            login(request,loginUser)
            messages.success(request,'Successfully LoggedIn')
            return redirect('/blog/content')

        else:
            messages.error(request,'Please check your login details..and try after some time')
            return redirect('/blog/content')

    return HttpResponse('404 - Page not found')

def userLogout(request):
    logout(request)
    messages.success(request,'Successfully logout...')
    return redirect('/blog/content')