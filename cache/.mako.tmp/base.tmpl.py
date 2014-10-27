# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414398957.3323085
_enable_loop = True
_template_filename = 'themes/dinky/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!doctype html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="chrome=1">\n    <title>Netkit-ng by netkit-ng</title>\n\n    <link rel="stylesheet" href="assets/css/styles.css">\n    <link rel="stylesheet" href="assets/css/pygment_trac.css">\n    <script src="assets/js/scale.fix.js"></script>\n    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">\n    <!--[if lt IE 9]>\n    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>\n    <![endif]-->\n  </head>\n  <body>\n    <div class="wrapper">\n      <header id="main-header">\n        <h1 class="header">Netkit-ng</h1>\n        <p class="header">Netkit reloaded</p>\n        <ul>\n          <li><a class="buttons github" href="https://github.com/netkit-ng">GitHub Profile</a></li>\n        </ul>\n      </header>\n      <section>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n      </section>\n      <footer id="main-footer">\n        <p><small>Hosted on <a href="http://pages.github.com">GitHub Pages</a> using the Dinky theme</small></p>\n      </footer>\n    </div>\n    <!--[if !IE]><script>fixScale(document);</script><![endif]-->\n                  <script type="text/javascript">\n            var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\n            document.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n          </script>\n          <script type="text/javascript">\n            try {\n              var pageTracker = _gat._getTracker("UA-45124358-3");\n            pageTracker._trackPageview();\n            } catch(err) {}\n          </script>\n\n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.tmpl", "filename": "themes/dinky/templates/base.tmpl", "source_encoding": "utf-8", "line_map": {"33": 27, "27": 27, "44": 33, "22": 2, "15": 0}}
__M_END_METADATA
"""
