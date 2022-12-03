from pdf.pdf_form_vps import vps_request_form
from pdf.pdf_form_colo import colo_request_form
from pdf.pdf_form_vpn import vpn_request_form
from pdf.pdf_form_account import account_request_form


def vps(payload):
    return vps_request_form(payload)


def colo(payload):
    return colo_request_form(payload)


def vpn(payload):
    return vpn_request_form(payload)


def account(payload):
    return account_request_form(payload)
