from blog.models import users, posts


def login_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("u must login")

    return wrapper


def authenticate(**kwargs):
    username = kwargs.get("username")  # .get used for avoid error:it return none
    email = kwargs.get("email")
    user_data = [user for user in users if user['username'] == username and user['email'] == email]
    return user_data


def logged_user():
    username = session.get("user")
    userid = [user["id"] for user in users if user["name"] == username][0]
    return userid


session = {}


class SigninView:
    def post(self, *args, **kwargs):
        user_name = kwargs.get("username")
        email = kwargs.get("email")
        user = authenticate(username=user_name, email=email)
        if user:
            print("sucess")
            session["user"] = user_name
        else:
            print("invalid credentials")


@login_required
def logout(*args, **kwargs):
    session.pop("user")


class PostListView:
    @login_required
    def get(self, *args, **kwargs):
        return posts


class MyPostsView:
    @login_required
    def get(self, *args, **kwargs):
        userid = logged_user()
        qs = [p for p in posts if p.get("userId") == userid][0]
        return qs


class PostCreateView:
    @login_required
    def post(self, *args, **kwargs):
        userId = logged_user()
        title = kwargs.get("title")
        body = kwargs.get("body")

        data = {
            "userid": userId,
            "title": title,
            "body": body
        }
        print(data)
        posts.append(data)
        print("post created successfully")


class postdetailsview():
    @login_required
    def get(self, *args, **kwargs):
        postId = kwargs.get("id")
        qs = [p for p in posts if p.get("id") == postId]
        return qs

    def put(self, id=None, *args, **kwargs):
        post = [p for p in posts if p.get("id") == id][0]
        title = kwargs.get("title")
        body = kwargs.get("body")
        post["title"] = title
        post["body"] = body
        print(post)


lo = SigninView()
lo.post(username="django", email="django@123")
pst = PostCreateView()
pst.post(title="my post", body="this is my post")

detail = postdetailsview()
detail.put(id=10, title="my post", body="tis is my new post")
mp = MyPostsView()
print(mp.get())


pl = PostListView()
s = pl.get()
# try:
#     allposts=pl.get()
# except Exception as e:
#     print(e)
