{
    'name':'ITI5',
    'summary':'ITI5 System',
    'author':'Nada-Soliman',
    'category':'Accounting',
    'website': "",
    'version':'0.1',
    'depends':['account','product'],
    'data':[
        'security/ir.model.access.csv',
        'security/groups.xml',
        'reports/iti_student_template.xml',
        'reports/iti_reports.xml',
        'views/base_menu.xml',
        'views/iti_student_views.xml',
        'views/iti_track_views.xml',
        'views/product_template_views.xml',
    ]
}