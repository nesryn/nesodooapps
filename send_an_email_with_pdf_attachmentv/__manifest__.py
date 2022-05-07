# -*- coding: utf-8 -*-
{
    'name': "Send An Email With PDF Attachment",

    'summary': """
      send list of products names every day""",

    'description': """
       send list of products names every day

    """,

    # for the full list
    'category': 'mail',
    'version': '12.0',
    'author': "Nesrine Essaies",

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'data/template.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'images': ['static/description/sedpdf.png'],
}