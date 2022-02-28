from markupsafe import Markup
from num2words import num2words

from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_html(self, data):
        if data:
            return Markup(data)
        return ''

    def get_discount(self):
        discount = 0.0
        for order in self:
            for line in order.order_line:
                discount += line.price_unit * (1 * line.discount / 100.0)
        return discount

    def get_total(self, total):
        if total:
            t_amount = 0.0
            total_amount = total.split(' ')
            if total_amount:
                t_amount = float(total_amount[0].replace(',', '')) - self.get_discount()
                return str(t_amount) + total_amount[1]
            else:
                return total

class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_html(self, data):
        if data:
            return Markup(data)
        return ''

    def convert_money_to_word(self, data):
        return num2words(data)

    def get_discount(self):
        discount = 0.0
        for invoice in self:
            for line in invoice.invoice_line_ids:
                discount += line.price_unit * (1 * line.discount / 100.0)
        return discount

    def get_total(self, total):
        if total:
            t_amount = 0.0
            total_amount = total.split(' ')
            if total_amount:
                t_amount = float(total_amount[0]) - self.get_discount()
                return str(t_amount) + total_amount[1]
            else:
                return total