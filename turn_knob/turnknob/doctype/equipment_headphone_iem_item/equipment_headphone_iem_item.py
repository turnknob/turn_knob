# Copyright (c) 2025, Raghav Ruia & others and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EquipmentHeadphoneIEMItem(Document):
	def before_save(self):
		self.full_equipment_name = f"{self.brand_name} {self.model_number} ({self.type})"
