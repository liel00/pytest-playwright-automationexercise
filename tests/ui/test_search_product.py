import pytest
from pages.HomePage import HomePage
from pages.ProductsPage import Products


@pytest.mark.sanity
def test_search_product(set_up_tear_down, page) -> None:
    """ This test verifies that the search functionality works correctly for a specific product."""
    home_page = HomePage(page)
    home_page.click_products_button()
    products_page = Products(page)
    products_page.search_product("Frozen Tops For Kids")
    products_page.verify_product_search("Frozen Tops For Kids")
