
def set_auth_cookie(response, token):
    response.set_cookie(
        "access_token",
        token,
        httponly=True,
        samesite="Lax",
        max_age=1800
    )
    return response

def delete_auth_cookie(response):
    response.delete_cookie(
        "access_token",
        httponly=True,
        samesite="Lax"
    )
    return response