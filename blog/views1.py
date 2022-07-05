from blog.models import users,posts
def loginrequired(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper
def loggeduser():
    username=session.get("user")
    userid=[user["id"] for user in users if user["name"]==username]
    return userid

def authenticate(**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data





session={}

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("successfully logged in")
        else:
            print("invalid credentials")

@loginrequired
def logout(*args,**kwargs):
    session.pop("user")
class PostListView:
    @loginrequired
    def get(self,*args,**kwargs):
        return posts

class MyPostView:
    @loginrequired
    def get(self,*args,**kwargs):
        userid=loggeduser()
        qs=[post for post in posts if post.get("userId")==userid][0]
        return qs
class postcreateview:
    @loginrequired
    def post(self,*args,**kwargs):
        userid=loggeduser()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userid,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")
class postdetailsview:
    @loginrequired
    def get(self,*args,**kwargs):
        postid=kwargs.get("id")
        qs=[p for p in posts if p.get("id")==postid]
        return qs
    def put(self,id=None,*args,**kwargs):
        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)


lo=SignInView()
lo.post(username="django",email="django@123")
pst=postcreateview()
pst.post(title="my post",body="this is my new post")
mp=MyPostView()
print(mp.get())
detail=postdetailsview()
detail.put(id=10,title="my post",body="it is my new post")






