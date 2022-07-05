from blog.models import users, posts

session = {}


def authenticate(**kwargs):
    username = kwargs.get("username")
    email = kwargs.get("email")
    user_data = [user for user in users if user["username"] == username and user["email"] == email]
    return user_data


def loginrequired(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("u must login")

    return wrapper


@loginrequired
def logged_user():
    username = session.get("user")
    user_id = [user["id"] for user in users if user["username"] == username][0]
    return user_id


class SignInView:
    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        user = authenticate(username="django", email="django@123")
        if user:
            print("sucess")
            session["user"] = username
        else:
            print("invalid credentials")


@loginrequired
def logout(*args, **kwargs):
    session.pop("user")


class PostListView:
    @loginrequired
    def get(self, *args, **kwargs):
        return posts


class MyPostView:
    @loginrequired
    def get(self, *args, **kwargs):
        user_id = logged_user()
        qs = [post for post in posts if post["userId"] == user_id]
        return qs


class PostCreateView:
    @loginrequired
    def post(self, *args, **kwargs):
        userId = logged_user()
        title = kwargs.get("title")
        body = kwargs.get("body")
        data = {"userId": userId,
                "title": title,
                "body": body}
        posts.append(data)
        print("post created successfully")


class PostDetailsView:
    @loginrequired
    def get(self, *args, **kwargs):
        post_id = kwargs.get("post_id")
        qs = [p for p in posts if p.get("id") == post_id]
        return qs

    def put(self, id=None, *args, **kwargs):
        pst = [p for p in posts if p.get("id") == id][0]
        title = kwargs.get("title")
        body = kwargs.get("body")
        pst["title"] == title
        pst["body"] == body


er = SignInView()
er.post(username="django", email="django@123")
po = PostCreateView()
po.post(title="mypost", body="this is my new post")
mp = MyPostView()
print(mp.get())
details = PostDetailsView()
print(details.get(post_id=10))

details.put(id=10, title="new data", body="this is new")
print(details.get(post_id=10))
