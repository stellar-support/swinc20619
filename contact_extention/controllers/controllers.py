# -*- coding: utf-8 -*-
# from odoo import http


# class ContactExtention(http.Controller):
#     @http.route('/contact_extention/contact_extention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_extention/contact_extention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_extention.listing', {
#             'root': '/contact_extention/contact_extention',
#             'objects': http.request.env['contact_extention.contact_extention'].search([]),
#         })

#     @http.route('/contact_extention/contact_extention/objects/<model("contact_extention.contact_extention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_extention.object', {
#             'object': obj
#         })
