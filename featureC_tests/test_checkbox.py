def test_checkbox_toggle(checkbox_page):
    checkbox_page.click("input[type='checkbox']:nth-of-type(1)")
    assert checkbox_page.is_checked("input[type='checkbox']:nth-of-type(1)")