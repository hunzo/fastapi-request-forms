from fastapi import APIRouter
from handler.pdf import vps, colo, vpn, account
from models import VPS, COLO, VPN, ACCOUNT
from fastapi.responses import StreamingResponse

api = APIRouter()


@api.post("/vps")
def Home(payload: VPS):
    try:
        buffer = vps(payload.dict())
        response = StreamingResponse(buffer, media_type="application/pdf")
        # response.headers["Content-Disposition"] = "inline; filename=pdfFile.pdf"
        response.headers["Content-Disposition"] = f"attachment; filename={payload.form_iso_no}.pdf"
        return response
    except Exception as e:
        return str(e)


@api.post("/colo")
def Home(payload: COLO):
    try:
        buffer = colo(payload.dict())
        response = StreamingResponse(buffer, media_type="application/pdf")
        # response.headers["Content-Disposition"] = "inline; filename=pdfFile.pdf"
        response.headers["Content-Disposition"] = f"attachment; filename={payload.form_iso_no}.pdf"
        return response
    except Exception as e:
        return str(e)


@api.post("/vpn")
def Home(payload: VPN):
    try:
        buffer = vpn(payload.dict())
        response = StreamingResponse(buffer, media_type="application/pdf")
        # response.headers["Content-Disposition"] = "inline; filename=pdfFile.pdf"
        response.headers["Content-Disposition"] = f"attachment; filename={payload.form_iso_no}.pdf"
        return response
    except Exception as e:
        print(e)
        return str(e)


@api.post("/account")
def Home(payload: ACCOUNT):
    try:
        buffer = account(payload.dict())
        response = StreamingResponse(buffer, media_type="application/pdf")
        # response.headers["Content-Disposition"] = "inline; filename=pdfFile.pdf"
        response.headers["Content-Disposition"] = f"attachment; filename={payload.form_iso_no}.pdf"
        return response
    except Exception as e:
        print(e)
        return str(e)
