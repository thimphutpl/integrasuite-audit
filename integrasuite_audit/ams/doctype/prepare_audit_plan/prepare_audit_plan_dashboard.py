from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
        'fieldname': 'prepare_audit_plan_no',
		'transactions': [
			{
				'label': _('Related'),
				'items': ['Audit Engagement Letter', 'Execute Audit']
			},
   			{
				'items': ['Audit Initial Report','Follow Up']
			},
		]
	}
