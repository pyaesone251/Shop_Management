{
    'name':'Shop Management',
    'version':'19.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Shop Management System',
    'installable':True,
    'auto_install':False,
    'application':True,
    'sequence':1,
    'depends':['sale_management'],
    'data':[
        'views/sale_order_inherit_view.xml',
        'report/sale_order_inherit_report.xml',
    ],
}