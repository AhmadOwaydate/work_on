# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TimesheetCategory(models.Model):
    _name = "timesheet.category"
    _description = "A timsheet category name and code "

    name = fields.Char(String="Category name")
    code = fields.Char(String="Category code")
    timesheets_ids = fields.One2many("account.analytic.line", "category_id", string="Appointments")




#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100