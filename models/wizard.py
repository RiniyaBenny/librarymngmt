# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'librarymngmt.wizard'
    _description = "Wizard: Quick View of Rented Customer Details with count of rented books to Book"

    def _default_book(self):
        return self.env['librarymngmt.book'].browse(self._context.get('active_ids'))

    book_ids = fields.Many2many('librarymngmt.book',
                                string="Books", required=True)

    customer_ids = fields.Many2many('librarymngmt.customer', string="Customers")

    def subscribe(self):
        for book in self.book_ids:
            book.customer_ids |= self.customer_ids
            return {}