# Project_Multi_User_Blog
**Project 3 Udacity Full Stack Developer Nanodegree**

Built a multi user blog where users can sign in and post blog posts as well as
'Like' and 'Comment'.This blog is hosted on Google App Engine and an authentication system
was also created for users to be able to signup and sign in and then create blog posts!

**key words**: Python, Webapp2, jinja2, Google Cloud Platform,  Cloud Datastore

You can download all the files: $ git clone https://github.com/fwangboulder/Project_Multi_User_Blog.git

**How to run it locally?**
step 1: $ dev_appserver.py [your folder path]

        note: if you are right in the SinglePageBlog folder: $ dev_appserver.py ./

step 2: Go to the default url: localhost:8080

        note: if you want a different port number (ex. 9999),
        in step 1, use: $ dev_appserver.py --port=9999 ./

step 3: Go to url: localhost:8080/newpost

        add new post and submit it. Make sure you have both title and subject filled.

step 4: go back to url: localhost:8080 to check the history post.


**How to host it with Google APP Engine?**

step 1: Create a new project in your google app engine dashboard. Get your Project ID.

        My project ID is awesomewangblog.

step 2: Change the application (in app.yaml) to the your ID.

step 3: host it using Google App Engine

$ gcloud config set project awesomewangblog

$ gcloud beta app create

$ appcfg.py update [path]

step 4: browse it

$ gcloud app browse

**How to use the online version?**

My website link is: https://awesomewangblog.appspot.com

Sign up and enjoy your journey to write your blog!!!
