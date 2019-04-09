# WPTestLib
# Written by Angela Korra'ti
# Last updated 4/9/19
#
# This is a helper class providing access to assorted strings for IDs and such for configuring and running tests.


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
    getMediaId = 25514
    getMediaIdWindows = 25550
    getMediaTitle = "cropped-faerie-blood-epub-cover.jpg"
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
