from psycopg2.extensions import AsIs
from odoo import tools
from odoo import api, fields, models


class ReportDwjo(models.Model):
    _name = "report.dwjo"
    _description = "Suggested Reorder Report"
    _auto = False
    _order = 'name'

    name = fields.Char(
        string='Reference', readonly=True, help="Used to indicate the product code or reference.")
    sale_months_6 = fields.Float(
        readonly=True, group_operator="sum", help="It expresses the quantity of the product sold in the last 6 months")
    sale_months_2 = fields.Float(
        readonly=True, group_operator="sum", help="It expresses the quantity of the product sold in the last 2 months")
    sale_months_last = fields.Float(
        readonly=True, group_operator="sum", help="It expresses the quantity of the product sold in the last month")
    sale_weeks_2 = fields.Float(
        readonly=True, group_operator="sum", help="It expresses the quantity of the product sold in the last 6 weeks")
    qty_hand = fields.Float(
        readonly=True, group_operator="sum", help="Quantity on hand of the product that can be sold")
    qty_order = fields.Float(
        readonly=True, group_operator="sum", help="Quantity of the product ordered in purchases awaiting entry")
    qty_reserved = fields.Float(
        readonly=True, group_operator="sum", help="Quantity of the product reserved to be dispatched to the customer")

    def _select(self):

        select_str = """
            with dwjo as (
                                (select ail.product_id as id,
                                sum (case
                                        when i.date_invoice > current_date - interval '6 months' then ail.quantity
                                        else 0
                                    end) as quantity_6,
                                sum (case
                                        when i.date_invoice > current_date - interval '2 months' then ail.quantity
                                        else 0
                                    end) as quantity_2,
                                sum (case
                                        when i.date_invoice > current_date - interval '1 months' then ail.quantity
                                        else 0
                                    end) as quantity_1,
                                sum (case
                                        when i.date_invoice > current_date - interval '2 weeks' then ail.quantity
                                        else 0
                                    end) as quantity,
                                0 as qty_hand,
                                0 as qty_order,
                                0 as qty_reserved
                                from account_invoice_line as ail
                                inner join account_invoice as i on i.id = ail.invoice_id
                                group by ail.product_id,
                                qty_hand,
                                qty_order,
                                qty_reserved)
                            union
                                (select sq.product_id as id,
                                0 as quantity_6,
                                0 as quantity_2,
                                0 as quantity_1,
                                0 as quantity,
                                sq.quantity as qty_hand,
                                0 as qty_order,
                                0 as qty_reserved
                                from stock_quant as sq
                                inner join stock_location as sl on sl.id = sq.location_id
                                where sl.usage = 'internal')
                            union
                                (select sm.product_id as id,
                                0 as quantity_6,
                                0 as quantity_2,
                                0 as quantity_1,
                                0 as quantity,
                                0 as qty_hand,
                                sum(coalesce(sm.product_uom_qty, 0)) as qty_order,
                                0 as qty_reserved
                                from stock_move as sm
                                inner join stock_location as slo on slo.id = sm.location_id
                                inner join stock_location as sld on sld.id = sm.location_dest_id
                                where slo.usage != 'internal'
                                    and sld.usage = 'internal'
                                    and sm.state in ('confirmed',
                                                    'assigned')
                                group by sm.product_id,
                                quantity_6,
                                quantity_2,
                                quantity_1,
                                quantity,
                                qty_hand,
                                qty_reserved)
                            union
                                (select sml.product_id as id,
                                0 as quantity_6,
                                0 as quantity_2,
                                0 as quantity_1,
                                0 as quantity,
                                0 as qty_hand,
                                0 as qty_order,
                                sum(coalesce(sml.product_uom_qty, 0)) as qty_reserved
                                from stock_move_line as sml
                                inner join stock_location as slo on slo.id = sml.location_id
                                inner join stock_location as sld on sld.id = sml.location_dest_id
                                where slo.usage = 'internal'
                                    and sld.usage != 'internal'
                                group by sml.product_id,
                                quantity_6,
                                quantity_2,
                                quantity_1,
                                quantity,
                                qty_hand,
                                qty_order))
            select min(p.id) as id,
            case
                when p.default_code is not null then concat('[', p.default_code, ']', ' ', pt.name)
                else pt.name
            end as name,
            sum(quantity_6) as sale_months_6,
            sum(quantity_2) as sale_months_2,
            sum(quantity_1) as sale_months_last,
            sum(quantity) as sale_weeks_2,
            sum(qty_hand) as qty_hand,
            sum(qty_order) as qty_order,
            sum(qty_reserved) as qty_reserved
            from product_product as p
            left join dwjo as d on p.id = d.id
            inner join product_template as pt on pt.id = p.product_tmpl_id
            group by p.id,
            pt.name
            order by p.id
        """
        return select_str

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            )""", (AsIs(self._table), AsIs(self._select())))


class ReportDwjoPdf(models.AbstractModel):
    _name = "report.stellar.report_dwjo"
    _description = "Suggested Reorder Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        products = self.env['report.dwjo'].search([('id', 'in', docids)])
        return {
            'doc_ids': docids,
            'docs': products,
            'doc_model': 'report.dwjo',
        }
