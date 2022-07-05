def admin_permission_required(fn):
    def inner_function(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "admin":
            raise Exception("permission denied")
        else:
            return fn(*args, **kwargs)

    return inner_function


class user:
    def setuser(self, username, role):
        self.username = username
        self.role = role

    def print(self):
        print(self.username, self.role)


class add_course:
    def set_course(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def print(self):
        print(self.course_name)


class add_batch:
    def set_batch(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.batch_code = kwargs.get("b_code")
        self.course = kwargs.get("course")

    def print(self):
        print(self.batch_code)
