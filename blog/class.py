class Ide:
    def functionalities(self):
        funcs=["create file","rename","debug"]
        return funcs
class pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("excecute")
        funcs.append("delete")
        return funcs
class VsCode(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("vcs")
        funcs.append("formatting")
        return funcs
m=pycharm()
print(m.functionalities())
s=VsCode()
print(s.functionalities())