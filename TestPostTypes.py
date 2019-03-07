from BaseTest import BaseTest

# TestPostTypes
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the post-types-related endpoints for the WordPress test site.


class TestPostTypes(BaseTest):

    def test_get_post_types_returns_post_types(self):
        """
        Verify the GetPostTypes endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_post_types()
        assert req is not None, "GetPostTypes endpoint returned a null response."
        assert len(req) > 0, "GetPostTypes endpoint not returning at least one object in JSON output."

    def test_get_post_type_by_tag(self):
        """
        Verify getting a post type by specific tag off the GetPostTypeByTag endpoint
        """
        req = self.wp_tc.get_post_type_by_tag(self.wp_lib.getPostTypeTag)
        assert req is not None, "GetPostTypeByTag endpoint returned a null object. Post type may not exist."
        assert req['slug'] == self.wp_lib.getPostTypeTag, "GetPostTypeByTag endpoint didn't return correct slug."
        assert req['name'] == self.wp_lib.getPostTypeName,\
            "Retrieved post type from GetPostTypeByTag endpoint does not have expected name."
