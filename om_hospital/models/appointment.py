from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'
    patient_id = fields.Many2one(comodel_name='hospital.patient', string="Patient")
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    appointment_time = fields.Datetime(string='Appointment Time', help="Date of appointment")
    booking_date = fields.Date(string='Booking Date', help="Date of booking")
    ref = fields.Char(string='Reference', help="Reference from patient records")
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True, tracking=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')

    # how to define an onchange function
    @api.onchange('patient_id')  # specify the onchange
    def onchange_patient_id(self):  # field name
        self.ref = self.patient_id.ref  # get it from the patient model self.patient_id_ref

    # function named 'action_test' for the Test Button

    def action_test(self):
        print("Button clicked !!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfull',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
