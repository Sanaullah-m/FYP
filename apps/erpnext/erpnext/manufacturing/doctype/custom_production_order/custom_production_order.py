# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CustomProductionOrder(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.selling.doctype.sales_order_item.sales_order_item import SalesOrderItem
		from frappe.types import DF

		amended_from: DF.Link | None
		company: DF.Link
		item: DF.Table[SalesOrderItem]
		naming_series: DF.Literal["MFG-PP-.YYYY.-"]
		posting_date: DF.Date
		production_type: DF.Literal["Make-to-Order", "Make-to-Stock"]
		sales_order: DF.Link
	# end: auto-generated types
	pass
