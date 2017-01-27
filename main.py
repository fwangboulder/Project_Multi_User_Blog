#!/usr/bin/env python


#general
from webapp2 import WSGIApplication
from google.appengine.ext import db
from general import *         #general

#Models
from Models.user import User  #user
from Models.blog import *     #comment, like, post

#Handlers
from Handlers.helpers import *



#mapping the handlers

app = WSGIApplication([
    ('/', BlogFrontHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/newpost', NewPostHandler),
    ('/([0-9]+)', PostHandler),
    ('/([0-9]+)/like', LikePostHandler),
    ('/([0-9]+)/unlike', UnlikePostHandler),
    ('/([0-9]+)/edit', EditPostHandler),
    ('/([0-9]+)/delete/([0-9]+)', DeletePostHandler),
    ('/([0-9]+)/addcomment/([0-9]+)', AddCommentHandler),
    ('/([0-9]+)/([0-9]+)/editcomment/([0-9]+)', EditCommentHandler),
    ('/([0-9]+)/([0-9]+)/deletecomment/([0-9]+)', DeleteCommentHandler)
], debug=True)
