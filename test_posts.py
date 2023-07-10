from BaseTest import BaseTest

# TestPosts
# Written by Angela Korra'ti
# Last updated 7/10/2023
#
# This test class is for verifying the posts-related endpoints for the WordPress test site.


class TestPosts(BaseTest):

    def test_get_posts_returns_posts(self):
        """
        Verify the Get Posts endpoint returns a JSON array of length > 0
        """
        req = self.wp_tc.get_posts()
        assert req is not None, "GetPosts endpoint returned a null response."
        assert len(req) > 0, "GetPosts endpoint not returning at least one object in JSON output."

    def test_get_post_by_id(self):
        """
        Verify getting a post by specific ID off the Get Post by Id endpoint
        """
        req = self.wp_tc.get_post_by_id(self.wp_lib.getPostId)
        assert req is not None, "GetPostById endpoint returned a null object. Post may not exist."
        assert req['id'] == self.wp_lib.getPostId, "GetPostById endpoint didn't return correct ID number."
        assert req['title']['rendered'] == self.wp_lib.getPostTitle,\
            "Retrieved post from GetPostById endpoint does not have expected title."

    def test_get_post_id_that_does_not_exist(self):
        """
        Verify that the Get Post by Id endpoint exhibits expected error behavior for a post ID that doesn't exist
        """
        req = self.wp_tc.get_post_by_id(self.wp_lib.getNonExistentId)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getNonExistentCode,
                                                        self.wp_lib.getNonExistentMessage)

    def test_get_post_id_bad_id(self):
        """
        Verify that the Get Post by Id endpoint throws expected error for an invalid post ID
        """
        req = self.wp_tc.get_post_by_id(self.wp_lib.getInvalidId)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_post_id_max_size(self):
        """
        Verify that the Get Post by Id endpoint throws expected error for a post ID using sys.maxsize
        """
        req = self.wp_tc.get_post_by_id(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getNonExistentCode,
                                                        self.wp_lib.getNonExistentMessage)

    def test_get_post_id_min_size(self):
        """
        Verify that the Get Post by Id endpoint throws expected error for a post ID using -sys.maxsize
        """
        req = self.wp_tc.get_post_by_id(str(self.minsize))
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)
