# -*- encoding: utf-8 -*-

{
    "name": "Hotel Management",
    "version": "1.3",
    "author": "Pragmatic TechSoft Pvt Ltd",
    'website': 'http://pragtech.co.in/',
    "category": "Generic Modules/Hotel Management",
    "description": """
    Enhance Property of hotel module.
    """,
    "depends": ["base", 'stock', "hotel", 'hotel_restaurant', 'hotel_housekeeping', 'sale_enhancement'],
    "init_xml": [],
    "demo_xml": [
    ],
    "data": [
        'security/hotel_management_security.xml',
        "security/ir.model.access.csv",
        'views/roomwise_guestwise_report_view.xml',
        'views/monthly_occupency_report_view.xml',

        'wizard/folio_cancel_wizard_view.xml',
        'wizard/issue_material_view.xml',
        'wizard/hotel_reservation_wizard.xml',
        "wizard/banquet_deposite_amt_view.xml",
        'wizard/advance_payment_wizard_view.xml',
        'wizard/folio_invoice_transfer_view.xml',
        'wizard/roomwise_guestwise_wizard.xml',
        "views/sale_view.xml",
        "views/hotel_management_view.xml",
        'views/hotel_housekeeping_view.xml',
        'data/hotel_housekeeping_data.xml',
        'views/hotel_management_sequence.xml',
        'views/agent_commission_view.xml',
        'views/res_config_view.xml',
        'wizard/arrival_departure_wizard.xml',
        'wizard/monthly_occupancy_wizard.xml',
        'report/hotel_folio_report_view.xml',
        'report/hotel_report_view.xml',
        'report/hotel_report.xml',
        'report/hotel_reservation_report.xml',
        'report/roomwise_guestwise_qweb.xml',
        'report/monthly_occupency_qweb.xml',
        'report/hotel_management_report.xml',
        'report/report_arrival_dept_guest.xml',
        'report/reservation_report_new.xml',
        'report/hotel_reservation_report.xml',
        'report/hotel_reservation_checkin_report.xml',
        'report/hotel_reservation_checkout_report.xml',
        'report/hotel_reservation_room_report.xml',
        'report/hotel_restaurant_order_kot_report.xml',
        'report/hotel_restaurant_order_bill.xml',
        'report/hotel_reservation_order_kot_report.xml',
        'report/hotel_reservation_order_bill.xml',
    ],

    # "js":['static/src/js/dashboard_url.js'],
    "active": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
