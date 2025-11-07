# Copyright (c) 2025, Raghav Ruia & others and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.website.website_generator import WebsiteGenerator

class StudioProperty(Document):
	# Add Studio Property to the child table in "Studio Partner"
	def after_insert(self): 
		property_id = self.name
		studio_partner_id = self.studio_partner_id

		# Get parent document
		studio_partner_parent_doc = frappe.get_doc("Studio Partner", studio_partner_id)

		# Create Child Doc Instance
		studio_property_detail_child_doc = frappe.new_doc("Studio Property Detail")

		# Set value in the Child Doc
		studio_property_detail_child_doc.name_of_property = property_id

		# Add child table item to Studio Partner
		studio_partner_parent_doc.append("list_of_properties", studio_property_detail_child_doc)

		studio_partner_parent_doc.save()
	
# @frappe.whitelist()
# def mark_properties_inactive(property_names):
# 	"""
# 	Marks selected properties and their rooms as inactive.
# 	"""
# 	disabled_properties = []
# 	disabled_rooms = []

# 	for property_name in property_names:
# 		# Get the document for property
# 		property_doc = frappe.get_doc("Studio Property", property_name)

# 		# Get the associated Studio Partner document
# 		studio_partner_doc = frappe.get_doc("Studio Partner", property_doc.studio_partner_id)

# 		# Get all rooms associated with the property
# 		for room in property_doc.list_of_rooms:
# 			# Update the Room and Room Detail status
# 			frappe.db.set_value("Studio Room", room.name_of_room, "is_active", "0")
# 			frappe.db.set_value("Studio Room Detail", room.name, "is_active", "0")
# 			disabled_rooms.append(room.name_of_room)

# 		# Update the Property status
# 		frappe.db.set_value("Studio Property", property_name, "is_active", "0")

# 		# Update the Studio Property Detail status
# 		for property in studio_partner_doc.list_of_properties:
# 			if property.name_of_property == property_name:
# 				frappe.db.set_value("Studio Property Detail", property.name, "is_active", "0")
		
# 		disabled_properties.append(property_name)

# 	frappe.db.commit()
# 	return {"properties": disabled_properties, "rooms": disabled_rooms}
