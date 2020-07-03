from BaseTest import BaseTest

# TestCategories
# Written by Angela Korra'ti
# Last updated 4/10/2019
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

    def test_get_category_id_that_does_not_exist(self):
        """
        Verify that the Get Category by Id endpoint exhibits expected error behavior for a category ID that doesn't
        exist
        """
        req = self.wp_tc.get_category_by_id(self.wp_lib.getNonExistentId)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTermNonExistentCode,
                                                        self.wp_lib.getTermNonExistentMessage)

    def test_get_category_id_bad_id(self):
        """
        Verify that the Get Category by Id endpoint throws expected error for an invalid category ID
        """
        req = self.wp_tc.get_category_by_id(self.wp_lib.getInvalidId)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_category_id_max_size(self):
        """
        Verify that the Get Category by Id endpoint throws expected error for a category ID using sys.maxsize
        """
        req = self.wp_tc.get_category_by_id(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTermNonExistentCode,
                                                        self.wp_lib.getTermNonExistentMessage)

    def test_get_category_id_min_size(self):
        """
        Verify that the Get Category by Id endpoint throws expected error for a category ID using -sys.maxsize
        """
        req = self.wp_tc.get_category_by_id(str(self.minsize))
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)
