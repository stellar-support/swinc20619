# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderExtention(http.Controller):
#     @http.route('/sale_order_extention/sale_order_extention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_extention/sale_order_extention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_extention.listing', {
#             'root': '/sale_order_extention/sale_order_extention',
#             'objects': http.request.env['sale_order_extention.sale_order_extention'].search([]),
#         })

#     @http.route('/sale_order_extention/sale_order_extention/objects/<model("sale_order_extention.sale_order_extention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_extention.object', {
#             'object': obj
#         })
