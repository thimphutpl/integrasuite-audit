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
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "complexity",
			"label": "Complexity",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "control_environment",
			"label": "Control Environment",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "operating_management",
			"label": "Operating Management",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "changes",
			"label": "Changes",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "sensitivity",
			"label": "Sensitivity",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "budget",
			"label": "Budget",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "staff",
			"label": "Staff",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "weightage_ce",
			"label": "Weightage (CE)",
			"fieldtype": "Int",
			"width": 150
		},
		{
			"fieldname": "total_score",
			"label": "Total Score",
			"fieldtype": "Float",
			"width": 150
		},
		{
			"fieldname": "average",
			"label": "Average",
			"fieldtype": "Float",
			"width": 150,
			"precision": 3
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
			rai.audit_subject, 
			CASE WHEN rai.prior_audit_work LIKE '%3yrs%' THEN 3 WHEN rai.prior_audit_work LIKE '%1-2yrs%' THEN 2 ELSE 1 END AS prior_audit_work,
			CASE WHEN rai.complexity='High' THEN 3 WHEN rai.complexity = 'Medium' THEN 2 ELSE 1 END AS complexity,
			CASE WHEN rai.control_environment='Very Weak' THEN 3 WHEN rai.control_environment = 'Weak' THEN 2 ELSE 1 END AS control_environment,
			CASE WHEN rai.operating_management='Poor' THEN 3 WHEN rai.operating_management = 'Satisfactory' THEN 2 ELSE 1 END AS operating_management,
			CASE WHEN rai.changes='Many' THEN 3 WHEN rai.changes = 'Some' THEN 2 ELSE 1 END AS changes,
			CASE WHEN rai.sensitivity='Frontline' THEN 3 WHEN rai.sensitivity = 'Significant' THEN 2 ELSE 1 END AS sensitivity,
			CASE WHEN rai.budget='High' THEN 3 WHEN rai.budget = 'Medium' THEN 2 ELSE 1 END AS budget,
			CASE WHEN rai.staff='High' THEN 3 WHEN rai.staff = 'Medium' THEN 2 ELSE 1 END AS staff,
			CASE WHEN rai.weightage_ce='Very Weak' THEN 3 WHEN rai.weightage_ce = 'Weak' THEN 2 ELSE 1 END AS weightage_ce,
			(
				(CASE WHEN rai.prior_audit_work LIKE '%3yrs%' THEN 3 WHEN rai.prior_audit_work LIKE '%1-2yrs%' THEN 2 ELSE 1 END) +
				(CASE WHEN rai.complexity='High' THEN 3 WHEN rai.complexity = 'Medium' THEN 2 ELSE 1 END) + 
				(CASE WHEN rai.control_environment='Very Weak' THEN 3 WHEN rai.control_environment = 'Weak' THEN 2 ELSE 1 END) +
				(CASE WHEN rai.operating_management='Poor' THEN 3 WHEN rai.operating_management = 'Satisfactory' THEN 2 ELSE 1 END) +
				(CASE WHEN rai.changes='Many' THEN 3 WHEN rai.changes = 'Some' THEN 2 ELSE 1 END) +
				(CASE WHEN rai.sensitivity='Frontline' THEN 3 WHEN rai.sensitivity = 'Significant' THEN 2 ELSE 1 END) +
				(CASE WHEN rai.budget='High' THEN 3 WHEN rai.budget = 'Medium' THEN 2 ELSE 1 END) +
				(CASE WHEN rai.staff='High' THEN 3 WHEN rai.staff = 'Medium' THEN 2 ELSE 1 END) + 
				(CASE WHEN rai.weightage_ce='Very Weak' THEN 3 WHEN rai.weightage_ce = 'Weak' THEN 2 ELSE 1 END)
			) as total_score,
			(
				(
					(CASE WHEN rai.prior_audit_work LIKE '%3yrs%' THEN 3 WHEN rai.prior_audit_work LIKE '%1-2yrs%' THEN 2 ELSE 1 END) +
					(CASE WHEN rai.complexity='High' THEN 3 WHEN rai.complexity = 'Medium' THEN 2 ELSE 1 END) + 
					(CASE WHEN rai.control_environment='Very Weak' THEN 3 WHEN rai.control_environment = 'Weak' THEN 2 ELSE 1 END) +
					(CASE WHEN rai.operating_management='Poor' THEN 3 WHEN rai.operating_management = 'Satisfactory' THEN 2 ELSE 1 END) +
					(CASE WHEN rai.changes='Many' THEN 3 WHEN rai.changes = 'Some' THEN 2 ELSE 1 END) +
					(CASE WHEN rai.sensitivity='Frontline' THEN 3 WHEN rai.sensitivity = 'Significant' THEN 2 ELSE 1 END) +
					(CASE WHEN rai.budget='High' THEN 3 WHEN rai.budget = 'Medium' THEN 2 ELSE 1 END) +
					(CASE WHEN rai.staff='High' THEN 3 WHEN rai.staff = 'Medium' THEN 2 ELSE 1 END) + 
					(CASE WHEN rai.weightage_ce='Very Weak' THEN 3 WHEN rai.weightage_ce = 'Weak' THEN 2 ELSE 1 END)
				) / 8
			) as average,
			ra.company
		from
			`tabRisk Assessment` ra, `tabRisk Assessment Item` rai
		where
			ra.docstatus=1 and ra.name=rai.parent {cond}
			order by average desc
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