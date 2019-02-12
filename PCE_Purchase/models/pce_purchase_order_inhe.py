from odoo import api, fields, models

class purchase_order_inhe(models.Model):
    _inherit = "purchase.order"
    
    deliver_term_id=fields.Many2one('delivery_term.master',string='Delivery Term')
    transport_mode_id=fields.Many2one('transport_mode.master',string='Transport Mode')
    