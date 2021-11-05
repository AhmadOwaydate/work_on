
from odoo import api, fields, models


class TimsheetAddCategory(models.Model):
    _inherit = "account.analytic.line"
    _description = "Add the timsheet category  "
    category_id = fields.Many2one("timesheet.category", String="Category")

  #  def _compute_name(self):
  #     print("--------------------------------------------------------------------------------")
   #    for product in self.order_line:
   #        self.compound_name = product.name.split("]")
  #         print(f"------{compound_name}")
  #     print("--------------------------------------------------------------------------------")

  #  pro_forma_date = fields.Date(string="Pro-forma Date")
