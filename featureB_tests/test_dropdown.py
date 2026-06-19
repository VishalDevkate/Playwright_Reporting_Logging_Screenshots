def test_dropdown_select(dropdown_page):
    dropdown_page.select_option("#dropdown", "1")
    assert dropdown_page.input_value("#dropdown") == "1"