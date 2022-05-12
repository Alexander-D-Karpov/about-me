from django.shortcuts import render

from about.models import Project
from site_blog.settings import BASE_DIR
from django.contrib.auth.decorators import permission_required


@permission_required("is_superuser")
def about_edit(request):
    if request.method == "POST":
        page = request.POST["text"]
        with open(str(BASE_DIR) + "/about/templates/about/about.html", "w") as file:
            file.write(page)
    page = open(str(BASE_DIR) + "/about/templates/about/about.html").read()
    return render(
        request, "about/about_edit.html", context={"page": page}
    )


def about(request):
    return render(
        request, "about/about.html", context={"projects": Project.objects.all()}
    )
