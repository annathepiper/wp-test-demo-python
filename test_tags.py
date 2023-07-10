from BaseTest import BaseTest

# TestTags
# Written by Angela Korra'ti
# Last updated 7/10/2023
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

    def test_get_tag_id_that_does_not_exist(self):
        """
        Verify that the Get Tag by Id endpoint exhibits expected error behavior for a tag ID that doesn't exist
        """
        req = self.wp_tc.get_tag_by_id(self.wp_lib.getNonExistentId)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTermNonExistentCode,
                                                        self.wp_lib.getTermNonExistentMessage)

    def test_get_tag_id_bad_id(self):
        """
        Verify that the Get Tag by Id endpoint throws expected error for an invalid tag ID
        """
        req = self.wp_tc.get_tag_by_id(self.wp_lib.getInvalidId)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_tag_id_max_size(self):
        """
        Verify that the Get Tag by Id endpoint throws expected error for a tag ID using sys.maxsize
        """
        req = self.wp_tc.get_tag_by_id(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getTermNonExistentCode,
                                                        self.wp_lib.getTermNonExistentMessage)

    def test_get_tag_id_min_size(self):
        """
        Verify that the Get Tag by Id endpoint throws expected error for a tag ID using -sys.maxsize
        """
        req = self.wp_tc.get_tag_by_id(str(self.minsize))
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)
