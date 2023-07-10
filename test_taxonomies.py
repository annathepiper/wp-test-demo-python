from BaseTest import BaseTest

# TestTaxonomies
# Written by Angela Korra'ti
# Last updated 7/10/2023
#
# This test class is for verifying the taxonomies-related endpoints for the WordPress test site.


class TestTaxonomies(BaseTest):

    def test_get_taxonomies_returns_taxonomies(self):
        """
        Verify the GetTaxonomies endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_taxonomies()
        assert req is not None, "GetTaxonomies endpoint returned a null response."
        assert len(req) > 0, "GetTaxonomies endpoint not returning at least one object in JSON output."

    def test_get_taxonomy_by_tag(self):
        """
        Verify getting a taxonomy by specific tag off the GetTaxonomyByTag endpoint
        """
        req = self.wp_tc.get_taxonomy_by_tag(self.wp_lib.getTaxonomyTag)
        assert req is not None, "GetTaxonomyByTag endpoint returned a null object. Taxonomy may not exist."
        assert req['slug'] == self.wp_lib.getTaxonomyTag, "GetTaxonomyByTag endpoint didn't return correct slug."
        assert req['name'] == self.wp_lib.getTaxonomyName,\
            "Retrieved taxonomy from GetTaxonomyByTag endpoint does not have expected name."

    def test_get_taxonomy_tag_that_does_not_exist(self):
        """
        Verify that the Get Taxonomy by Tag endpoint exhibits expected error behavior for a taxonomy tag that doesn't
        exist
        """
        req = self.wp_tc.get_taxonomy_by_tag(self.wp_lib.getNonExistentTag)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTaxonomyNonExistentCode,
                                                        self.wp_lib.getTaxonomyNonExistentMessage)

    def test_get_taxonomy_tag_bad_tag(self):
        """
        Verify that the Get Taxonomy by Tag endpoint throws expected error for an invalid taxonomy tag
        """
        req = self.wp_tc.get_taxonomy_by_tag(self.wp_lib.getInvalidTag)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_taxonomy_tag_max_size(self):
        """
        Verify that the Get Taxonomy by Tag endpoint throws expected error for a taxonomy tag using sys.maxsize
        """
        req = self.wp_tc.get_taxonomy_by_tag(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTaxonomyNonExistentCode,
                                                        self.wp_lib.getTaxonomyNonExistentMessage)

    def test_get_taxonomy_tag_min_size(self):
        """
        Verify that the Get Taxonomy by Tag endpoint throws expected error for a taxonomy tag using -sys.maxsize
        """
        req = self.wp_tc.get_taxonomy_by_tag(str(self.minsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTaxonomyNonExistentCode,
                                                        self.wp_lib.getTaxonomyNonExistentMessage)
