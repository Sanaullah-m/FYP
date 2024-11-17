# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ItemAttribute(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.stock.doctype.item_attribute_value.item_attribute_value import ItemAttributeValue
		from frappe.types import DF

		attribute_name: DF.Data
		from_range: DF.Float
		increment: DF.Float
		item_attribute_values: DF.Table[ItemAttributeValue]
		numeric_values: DF.Check
		to_range: DF.Float
	# end: auto-generated types
	pass
