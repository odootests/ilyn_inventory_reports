from odoo import models, fields, api

class Inventory_Reports(models.Model):
	_name='ilyn.inven.reports'
	_inherit='stock.inventory'
	current_product_id = fields.Integer("Static Value")
	# def get_product(self):
		# current_product_id = self.env['product.product'].browse(PRODUCT_ID)

