# -*- coding: utf-8 -*-
# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe
from frappe.model.document import Document


class AnnualAuditPlanExtension(Document):
	def validate(self):
		self.validate_dates()

	def on_submit(self):
		self.update_annual_audit_plan()

	def update_annual_audit_plan(self):
		doc = frappe.get_doc("Annual Audit Plan", self.annual_audit_plan)
		doc.q1_start_date = self.q1_start_date
		doc.q1_end_date = self.q1_end_date
		doc.q2_start_date = self.q2_start_date
		doc.q2_end_date = self.q2_end_date
		doc.q3_start_date = self.q3_start_date
		doc.q3_end_date = self.q3_end_date
		doc.q4_start_date = self.q4_start_date
		doc.q4_end_date = self.q4_end_date
		doc.remarks = self.remarks
		doc.save(ignore_permissions=True)
	
	def validate_dates(self):
		if self.q1_start_date > self.q1_end_date:
			frappe.throw(_("Quarter 1 start date can not be greater than Quarter 1 end date"))

		if self.q2_start_date > self.q2_end_date:
			frappe.throw(_("Quarter 2 start date can not be greater than Quarter 2 end date"))

		if self.q3_start_date > self.q3_end_date:
			frappe.throw(_("Quarter 3 start date can not be greater than Quarter 3 end date"))

		if self.q4_start_date > self.q4_end_date:
			frappe.throw(_("Quarter 4 start date can not be greater than Quarter 4 end date"))
