from BaseTest import BaseTest

# TestComments
# Written by Angela Korra'ti
# Last updated 2/18/2019
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
