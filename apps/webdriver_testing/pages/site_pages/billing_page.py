#!/usr/bin/env python


from apps.webdriver_testing.pages.site_pages import UnisubsPage
import requests

class BillingPage(UnisubsPage):
    """Billing page, available only to is_superuser users.

    """

    _URL = "admin/billing/"
    _TEAM = "select#id_team"
    _START = "input#id_start_date"
    _END = "input#id_end_date"
    _TYPE = "select#id_type"
    _SUBMIT = "button.green_button"
    _LATEST_REPORT = "tbody tr:nth-child(1) td:nth-child(6) a"

    def open_billing_page(self):
        self.open_page(self._URL)


    def submit_billing_parameters(self, team, start, end, bill_type):
        self.select_option_by_text(self._TEAM, team)
        self.type_by_css(self._START, start)
        self.type_by_css(self._END, end)
        self.select_option_by_text(self._TYPE, bill_type)
        self.submit_by_css(self._SUBMIT)

    def check_latest_report_url(self):
        self.logger.info(self.get_text_by_css(self._LATEST_REPORT))
        url = self.get_element_attribute(self._LATEST_REPORT, 'href')
        self.logger.info('Getting content and headers of latest link')
        r = requests.get(url)
        billings = []
        for l in r.iter_lines():
            billings.append(l)
        return billings
