# -*- coding: utf-8 -*-
# from odoo import http


# class AccountExtention(http.Controller):
#     @http.route('/account_extention/account_extention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_extention/account_extention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_extention.listing', {
#             'root': '/account_extention/account_extention',
#             'objects': http.request.env['account_extention.account_extention'].search([]),
#         })

#     @http.route('/account_extention/account_extention/objects/<model("account_extention.account_extention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_extention.object', {
#             'object': obj
#         })
