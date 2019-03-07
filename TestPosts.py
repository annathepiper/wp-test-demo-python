from BaseTest import BaseTest

# TestPosts
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the posts-related endpoints for the WordPress test site.


class TestPosts(BaseTest):

    def test_get_posts_returns_posts(self):
        """
        Verify the GetPosts endpoint returns a JSON array of length > 0
        """
        req = self.wp_tc.get_posts()
        assert req is not None, "GetPosts endpoint returned a null response."
        assert len(req) > 0, "GetPosts endpoint not returning at least one object in JSON output."

    def test_get_post_by_id(self):
        """
        Verify getting a post by specific ID off the GetPosts endpoint
        """
        req = self.wp_tc.get_post_by_id(self.wp_lib.getPostId)
        assert req is not None, "GetPostById endpoint returned a null object. Post may not exist."
        assert req['id'] == self.wp_lib.getPostId, "GetPostById endpoint didn't return correct ID number."
        assert req['title']['rendered'] == self.wp_lib.getPostTitle,\
            "Retrieved post from GetPostById endpoint does not have expected title."
