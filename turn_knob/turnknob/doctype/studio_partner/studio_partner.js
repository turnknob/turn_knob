// Copyright (c) 2025, Raghav Ruia & others and contributors
// For license information, please see license.txt

frappe.ui.form.on("Studio Partner", {
	refresh(frm) {        
        if (frm.is_new()) {
            frm.toggle_display("partner_status_section", false);
            frm.toggle_display("property_details_section", false);
        }
        if (!frm.is_new()) {
            // Property Button Actions
            frm.add_custom_button(__("Create Property"), () => {
                frappe.new_doc("Studio Property", {
                    studio_partner_id: frm.doc.name
                });
            });
        }
    }
    //          // Add the custom button under the "Property" dropdown
    //     frm.add_custom_button(__("Mark as Inactive"), () => {
    //         // Check if there are properties to show
    //         frappe.db.get_list("Studio Property", {
    //             filters: {
    //                 studio_partner_id: frm.doc.name,
    //                 is_active: ["!=", 0]
    //             },
    //             fields: ["name", "property_name"]
    //         }).then(properties => {
    //             if (properties.length === 0) {
    //                 frappe.msgprint(__("No active properties found for this Studio Partner."));
    //                 return;
    //             }
                
    //             // Open the multi-select dialog
    //             const d = new frappe.ui.form.MultiSelectDialog({
    //                 doctype: "Studio Property",
    //                 target: frm,
    //                 setters: {
    //                     studio_partner_id: frm.doc.name
    //                 },
    //                 get_query: () => {
    //                     return {
    //                         filters: {
    //                             studio_partner_id: frm.doc.name,
    //                             is_active: ["!=", 0]
    //                         }
    //                     };
    //                 },
    //                 action: (selections) => {
    //                     if (!selections || selections.length === 0) {
    //                         frappe.msgprint(__("No properties selected."));
    //                         d.hide();
    //                         return;
    //                     }
                        
    //                     // Show the confirmation dialog
    //                     frappe.confirm(
    //                         __("This will mark the property & all the rooms inside the property as inactive. Do you want to proceed?"),
    //                         () => {
    //                             // On confirmation, execute the server-side function
    //                             frappe.call({
    //                                 method: "mark_properties_inactive",
    //                                 args: {
    //                                     property_names: selections
    //                                 },
    //                                 callback: (r) => {
    //                                     if (r.message) {
    //                                         let disabled_props = r.message.properties;
    //                                         let disabled_rooms = r.message.rooms;
                                            
    //                                         // Prepare HTML message for frappe.msgprint
    //                                         let message = `
    //                                             <p>Successfully marked the following documents as inactive:</p>
    //                                             <br>
    //                                             <b>Properties:</b>
    //                                             <ul>
    //                                                 ${disabled_props.map(p => `<li>${p}</li>`).join('')}
    //                                             </ul>
    //                                             <b>Rooms:</b>
    //                                             <ul>
    //                                                 ${disabled_rooms.map(r => `<li>${r}</li>`).join('')}
    //                                             </ul>
    //                                         `;
                                            
    //                                         frappe.msgprint({
    //                                             title: __("Success"),
    //                                             indicator: "green",
    //                                             message: message
    //                                         });
    //                                         frm.reload_doc();
    //                                     } else {
    //                                         frappe.msgprint({
    //                                             title: __("Error"),
    //                                             indicator: "red",
    //                                             message: __("An unexpected error occurred.")
    //                                         });
    //                                     }
    //                                 }
    //                             });
    //                             d.hide();
    //                         },
    //                         () => {
    //                             // If 'No' is clicked
    //                             frappe.msgprint(__("Aborted, no change is made"));
    //                         }
    //                     );
    //                 }
    //             });
    //             d.show();
    //         });
    //     }, __("Property"));
    //     }
	// },
});
