from odoo import models, fields, api

class Inventory_Reports(models.Model):
	_name='ilyn.inven.reports'
	_inherit='stock.quant'
	current_products = fields.Integer("Static Value")
	
	def get_product(self):
		current_products = self.search_read([], ['name'])
		prod_obj=self.pool.get(product.product)
		prod_name=prod_obj.browse(cr,uid,ids)[0].name



