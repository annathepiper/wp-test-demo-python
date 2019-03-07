from BaseTest import BaseTest

# TestTaxonomies
# Written by Angela Korra'ti
# Last updated 2/18/2019
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
