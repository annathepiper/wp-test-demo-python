from BaseTest import BaseTest

# TestPostStatuses
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the post-status-related endpoints for the WordPress test site.


class TestPostStatuses(BaseTest):

    def test_get_post_statuses_returns_post_statuses(self):
        """
        Verify the GetPostStatuses endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_post_statuses()
        assert req is not None, "GetPostStatuses endpoint returned a null response."
        assert len(req) > 0, "GetPostStatuses endpoint not returning at least one object in JSON output."

    def test_get_post_status_by_tag(self):
        """
        Verify getting a post status by specific tag off the GetPostStatusByTag endpoint
        """
        req = self.wp_tc.get_post_status_by_tag(self.wp_lib.getPostStatusTag)
        assert req is not None, "GetPostStatusByTag endpoint returned a null object. Post status may not exist."
        assert req['slug'] == self.wp_lib.getPostStatusTag, "GetPostStatusByTag endpoint didn't return correct slug."
        assert req['name'] == self.wp_lib.getPostStatusName,\
            "Retrieved post status from GetPostStatusByTag endpoint does not have expected name."
