def test_login_success(login_user):
    assert "Secure Area" in login_user.text_content("h2")