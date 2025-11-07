// Copyright (c) 2025, Raghav Ruia & others and contributors
// For license information, please see license.txt

frappe.ui.form.on("Studio Room", {
    //     refresh(frm) {
    //     // Use frappe.is_mobile() to check the device type.
    //     const isMobile = frappe.is_mobile();

        
    //         console.log("is mobile")
    //         // Get the field object for your child table.
    //         // Replace 'your_child_table_fieldname' with the actual fieldname of your child table.
    //         const child_table_field = frm.get_field('list_of_microphones');

    //         if (child_table_field) {
    //             // Check if the grid is currently editable.
    //             const is_grid_editable = child_table_field.grid.editable;
                
    //             // If grid is editable, turn it off.
    //             if (is_grid_editable) {
    //                 child_table_field.grid.toggle_editable(false);
    //                 frm.refresh_field(child_table_field);
    //             }
    //         }
    // }

	// onload(frm) {
    //     // Basic mobile check
    //     const isMobile = frappe.is_mobile() || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

    //     if (isMobile) {
    //         frappe.show_alert({ message: 'Mobile device detected 📱', indicator: 'orange' });
    //         // Target the child table fieldname
    //         const field = frm.fields_dict['list_of_microphones'];

    //         if (field && field.grid) {
    //             // // Disable editable grid on mobile
    //             // field.grid.editable_fields = [];
    //             // field.grid.only_sortable = false;
    //             field.grid.editable_grid = false;
    //             // field.grid.wrapper.find('.grid-add-row, .grid-row-open').show(); // show + buttons normally

    //             // Force refresh to apply non-editable mode
    //             frm.refresh_field('list_of_microphones');
    //         }
    //     }
	// }
//     refresh(frm) {
//     const isMobile = frappe.is_mobile() || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

//     if (isMobile) {
//       const grid = frm.fields_dict['list_of_microphones'].grid;

//       // Override the default "Add Row" behavior
//       grid.add_new_row = function(idx, freeze) {
//         // Call original add row method
//         const row = this.add_new_row.__original.apply(this, arguments);
        
//         // Immediately open the full form dialog for the new row
//         if (row) this.open_grid_row(row);

//         return row;
//       };

//       // Keep reference to original method so we can call it inside override
//       if (!grid.add_new_row.__original) {
//         grid.add_new_row.__original = frappe.ui.form.Grid.prototype.add_new_row;
//       }

//       frappe.show_alert({ message: 'Mobile mode: Add Row opens full form 🧾', indicator: 'orange' });
//     } else {
//       frappe.show_alert({ message: 'Desktop mode: Normal grid editing 💻', indicator: 'green' });
//     }
//   }
});
