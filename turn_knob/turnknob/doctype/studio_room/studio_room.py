# Copyright (c) 2025, Raghav Ruia & others and contributors
# For license information, please see license.txt

import frappe
# from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class StudioRoom(Document):

	# Set `name` of Studio Room
	def autoname(self):
		# Get object of Studio Property
		studio_property_parent_doc = frappe.get_doc("Studio Property", self.studio_property_id)

		# Count the existing Rooms in Property
		count_of_rooms = 0
		count_of_rooms = len(studio_property_parent_doc.list_of_rooms)
		
		# Set Serial Number for New Room by incrementing 1 & add leading zeros
		serial_no_of_new_room = str(count_of_rooms+1).zfill(4)

		# Set Room ID
		self.name = f"RID-[{self.studio_property_id}]-R{serial_no_of_new_room}"

	# Add Studio Room inheritance to Studio Property
	def after_insert(self): 
		room_id = self.name
		studio_property_id = self.studio_property_id

		# Get parent document
		studio_property_parent_doc = frappe.get_doc("Studio Property", studio_property_id)

		# Create Child Doc Instance
		studio_room_detail_child_doc = frappe.new_doc("Studio Room Detail")

		# Set value in the Child Doc
		studio_room_detail_child_doc.name_of_room = room_id

		# Add child table item to Studio Property
		studio_property_parent_doc.append("list_of_rooms", studio_room_detail_child_doc)

		studio_property_parent_doc.save()

	# Restrict Studio Room Size 
	def validate(self):
		if self.area_of_room_sq_ft < 25:
			frappe.throw("Area of Room must be greater than or equal to 25 sq. ft.")

	# Set Room Type, Inherit Studio Room Category to Studio Property
	def before_save(self):
		# Auto select the Room Size Type based on the "area_of_room_sq_ft" field
		if self.area_of_room_sq_ft >= 25 and self.area_of_room_sq_ft <= 75:
			self.room_size_type = "Cozy"
		elif self.area_of_room_sq_ft >= 76 and self.area_of_room_sq_ft <= 200:
			self.room_size_type = "Stretch"
		elif self.area_of_room_sq_ft > 200:
			self.room_size_type = "Grand"

		# Store Current Studio Room Activity Category
		list_of_category_inside_room = []
		for category in self.category_of_room:
			list_of_category_inside_room.append(category.studio_room_category)
		
		# Get Studio Property Object
		studio_property = frappe.get_doc("Studio Property", self.studio_property_id)

		# Get Activity Category already present in Studio Property
		list_of_category_inside_property = []
		for category in studio_property.suitable_for_category:
			list_of_category_inside_property.append(category.studio_room_category)

		# Find Activity Categories that exist in Studio Room but not in Studio Property
		new_categories = [category for category in list_of_category_inside_room if category not in list_of_category_inside_property]

		# Add non-exisiting activity categories to Studio Property
		for category in new_categories:
			studio_property.append("suitable_for_category", {
				"studio_room_category": category
			})

		# Save only if new items were added
		if new_categories:
			studio_property.save()
