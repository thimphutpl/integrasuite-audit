# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters=None):
	columns = [
		{
			"fieldname": "audit_subject",
			"label": "Audit Subject",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "prior_audit_work",
			"label": "Prior Audit Work",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "complexity",
			"label": "Complexity",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "control_environment",
			"label": "Control Environment",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "operating_management",
			"label": "Operating Management",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "changes",
			"label": "Changes",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "sensitivity",
			"label": "Sensitivity",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "budget",
			"label": "Budget",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "staff",
			"label": "Staff",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "weightage_ce",
			"label": "Weightage (CE)",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "company",
			"label": "Company",
			"fieldtype": "Link",
			"options": "Company",
			"width": 200
		}
	]
	return columns

def get_data(filters=None):
	data = []
	conditions = get_conditions(filters)
	query = """
		select
			rai.audit_subject, rai.prior_audit_work, rai.complexity, rai.control_environment, rai.operating_management, rai.changes, rai.sensitivity,
			rai.budget, rai.staff, rai.weightage_ce, ra.company
		from
			`tabRisk Assessment` ra, `tabRisk Assessment Item` rai
		where
			ra.docstatus=1 and ra.name=rai.parent {cond}
			order by rai.audit_subject
	""".format(cond=conditions)

	data = frappe.db.sql(query, as_dict=True)
	return data
		

def get_conditions(filters=None):
	conditions = ""
	if not filters.get("from_date"):
		frappe.throw(_("'From Date' is required"))
	
	if not filters.get("to_date"):
		frappe.throw(_("'To Date' is required"))

	if filters.get("from_date") and filters.get("to_date"):
		conditions += " and rai.posting_date between '{}' and '{}'".format(filters.get("from_date"),filters.get("to_date"))

	return conditions