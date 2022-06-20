import json
import os
from django.shortcuts import render
from power_on.settings import STATICFILES_DIRS
from power_on.wake_up_on_lan import wake


def click(request):
    print(request.POST)
    context = {'hello': 'Hello World!', 'clients': []}
    for dir_address in STATICFILES_DIRS:
        json_path = os.path.join(dir_address, "client.json")
        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                context["clients"] = json.load(f)
            break
    if request.POST:
        mac_address = request.POST['wake_mac']
        wake(mac_address)
    return render(request, "button.html", context)
