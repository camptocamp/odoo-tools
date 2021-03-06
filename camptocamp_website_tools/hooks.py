#  Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def post_init_hook(cr, registry):
    query = """
        UPDATE ir_ui_view
        SET customize_show = False, active = False
        WHERE key = 'website.show_website_info';
    """
    cr.execute(query)


def uninstall_hook(cr, registry):
    query = """
        UPDATE ir_ui_view
        SET customize_show = True
        WHERE key = 'website.show_website_info';
    """
    cr.execute(query)
