# from odoo import http


# class StudentManagement(http.Controller):
#     @http.route('/student_management/student_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_management/student_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_management.listing', {
#             'root': '/student_management/student_management',
#             'objects': http.request.env['student_management.student_management'].search([]),
#         })

#     @http.route('/student_management/student_management/objects/<model("student_management.student_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_management.object', {
#             'object': obj
#         })

