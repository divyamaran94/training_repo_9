{
    'name': "shpt_others",
    'description': """SHPT Others""",
    'author': "Divya Jothy D",
    'category': 'SHPT Others',
    'version': '0.1',
    'depends': ['base','point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/shpt_report_wizard.xml',
        'views/shpt_pos_report.xml'
    ],
    'license': 'LGPL-3',
}