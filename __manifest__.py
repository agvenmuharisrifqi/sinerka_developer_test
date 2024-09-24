{
    'name': 'School Management',
    'version': '1.0',
    'description': '',
    'summary': '',
    'author': 'Agven Muharis Rifqi',
    'website': '',
    'license': 'LGPL-3',
    'category': 'School/School',
    'depends': [
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_student_invoice.xml',
        'reports/report_school_classroom.xml',
        'reports/report_student_invoice.xml',
        'views/school_classroom_views.xml',
        'views/school_teacher_views.xml',
        'views/school_student_views.xml',
        'views/school_menuitems.xml',
        'views/account_move_views.xml',
    ],
    'demo': [
        'data/school_demo.xml',
    ],
    'auto_install': False,
    'application': True,
    'assets': {}
}