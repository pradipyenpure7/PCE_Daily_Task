# -*- coding: utf-8 -*-
{
    'name': "Purchase Order",
    'summary': """
        All Purchase Order Views and Models in this app
        """,
    'description': """
        Long description of module's purpose
    """,
    'author': "Pradip R.Yepure",
    'website': "http://www.saiaipl.com",
    'category': 'Purchase',
    'version': '1.1',
    # any module necessary for this one to work correctly
    'depends': ['purchase',],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',        
        'views/purchase_view_order_form_view.xml',
    ],
    # only loaded in demonstration mode
    
    'installable':True,
    'auto_install':False,
    'application':True,
}
