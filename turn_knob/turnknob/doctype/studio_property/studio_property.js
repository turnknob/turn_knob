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
    branch_name(frm) {
        // let studio_brand_name = frm.fields_dict['studio_partner_id'].disp_area.innerText;
        frm.set_value("property_name", `${frm.doc.studio_partner_name} (${frm.doc.branch_name})`);
    }
});
