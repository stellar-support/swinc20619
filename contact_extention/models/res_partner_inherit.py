from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    contact_name = fields.Char(
        string='Contact Name',
        required=False)

    customer_id = fields.Char(
        string='Customer Id',
        required=False)

    fax = fields.Char(
        string='Fax',
        required=False)

    field_LMw5H = fields.Char(
        string='Customer Id',
        required=False)

    field_efH4o = fields.Char(
        string='New Text',
        required=False)

    field_nKi0h = fields.Char(
        string='Customer Id Number',
        required=False)

    phone2 = fields.Char(
        string='Phone 2',
        required=False)

    pst_number = fields.Text(
        string='PST Number',
        required=False)

    second_contact_name = fields.Char(
        string='Second Contact Name',
        required=False)