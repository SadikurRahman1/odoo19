{
    'name': 'Pharmacy POS Role',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Custom POS Roles for Pharmacy - Admin Only Sales & No Cash Collection',
    'author': 'Your Name',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
        'sale',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/pos_role_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pharmacy_pos_role/static/src/js/*.js',
            'pharmacy_pos_role/static/src/xml/*.xml',
        ],
    },
    'installable': True,
    'application': False,
}
