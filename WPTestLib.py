# WPTestLib
# Written by Angela Korra'ti
# Last updated 4/9/2019
#
# This is a helper class providing access to assorted strings for IDs and such for configuring and running tests,
# as well as useful helper methods.


class WPTestLib:
    protocol = "http"
    host = "wordpress.local"
    getPostId = 25428
    getPostTitle = "Hello, readers!"
    getCategoryId = 1
    getCategoryName = "Uncategorized"
    getTagId = 7
    getTagName = "administrivia"
    getPageId = 1087
    getPageTitle = "Faerie Blood"
    getCommentId = 2
    getCommentContent = "This is a comment for testing purposes, used by my test automation suite."
    getTaxonomyTag = "category"
    getTaxonomyName = "Categories"
    getMediaId = 25399
    getMediaIdWindows = 25549
    getMediaTitle = "Faerie Blood"
    getUserId = 1
    getUserName = "annathepiper"
    getPostTypeTag = "post"
    getPostTypeName = "Posts"
    getPostStatusTag = "publish"
    getPostStatusName = "Published"

    # These are string specifically pertinent to negative test cases
    getNonExistentId = 999999999
    getNonExistentMessage = "Invalid post ID."
    getNonExistentCode = "rest_post_invalid_id"
    getNonExistentTag = "pancakes"
    getInvalidId = "aaaaaaa"
    getInvalidMessage = "No route was found matching the URL and request method"
    getInvalidCode = "rest_no_route"
    getInvalidTag = "pancakes(*)( @!!!"
    getTermNonExistentMessage = "Term does not exist."
    getTermNonExistentCode = "rest_term_invalid"
    getCommentNonExistentMessage = "Invalid comment ID."
    getCommentNonExistentCode = "rest_comment_invalid_id"
    getTaxonomyNonExistentMessage = "Invalid taxonomy."
    getTaxonomyNonExistentCode = "rest_taxonomy_invalid"
    getUserNonExistentMessage = "Invalid user ID."
    getUserNonExistentCode = "rest_user_invalid_id"
    getPostTypeNonExistentMessage = "Invalid post type."
    getPostTypeNonExistentCode = "rest_type_invalid"
    getPostStatusNonExistentMessage = "Invalid status."
    getPostStatusNonExistentCode = "rest_status_invalid"

    def verify_response_item_does_not_exist(self, req, error_code, error_message):
        """
        Helper method to take a JSON response object, expected error code, and expected error message, and make sure
        the response contains the appropriate data to reflect that the tested-for item does not exist.
        :param req: response from previously made request
        :param error_code: expected error code
        :param error_message: expected error message
        :return: n/a
        """
        assert req['code'] == error_code, "Target endpoint thinks target item ID actually exists."
        assert req['message'] == error_message, "Target endpoint didn't throw the expected error message."
        assert req['data'] is not None, "Target endpoint didn't include data object in response."
        assert req['data']['status'] == 404, "Target endpoint didn't return expected error code."

    def verify_response_item_is_invalid(self, req, error_code, error_message):
        """
        Helper method to take a JSON response object, expected error code, and expected error message, and make sure
        the response contains the appropriate data to reflect that the tested-for item is invalid.
        :param req: response from previously made request
        :param error_code: expected error code
        :param error_message: expected error message
        :return: n/a
        """
        assert req['code'] == error_code, "Target endpoint thinks target item ID is actually valid."
        assert req['message'] == error_message, "Target endpoint didn't throw the expected error message."
        assert req['data'] is not None, "Target endpoint didn't include data object in response."
        assert req['data']['status'] == 404, "Target endpoint didn't return expected error code."
