def role_flags(request):
    if not request.user.is_authenticated:
        return {}

    return {
        "is_admin": request.user.groups.filter(name="Admin").exists(),
        "is_teacher": request.user.groups.filter(name="Teacher").exists(),
        "is_student": request.user.groups.filter(name="Student").exists(),
    }
