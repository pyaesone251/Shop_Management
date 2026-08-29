{
    'name':'Shop Management',
    'version':'19.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Shop Management System',
    'installable':True,
    'auto_install':False,
    'application':True,
    'sequence':1,
    'assets':{
        'point_of_sale._assets_pos':[
            "shop_management/static/src/js/pos_order.js",
            "shop_management/static/src/js/payment_screen.js",
            "shop_management/static/src/xml/pos_receipt.xml",
        ]
    },
    'depends':['sale_management','point_of_sale',],
    'data':[
        'views/sale_order_inherit_view.xml',
        'report/sale_order_inherit_report.xml',
    ],
}