import re
from playwright.sync_api import Page, expect


class ItemsPage:

    def __init__(self, page: Page):
        self.page = page

        # =========================
        # Listing Page
        # =========================

        self.search_input = page.get_by_role(
            "searchbox",
            name="Search:"
        )

        self.table_rows = page.locator(
            "table tbody tr"
        )

        # =========================
        # Add Item Button
        # =========================

        self.add_item_button = (
            page.locator(
                "main, .content-wrapper, body"
            )
            .locator(
                "a:visible, button:visible"
            )
            .filter(
                has_text=re.compile(
                    r"Add|Create|New",
                    re.IGNORECASE
                )
            )
        )

        # =========================
        # Item Form
        # =========================

        self.item_name_input = page.get_by_placeholder(
            "Product Name"
        )

        self.manufacturer_input = page.get_by_placeholder(
            "Eg: Getz Pharma"
        )

        # Product Type
        self.product_type = page.locator(
            "#productType"
        )

        self.save_item_button = page.get_by_role(
            "button",
            name="Save Item"
        )

        # =========================
        # Variation
        # =========================

        self.add_variation_button = page.get_by_role(
            "button",
            name="Add Variation"
        )

        self.variation_name_input = page.get_by_placeholder(
            "Variation Name"
        )

        self.sku_input = page.get_by_placeholder(
            "Enter SKU"
        )

        self.opening_stock_rate_input = page.get_by_placeholder(
            "Enter opening stock rate"
        )

        self.pills_in_pack_input = page.get_by_placeholder(
            "Enter No. of Pills in Pack"
        )

        self.reorder_point_input = page.get_by_placeholder(
            "Enter reorder point"
        )

        self.variation_save_button = (
            page.locator(".modal")
            .get_by_role(
                "button",
                name="Save"
            )
        )

    # =========================
    # Search Item
    # =========================

    def search_item(self, product_name):

        self.search_input.fill(
            product_name
        )

        self.page.wait_for_timeout(
            1000
        )

    # =========================
    # Open Add Item Form
    # =========================

    def open_create_item_form(self):

        self.add_item_button.first.click()

    # =========================
    # Create New Item
    # =========================

    def create_new_item(
        self,
        name,
        manufacturer="GSK"
    ):

        # Product Name
        self.item_name_input.fill(
            name
        )

        # Manufacturer
        self.manufacturer_input.fill(
            manufacturer
        )

        self.page.wait_for_timeout(
            500
        )

        self.manufacturer_input.press(
            "ArrowDown"
        )

        self.manufacturer_input.press(
            "Enter"
        )

        # Product Type
        self.product_type.select_option(
            "Medicine"
        )

        # Save Item
        self.save_item_button.click()

    # =========================
    # Add Variation
    # =========================

    def add_variation(
        self,
        item_name
    ):

        expect(
            self.add_variation_button
        ).to_be_visible(
            timeout=10000
        )

        self.add_variation_button.click()

        # Variation Name
        self.variation_name_input.fill(
            f"{item_name}_Var"
        )

        # SKU
        sku = str(
            int(
                self.page.evaluate(
                    "Date.now()"
                )
            )
        )

        self.sku_input.fill(
            sku
        )

        # Opening Stock Rate
        self.opening_stock_rate_input.fill(
            "100"
        )

        # Pills in Pack
        self.pills_in_pack_input.fill(
            "10"
        )

        # Reorder Point
        self.reorder_point_input.fill(
            "5"
        )

        # Save Variation
        self.variation_save_button.click()