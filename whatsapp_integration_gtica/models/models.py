# -*- coding: utf-8 -*-

import logging
import urllib
import html2text
from odoo import http, models, fields, api, tools, _
from odoo.http import request

_logger = logging.getLogger(__name__)

class ConvertHtmlText(object):

    def convert_html_to_text(result_txt):
        capt = b'%s' % (result_txt)
        convert_byte_to_str = capt.decode('utf-8')
        return html2text.html2text(convert_byte_to_str)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def send_whatsapp_step_one(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp'),
                'res_model': 'send.whatsapp',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_partner_id': self.id, 'format_invisible': True},
                }

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def send_whatsapp_step_one(self):

        record = self.with_context(proforma=True)
        dominio = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url_preview = self.get_portal_url()
        format_url = '{}{}'.format(dominio, url_preview)

        result_txt = request.env['ir.ui.view'].render_template("whatsapp_integration_gtica.template_quote", {
            'doc_ids': self.ids,
            'doc_model': 'sale.order',
            'docs': record,
        })
        result_link = request.env['ir.ui.view'].render_template("whatsapp_integration_gtica.template_quote_link", {
            'doc_ids': self.ids,
            'doc_model': 'sale.order',
            'docs': record,
        })

        message_txt = ConvertHtmlText.convert_html_to_text(result_txt)
        message_link = ConvertHtmlText.convert_html_to_text(result_link)
        message_with_link = str(message_link).format(link =format_url)

        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp'),
                'res_model': 'send.whatsapp',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_partner_id': self.partner_id.id, 'message_txt': message_txt, 'message_link': message_with_link},
                }

    @api.multi
    def action_quotation_whatsapp(self):

        name = self.partner_id.name
        mobile = self.partner_id.mobile
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url_quote = '%s/quote/%s/%s' % (base_url, self.id, self.access_token)
        messege_contact = u'Hola estimado@ {}, hemos recibido su solicitud a través de nuestra Página Web.\
 Adjunto tiene a su disposión presupuesto por la Solución Contable y Administrativa de su interés. Si tiene \
dudas, con gusto le brindaremos todo nuestro apoyo para contestarlas. Cotización -> {}'.format(name, url_quote)
        print(messege_contact)
        code_url = urllib.parse.quote(messege_contact.encode('utf8'))
        messege_whatsapp = 'https://wa.me/{}?text={}'.format(mobile, code_url)


        return {'type': 'ir.actions.act_url',
                'url': messege_whatsapp,
                'nodestroy': True,
                'target': 'new'
                }

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def send_whatsapp_step_one(self):

        record = self.with_context(proforma=True)
        dominio = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url_preview = self.get_portal_url()
        format_url = '{}{}'.format(dominio, url_preview)

        result_txt = request.env['ir.ui.view'].render_template("whatsapp_integration_gtica.template_invoice", {
            'doc_ids': self.ids,
            'doc_model': 'sale.order',
            'docs': record,
        })
        result_link = request.env['ir.ui.view'].render_template("whatsapp_integration_gtica.template_invoice_link", {
            'doc_ids': self.ids,
            'doc_model': 'sale.order',
            'docs': record,
        })

        message_txt = ConvertHtmlText.convert_html_to_text(result_txt)
        message_link = ConvertHtmlText.convert_html_to_text(result_link)
        message_with_link = str(message_link).format(link =format_url)

        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp'),
                'res_model': 'send.whatsapp',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_partner_id': self.partner_id.id, 'message_txt': message_txt, 'message_link': message_with_link},
                }

class StockPickig(models.Model):
    _inherit = 'stock.picking'

    def send_whatsapp_step_one(self):

        record = self.with_context(proforma=True)

        result_txt = request.env['ir.ui.view'].render_template("whatsapp_integration_gtica.template_stock_picking", {
            'doc_ids': self.ids,
            'doc_model': 'sale.order',
            'docs': record,
        })

        message_txt = ConvertHtmlText.convert_html_to_text(result_txt)

        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp'),
                'res_model': 'send.whatsapp',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_partner_id': self.partner_id.id, 'message_txt': message_txt, 'format_invisible': True},
                }