def trim(name, email, phone, urls, job, about, exp, education, top, soft, lang):

    return {
        "name": name,
        "email": email,
        "phone": phone,
        'urls': '',
        'job': job,
        'about': about,
        'exp': '',
        'edu': '',
        'top': '',
        'soft': '',
        'lang': '' 
    }


"""
# personal
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    urls = request.POST.get("urls")

    # description
    job = request.POST.get("job")
    about = request.POST.get("about")
    exp = request.POST.get("exp")
    education = request.POST.get("education")

    # skills
    top = request.POST.get("top")
    soft = request.POST.get("soft")
    lang = request.POST.get("lang")
"""
