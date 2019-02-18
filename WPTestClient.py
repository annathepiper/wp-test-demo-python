import WPTestLib
import requests

# WPTestClient
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is a helper client for the wp-test-demo-python project. It provides access to the REST API
# endpoints on the local test Wordpress site.


class WPTestClient:
    wp_lib = None
    
    # Use these to build the service endpoints
    host = None
    protocol = None

    # Service endpoint templates
    wpSite = "%s://%s"
    wpGetPostsTemplate = "/wp-json/wp/v2/posts"
    wpGetPostByIdTemplate = "/wp-json/wp/v2/posts/%s"
    wpGetCategoriesTemplate = "/wp-json/wp/v2/categories"
    wpGetCategoryByIdTemplate = "/wp-json/wp/v2/categories/%s"
    wpGetTagsTemplate = "/wp-json/wp/v2/tags"
    wpGetTagByIdTemplate = "/wp-json/wp/v2/tags/%s"
    wpGetPagesTemplate = "/wp-json/wp/v2/pages"
    wpGetPageByIdTemplate = "/wp-json/wp/v2/pages/%s"
    wpGetCommentsTemplate = "/wp-json/wp/v2/comments"
    wpGetCommentByIdTemplate = "/wp-json/wp/v2/comments/%s"
    wpGetTaxonomiesTemplate = "/wp-json/wp/v2/taxonomies"
    wpGetTaxonomyByTagTemplate = "/wp-json/wp/v2/taxonomies/%s"
    wpGetMediaTemplate = "/wp-json/wp/v2/media"
    wpGetMediaByIdTemplate = "/wp-json/wp/v2/media/%s"
    wpGetUsersTemplate = "/wp-json/wp/v2/users"
    wpGetUserByIdTemplate = "/wp-json/wp/v2/users/%s"
    wpGetPostTypesTemplate = "/wp-json/wp/v2/types"
    wpGetPostTypeByTagTemplate = "/wp-json/wp/v2/types/%s"
    wpGetPostStatusesTemplate = "/wp-json/wp/v2/statuses"
    wpGetPostStatusByTagTemplate = "/wp-json/wp/v2/statuses/%s"

    def __init__(self, host, protocol):
        """
        Init function for the class
        :param host: Host for the Wordpress REST API endpoints
        :param protocol: Protocol for hitting the host
        """
        self.wp_lib = WPTestLib.WPTestLib()
        self.host = host
        self.protocol = protocol
        self.wpSite = self.wpSite % (self.protocol, self.host)

    def get_posts(self):
        """
        :return: JSON response from hitting the GetPosts endpoint
        """
        uri = self.wpSite + self.wpGetPostsTemplate
        req = requests.get(uri)
        return req.json()

    def get_post_by_id(self, postId):
        """
        :param postId: Id of the post we want to fetch
        :return: JSON response from hitting the GetPostById endpoint
        """
        uri = self.wpSite + (self.wpGetPostByIdTemplate % postId)
        req = requests.get(uri)
        return req.json()