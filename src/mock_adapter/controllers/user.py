#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

import models

class UserController(appier.Controller):

    @appier.route("/login/", "GET")
    def login(self):
        #self.url_for("admin.login_api", username = "root", password = "root")
        bag = models.Bag.new()
        bag.id = self.session.sid
        print self.session
        bag.save()
