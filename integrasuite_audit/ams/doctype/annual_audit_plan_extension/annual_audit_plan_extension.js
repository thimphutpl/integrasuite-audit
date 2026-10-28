// Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Annual Audit Plan Extension', {
	refresh: function(frm) {
		disable_fields(frm)
	}
});

function disable_fields(frm){
	//disable fields after save
		if (frm.doc.docstatus === 1){
			cur_frm.set_df_property("q1_start_date", "read_only", 1);
			cur_frm.set_df_property("q1_end_date", "read_only", 1);
			cur_frm.set_df_property("q2_start_date", "read_only", 1);
			cur_frm.set_df_property("q2_end_date", "read_only", 1);
			cur_frm.set_df_property("q3_start_date", "read_only", 1);
			cur_frm.set_df_property("q3_end_date", "read_only", 1);
			cur_frm.set_df_property("q4_start_date", "read_only", 1);
			cur_frm.set_df_property("q4_end_date", "read_only", 1);
		}
	}
