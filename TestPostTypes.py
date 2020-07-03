from BaseTest import BaseTest

# TestPostTypes
# Written by Angela Korra'ti
# Last updated 4/10/2019
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

    def test_get_post_type_tag_that_does_not_exist(self):
        """
        Verify that the Get Post Type by Tag endpoint exhibits expected error behavior for a post type tag that doesn't
        exist
        """
        req = self.wp_tc.get_post_type_by_tag(self.wp_lib.getNonExistentTag)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getPostTypeNonExistentCode,
                                                        self.wp_lib.getPostTypeNonExistentMessage)

    def test_get_post_type_tag_bad_tag(self):
        """
        Verify that the Get Post Type by Tag endpoint throws expected error for an invalid post type tag
        """
        req = self.wp_tc.get_post_type_by_tag(self.wp_lib.getInvalidTag)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_post_type_tag_max_size(self):
        """
        Verify that the Get Post Type by Tag endpoint throws expected error for a post type tag using sys.maxsize
        """
        req = self.wp_tc.get_post_type_by_tag(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getPostTypeNonExistentCode,
                                                        self.wp_lib.getPostTypeNonExistentMessage)

    def test_get_post_type_tag_min_size(self):
        """
        Verify that the Get Post Type by Tag endpoint throws expected error for a post type tag using -sys.maxsize
        """
        req = self.wp_tc.get_post_type_by_tag(str(self.minsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getPostTypeNonExistentCode,
                                                        self.wp_lib.getPostTypeNonExistentMessage)
