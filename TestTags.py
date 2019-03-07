from BaseTest import BaseTest

# TestTags
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the tags-related endpoints for the WordPress test site.


class TestTags(BaseTest):

    def test_get_tags_returns_tags(self):
        """
        Verify the GetTags endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_tags()
        assert req is not None, "GetTags endpoint returned a null response."
        assert len(req) > 0, "GetTags endpoint not returning at least one object in JSON output."

    def test_get_tag_by_id(self):
        """
        Verify getting a tag by specific ID off the GetTagById endpoint
        """
        req = self.wp_tc.get_tag_by_id(self.wp_lib.getTagId)
        assert req is not None, "GetTagById endpoint returned a null object. Tag may not exist."
        assert req['id'] == self.wp_lib.getTagId, "GetTagById endpoint didn't return correct ID number."
        assert req['name'] == self.wp_lib.getTagName,\
            "Retrieved tag from GetTagById endpoint does not have expected name."
