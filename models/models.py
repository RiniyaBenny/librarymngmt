# -*- coding: utf-8 -*-
import datetime
from datetime import datetime, timedelta
from odoo import models, fields, api
class Book(models.Model):
    _name = 'librarymngmt.book'
    _description = "LibraryManagement Books"

    isbn = fields.Char('ISBN Code', unique=True,
                        help="Shows International Standard Book Number")
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    author_ids = fields.Many2many('librarymngmt.author', string="Author/Authors")
    editor = fields.Char(string="Editor", required=True)
    yr_of_edition = fields.Char(string="Year Of Edition")
    publisher = fields.Char(string="Publisher", required=True)
    
    class Customer(models.Model):
        _name = 'librarymngmt.customer'
        _description = "LibraryManagement Customers"

        #def set_reminder(self):
        #    today = fields.Date.today()
        #    for r in self:
        #        if r.state == 'rented' and r.return_date < today:
        #            print("Reminder for returning the rented book.")

        def status_rented(self):
            for rec in self:
                rec.state = 'rented'
        def status_returned(self):
            for rec in self:
                rec.state = 'returned'

        def status_lost(self):
            for rec in self:
                rec.state = 'lost'

        def status_fined(self):
            for rec in self:
                rec.state = 'fined'

        def status_paid(self):
            for rec in self:
                rec.state = 'paid'

        name = fields.Many2one('res.partner', string="Name", required=True)
        #book_names = fields.Many2many('librarymngmt.book', string="Rented Books")
        book_names = fields.Many2many('librarymngmt.bookcopies', string="Rented Books")
        rental_date = fields.Date(string="Rental Date", default=fields.Date.today())
        return_date = fields.Date(string="Return Date")  
        #return_date = rental_date + datetime.timedelta(days=14)    
        #return_span = int(return_date.strftime('%m%d%Y'))
        #returned_date = fields.Date(string="Returned Date")
        #returned_span = int(returned_date.strftime('%m%d%Y'))
        

        state = fields.Selection([('rented', 'Rented'),
                                  ('returned', 'Returned'),
                                  ('lost', 'Lost'),
                                  ('fined', 'Fined'),
                                  ('paid', 'Paid'),
                                  ], string='Status', readonly=True, default='rented')
        rent_fee_for_one_day = fields.Integer(default=50, string="Rent Fee For One Day")
        lost_book = fields.Integer(default=1500, string="Lost Book Fine")
        delayed_return = fields.Integer(default=500, string="Delayed Return of Book Fine")
        tot_fee = fields.Integer(string="Total Amount Payable", compute='_tot_fee')

        @api.onchange('  state', 'tot_fee', ' rent_fee_for_one_day ')
        def _tot_fee(self):
            for r in self:
                if r.state == 'returned':
                    rent_fee = 14 * r.rent_fee_for_one_day
                    r.tot_fee = rent_fee
                    print("Rental fee = Rs ", rent_fee)
                    print("Total amount payable = Rs ", r.tot_fee)

                elif r.state == 'rented':
                    rent_fee = 14 * r.rent_fee_for_one_day
                    r.tot_fee = rent_fee
                    print("Rental fee = Rs ", rent_fee)
                    print("Total amount payable = Rs ", r.tot_fee)

                elif r.state == 'draft':
                    rent_fee = 0 * r.rent_fee_for_one_day
                    r.tot_fee = rent_fee
                    print("Rental fee = Rs ", rent_fee)
                    print("Total amount payable = Rs ", r.tot_fee)

                elif r.state == 'paid':
                    rent_fee = 0 * r.rent_fee_for_one_day
                    r.tot_fee = rent_fee
                    print("Rental fee = Rs ", rent_fee)
                    print("Total amount payable = Rs ", r.tot_fee)

                elif r.state == 'lost':
                    rent_fee = 14 * r.rent_fee_for_one_day
                    r.tot_fee = rent_fee + 1500
                    print("Rental fee = Rs", rent_fee)
                    print("Lost Book Fine = Rs 1500")
                    print("Total amount payable = Rs ", r.tot_fee)
                elif r.state == 'fined':
                    rent_fee = 14 * r.rent_fee_for_one_day
                    r.tot_fee = rent_fee + 500
                    print("Rental fee = Rs", rent_fee)
                    print("Delayed Return Book Fine = Rs 500")
                    print("Total amount payable = Rs ", r.tot_fee)
                else:
                    raise ValueError('Please enter Valid Data to calculate total amount payable')

                
    class Author(models.Model):
        _name = 'librarymngmt.author'
        _description = "LibraryManagement Authors"
        name = fields.Char(required=True)

    class RentBooks(models.Model):
        _name = 'librarymngmt.rentbook'
        _description = "LibraryManagement RentBooks"
