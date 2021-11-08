# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductCategoryGroup(models.Model):
    _name = 'product.category.group'
    _description = 'Grupo de categoría de producto'

    name = fields.Char(string='Descripción')