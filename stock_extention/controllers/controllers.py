# -*- coding: utf-8 -*-
# from odoo import http


# class StockExtention(http.Controller):
#     @http.route('/stock_extention/stock_extention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_extention/stock_extention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_extention.listing', {
#             'root': '/stock_extention/stock_extention',
#             'objects': http.request.env['stock_extention.stock_extention'].search([]),
#         })

#     @http.route('/stock_extention/stock_extention/objects/<model("stock_extention.stock_extention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_extention.object', {
#             'object': obj
#         })
