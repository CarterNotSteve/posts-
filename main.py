import os

un = input("username: ")

while 1:
    tmpposts = open("posts.posts", "r+")
    posts = tmpposts.readlines()
    
    def get_all():
        return posts[1:]

    def get_post(index):
        return posts[index+1]
    
    def make_post(un, message):
        tmpposts.write(un+": "+message)

    for i in posts[1:]:
        print(i.strip("\n"))

    
    term = input(un+" $~ ")
    cmd = term.split(" ")[0]
    args = term.split(" ")[1:]

    if cmd == "help":
        os.system('clear')
        print("""
Commands:
    post <post-content> *NOTE* Do not add quotes *NOTE*
    chun <new-name>
              """)

    elif cmd == "post":
        tmpposts.write("\n"+un+": "+" ".join(args))

    elif cmd == "chun":
        un = "_".join(args)

    elif cmd == "ratio":
        for i in args:
            if i.startswith("-index="):
                line = "".join(i[7:])
                line = int(line)
                posts[line+1] = ""
                tmpposts.seek(0)
                tmpposts.write("".join(posts))
    