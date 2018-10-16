# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    description = fields.Text()
    responsible_id = fields.Many2one(
        'res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
    level = fields.Selection(
        [(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")
    session_count = fields.Integer(
        "Session Count", compute="_compute_session_count")

    @api.depends('session_ids')
    def _compute_session_count(self):
        for course in self:
            course.session_count = len(course.session_ids)
