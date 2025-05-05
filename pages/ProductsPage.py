from pages.BasePage import BasePage


class Products(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator('#search_product')
        self.search_button = page.locator('#submit_search')
        self.product_name_frozen = page.locator('.single-products .productinfo p').first

    def search_product(self, product_name):
        self.safe_fill(self.search_input, product_name, "Search Input")
        self.safe_click(self.search_button, "Search Button")

    def verify_product_search(self, product_name):
        self.assert_element_text(self.product_name_frozen, product_name, "Product Name")
