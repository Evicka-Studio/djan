# import pyperclip  # only if you want to do local copying in dev; usually not used in production
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

from .models import Paste
from datetime import timedelta

MAX_PASTES = 100000  # Define your paste limit

def create_paste(request):
    if Paste.objects.count() >= MAX_PASTES:
        return render(request, "pastes/create_paste.html", {"error": "Paste limit reached. Please try again later."})
    if request.method == "POST":
        code_content = request.POST.get("code_area", "")
        if code_content.strip():
            # Create a new Paste object
            new_paste = Paste.objects.create(code=code_content)
            # Generate the URL for the newly created paste
            paste_url = request.build_absolute_uri(
                reverse("view_paste", kwargs={"paste_id": new_paste.id})
            )

            # # In a real production environment, we wouldn’t typically use pyperclip,
            # # but rather display the link for the user to copy.
            # # For demonstration:
            # try:
            #     pyperclip.copy(paste_url)
            # except:
            #     pass

            return redirect("view_paste", paste_id=new_paste.id)
        else:
            # If empty, just refresh the page or show an error message
            return render(
                request,
                "pastes/create_paste.html",
                {"error": "Cannot save empty paste."},
            )
    else:
        return render(request, "pastes/create_paste.html")


def view_paste(request, paste_id):
    paste = get_object_or_404(Paste, pk=paste_id)

    # Check expiration
    if paste.is_expired():
        # Optionally delete or show an error
        paste.delete()
        raise Http404("This paste has expired and been deleted.")

    return render(request, "pastes/view_paste.html", {"paste": paste})
