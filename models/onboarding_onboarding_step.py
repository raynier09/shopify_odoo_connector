# -*- coding: utf-8 -*-

from odoo import api, models


class OnboardingStep(models.Model):
    _inherit = 'onboarding.onboarding.step'

    @api.model
    def shopify_instance_action(self):
        return self.env.ref('shopify_odoo_connector.shopify_instance_action_form_view').sudo().read()[0]

    @api.model
    def action_shopify_settings(self):
        return self.env.ref('shopify_odoo_connector.action_shopify_settings').sudo().read()[0]

    @api.model
    def shopify_financial_status_action(self):
        return self.env.ref('shopify_odoo_connector.shopify_financial_status_action').sudo().read()[0]

    # TODO: Future Roadmap
    @api.model
    def action_scheduler_configuration(self):
        # Add some view for scheduler configuration
        return self.env.ref('shopify_odoo_connector.action_shopify_settings').sudo().read()[0]