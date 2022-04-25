# -*- coding: utf-8 -*-
import time
from odoo import fields, models, api


class arrival_dept_guest_wizard(models.TransientModel):
    _name = 'arrival.dept.guest.wizard'
    _description = 'Daily Customer Arrival/ Departure List'

    date_start = fields.Date(
        'From Date', default=lambda *a: time.strftime('%Y-%m-%d'), required=True)
    arrival_dept = fields.Selection([('arrival', 'Customer Arrival'), (
        'depart', 'Customer Departure')], string='Report For', default=lambda *a: 'arrival', required=True)


    # @api.multi
    def print_report(self):
        datas = {}
        return self.env.ref('hotel_management.report_arrival_dept_guest').report_action(self, data=datas, config=False)

        
