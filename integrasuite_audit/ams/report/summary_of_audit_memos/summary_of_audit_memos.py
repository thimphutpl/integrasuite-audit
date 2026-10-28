# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
    if not filters:
        filters = {}
  
    columns = get_columns(filters)
    data = get_data(filters)
 
    return columns, data

def get_columns(filters):
    columns = [
        ("Branches") + ":data:400",
        ("Total Memos Observed") + "::150",
        ("Memos Dropped") + "::150",
        ("Memos Pending") + "::150",
        ("% Resolved") + "::150",
    ]
    return columns

def get_data(filters):
    data = frappe.db.sql("""
        SELECT 
            c.branch, SUM(c.tmo) as totalmo, SUM(c.md) as memosd, SUM(c.mp) as memosp, round((SUM(c.md)/SUM(c.tmo))*100) as percentr
        FROM (
                SELECT a.branch, COUNT(*) as tmo, 0 as md, 0 as mp 
                FROM 
                    `tabExecute Audit` as a, `tabExecute Audit Checklist Item` as b
                    WHERE a.docstatus = 1 
                    AND a.name = b.parent
                    AND a.posting_date between '{from_date}' and '{to_date}'
                GROUP BY a.branch
                UNION 
                SELECT a.branch, 0 as tmo, COUNT(*) as md, 0 as mp 
                FROM 
                    `tabExecute Audit` as a, `tabExecute Audit Checklist Item` as b
                    WHERE a.docstatus = 1 
                    AND a.name = b.parent
                    AND a.posting_date between '{from_date}' and '{to_date}'
                    AND b.status = 'Close'
                GROUP BY a.branch
                UNION 
                SELECT a.branch, 0 as tmo, 0 as md, COUNT(*) as mp 
                FROM 
                    `tabExecute Audit` as a, `tabExecute Audit Checklist Item` as b
                    WHERE a.docstatus = 1 
                    AND a.name = b.parent
                    AND a.posting_date between '{from_date}' and '{to_date}'
                    AND b.status <> 'Close'
                GROUP BY a.branch) as c
        GROUP BY c.branch
        ORDER BY c.branch
        """.format(from_date=filters.get("from_date"), to_date=filters.get("to_date")))

    return data
