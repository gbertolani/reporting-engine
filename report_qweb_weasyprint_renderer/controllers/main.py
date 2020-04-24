from odoo import http
from odoo.addons.web.controllers.main import ReportController
from odoo.http import request

class ReportControllerDisableWk(ReportController):

    @http.route(['/report/check_wkhtmltopdf'], type='json', auth="user")
    def check_wkhtmltopdf(self):
        # Bypass wkhtmltopdf check
        return 'ok'
