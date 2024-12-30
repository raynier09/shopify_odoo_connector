/** @odoo-module **/

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { ListRenderer } from "@web/views/list/list_renderer";
import { ShopifyQueueDashboard } from '@shopify_odoo_connector/views/shopify_queue_dashboard';

export class QueueDashboardRenderer extends ListRenderer {};

QueueDashboardRenderer.template = 'shopify_odoo_connector.QueueListView';
QueueDashboardRenderer.components= Object.assign({}, ListRenderer.components, {ShopifyQueueDashboard})

export const QueueDashboardListView = {
    ...listView,
    Renderer: QueueDashboardRenderer,
};

registry.category("views").add("shopify_queue_dashboard_list", QueueDashboardListView);
