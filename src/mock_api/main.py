#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class BaggerMockApiApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            parts = (
                appier_extras.AdminPart,
            )
        )

if __name__ == "__main__":
    app = BaggerMockApiApp()
    app.serve()
