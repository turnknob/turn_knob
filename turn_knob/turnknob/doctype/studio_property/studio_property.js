// Copyright (c) 2025, Raghav Ruia & others and contributors
// For license information, please see license.txt

frappe.ui.form.on("Studio Property", {
	// onload(frm) {

	// },
    refresh(frm) {
        if (frm.is_new()) {
            frm.toggle_display("room_details_section", false);
            frm.toggle_display("activity_details_section", false);
            frm.toggle_display("inventory_items_at_studio_section", false);
        }

        if (!frm.is_new()) {
        frm.add_custom_button(__("Create Room"), () => {
            frappe.new_doc("Studio Room", {
                studio_property_id: frm.doc.name
            });
        });
        }
	},
});
