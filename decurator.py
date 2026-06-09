def login_required(func):
    def waraper():
        is_login =True
        print("hello")
        if is_login:
            func()
        else:
            print("login required")
    return waraper

@login_required
def dasboard():
    print("well come to dasboard")
dasboard()