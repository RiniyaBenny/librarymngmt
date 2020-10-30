# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class BookCopies(models.Model):
    _name = 'librarymngmt.bookcopies'
    _description = "LibraryManagement Bookcopies"
    _inherits = {'librarymngmt.book': 'lib_book_id'}
    lib_book_id = fields.Many2one('librarymngmt.book', 'Books', required=True, ondelete="cascade")
    sequence = fields.Char(string='Unique Internal Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('librarymngmt.bookcopies.sequence') or _('New')
        result = super(BookCopies, self).create(vals)
        return result