# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
import collections
from collections import Counter


class product_static(models.AbstractModel):
    _name = "report.send_an_email_with_pdf_attachment.report_product"

    @api.model
    def _get_report_values(self, docids, data):
        product_ids = self.env['product.template'].search([], order="name desc")

        return  {
           'product':product_ids,
         }