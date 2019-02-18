from BaseTest import BaseTest

# TestPages
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the pages-related endpoints for the WordPress test site.


class TestPages(BaseTest):

    def test_get_pages_returns_pages(self):
        """
        Verify the GetPages endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_pages()
        assert req is not None, "GetPages endpoint returned a null response."
        assert len(req) > 0, "GetPages endpoint not returning at least one object in JSON output."

    def test_get_page_by_id(self):
        """
        Verify getting a page by specific ID off the GetPageById endpoint
        """
        req = self.wp_tc.get_page_by_id(self.wp_lib.getPageId)
        assert req is not None, "GetPageById endpoint returned a null object. Page may not exist."
        assert req['id'] == self.wp_lib.getPageId, "GetPageById endpoint didn't return correct ID number."
        assert req['title']['rendered'] == self.wp_lib.getPageTitle,\
            "Retrieved page from GetPageById endpoint does not have expected title."
