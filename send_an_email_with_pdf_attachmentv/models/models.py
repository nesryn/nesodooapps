# -*- coding: utf-8 -*-
import base64

from odoo import models, fields, api


class my_module(models.Model):
    _inherit = 'product.template'

    def send_email_with_attachment(self):
        report_template_id = self.env.ref(
            'send_an_email_with_pdf_attachment.action_report_product').render_qweb_pdf(self.id)
        data_record = base64.b64encode(report_template_id[0])

        ir_values = {
            'name': "Report",
            'type': 'binary',
            'datas': data_record,
            'store_fname': 'data_record',
            'mimetype': 'application/x-pdf',
        }
        data_id = self.env['ir.attachment'].sudo().create(ir_values)

        template = self.env.ref('send_an_email_with_pdf_attachment.report_template')

        template.attachment_ids = [(6, 0, [data_id.id])]
        email_values = {'email_to': self.env.user.email,
                        'email_from': self.env.user.email}
        template.sudo().send_mail(self.id, email_values=email_values, force_send=True)

        template.attachment_ids = [(3, data_id.id)]
        return True
