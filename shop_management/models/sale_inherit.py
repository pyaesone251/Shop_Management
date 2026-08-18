from odoo import api,fields,models

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    custom_remark = fields.Char('Custom Remark')