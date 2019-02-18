from BaseTest import BaseTest

# TestCategories
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the categories-related endpoints for the WordPress test site.


class TestCategories(BaseTest):

    def test_get_categories_returns_categories(self):
        """
        Verify the GetCategories endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_categories()
        assert req is not None, "GetCategories endpoint returned a null response."
        assert len(req) > 0, "GetCategories endpoint not returning at least one object in JSON output."

    def test_get_category_by_id(self):
        """
        Verify getting a category by specific ID off the GetCategoryById endpoint
        """
        req = self.wp_tc.get_category_by_id(self.wp_lib.getCategoryId)
        assert req is not None, "GetCategoryById endpoint returned a null object. Category may not exist."
        assert req['id'] == self.wp_lib.getCategoryId, "GetCategoryById endpoint didn't return correct ID number."
        assert req['name'] == self.wp_lib.getCategoryName,\
            "Retrieved category from GetCategoryById endpoint does not have expected name."
