# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'pruebas.student'
    _description = 'Estudiants'

    name = fields.Char()
    year = fields.Integer()

class teacher(models.Model):
    _name = 'pruebas.teacher'
    _description = 'Teachers'

    name = fields.Char()
    year = fields.Date()

class subject(models.Model):
    _name = 'pruebas.subject'
    _description = 'Subjects'

    name = fields.Char()

class classroom(models.Model):
    _name = 'pruebas.classroom'
    _description = 'Classrooms'

    name = fields.Char()

#     value2 = fields.Float(comp

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

