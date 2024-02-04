from django.shortcuts import render
import qrcode
import base64
from io import BytesIO


def generate_qr(request):
    if request.method == "POST":
        text = request.POST.get("text")
        qr = qrcode.make(text)
        qr_image = BytesIO()
        qr.save(qr_image, format="PNG")
        qr_image_base64 = base64.b64encode(qr_image.getvalue()).decode(
            "utf-8"
        )

        return render(
            request, "qrcode.html", {"qr_image_base64": qr_image_base64, "text": text}
        )

    return render(request, "generate_qr.html")
