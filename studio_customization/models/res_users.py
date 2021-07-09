from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    subscribed_to_confirmation_email = fields.Boolean(
        related="partner_id.subscribed_to_confirmation_email",
        readonly=False
    )

    field_efH4o = fields.Char(string='New Text', related="partner_id.field_efH4o")
    field_nKi0h = fields.Char(string='Customer Id Number', related="partner_id.field_nKi0h")
    customer_id = fields.Char(string='Customer id', related="partner_id.customer_id")
    phone2 = fields.Char(string='Phone2', related="partner_id.phone2")
    field_LMw5H = fields.Char(string='Customer id', related="partner_id.field_LMw5H")
    contact_name = fields.Char(string='Contact Name', related="partner_id.contact_name")
    second_contact_name = fields.Char(string='Second Contact Name', related="partner_id.second_contact_name")
    fax = fields.Char(string='Fax', related="partner_id.fax")
    pst_number = fields.Text(string='PST Number', related="partner_id.pst_number")
