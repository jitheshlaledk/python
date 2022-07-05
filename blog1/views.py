from blog1.models import users,posts
session={}
def signinrequired(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper

def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("sucess")
        else:
            print("invalid")
class PostView:
    @signinrequired
    def get(self,*args,**kwargs):
        return posts

    @signinrequired
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        posts.append(kwargs)
        print("post added")
        print(posts)

class MyPostListView:
    @signinrequired
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        print(userId)
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts

class PostDetailsView:
    def get_object(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post

    @signinrequired
    def get(self,*args,**kwargs):
        post_id=kwargs.get("postId")
        post=self.get_object(post_id)
        return post

    @signinrequired
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=self.get_object(post_id)
        if data:
            post=data[0]
            posts.remove(post)
            print("post removed secessfully")
            print(len(posts))

    @signinrequired
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        instance=self.get_object(post_id)
        data=kwargs.get("data")
        if data:
            post_obj=instance[0]
            post_obj.update(data)
            print("post updated successfully")
            return post_obj

class LikedView:
    @signinrequired
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[ post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)


data={"title":"hello there"}

log=SignInView()
log.post(username="anu",password="Password@123")
s=PostView()
s.post()
# mypost=MyPostListView()
# mypost.get()
# postdetail=PostDetailsView()
# print(postdetail.put(post_id=4,data=data))
# like=LikedView()
# like.get(postid=7)
# postdetail.delete(post_id=4)
# print(postdetail.get(postId=6))

# print(session)
# data=PostView()
# print(data.get())
# data.post(psotId=9,
#           title="hello",
#           content="hello there",
# #           liked_by=[])





