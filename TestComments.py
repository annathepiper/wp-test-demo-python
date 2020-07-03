from BaseTest import BaseTest

# TestComments
# Written by Angela Korra'ti
# Last updated 4/10/2019
#
# This test class is for verifying the comments-related endpoints for the WordPress test site.


class TestComments(BaseTest):

    def test_get_comments_returns_comments(self):
        """
        Verify the GetComments endpoint returns a JSON dictionary of length > 0
        """
        req = self.wp_tc.get_comments()
        assert req is not None, "GetComments endpoint returned a null response."
        assert len(req) > 0, "GetComments endpoint not returning at least one object in JSON output."

    def test_get_comment_by_id(self):
        """
        Verify getting a comment by specific ID off the GetCommentById endpoint
        """
        req = self.wp_tc.get_comment_by_id(self.wp_lib.getCommentId)
        assert req is not None, "GetCommentById endpoint returned a null object. Comment may not exist."
        assert req['id'] == self.wp_lib.getCommentId, "GetCommentById endpoint didn't return correct ID number."
        assert self.wp_lib.getCommentContent in req['content']['rendered'],\
            "Retrieved comment from GetCommentById endpoint does not have expected content."

    def test_get_comment_id_that_does_not_exist(self):
        """
        Verify that the Get Comment by Id endpoint exhibits expected error behavior for a comment ID that doesn't exist
        """
        req = self.wp_tc.get_comment_by_id(self.wp_lib.getNonExistentId)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getCommentNonExistentCode,
                                                        self.wp_lib.getCommentNonExistentMessage)

    def test_get_comment_id_bad_id(self):
        """
        Verify that the Get Comment by Id endpoint throws expected error for an invalid comment ID
        """
        req = self.wp_tc.get_comment_by_id(self.wp_lib.getInvalidId)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_comment_id_max_size(self):
        """
        Verify that the Get Comment by Id endpoint throws expected error for a comment ID using sys.maxsize
        """
        req = self.wp_tc.get_comment_by_id(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getCommentNonExistentCode,
                                                        self.wp_lib.getCommentNonExistentMessage)

    def test_get_comment_id_min_size(self):
        """
        Verify that the Get Comment by Id endpoint throws expected error for a comment ID using -sys.maxsize
        """
        req = self.wp_tc.get_comment_by_id(str(self.minsize))
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)
