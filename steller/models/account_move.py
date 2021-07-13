from odoo import models


class AccountBankStatement(models.Model):
    _name = "account.bank.statement"
    _inherit = ['account.bank.statement', 'mail.thread', 'mail.activity.mixin']
