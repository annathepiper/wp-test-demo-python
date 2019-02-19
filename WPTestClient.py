import WPTestLib
import requests

# WPTestClient
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is a helper client for the wp-test-demo-python project. It provides access to the REST API
# endpoints on the local test WordPress site.


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
        :param host: Host for the WordPress REST API endpoints
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

    def get_post_by_id(self, post_id):
        """
        :param post_id: Id of the post we want to fetch
        :return: JSON response from hitting the GetPostById endpoint
        """
        uri = self.wpSite + (self.wpGetPostByIdTemplate % post_id)
        req = requests.get(uri)
        return req.json()

    def get_categories(self):
        """
        :return: JSON response from hitting the GetCategories endpoint
        """
        uri = self.wpSite + self.wpGetCategoriesTemplate
        req = requests.get(uri)
        return req.json()

    def get_category_by_id(self, category_id):
        """
        :param category_id: Id of the post we want to fetch
        :return: JSON response from hitting the GetCategoryById endpoint
        """
        uri = self.wpSite + (self.wpGetCategoryByIdTemplate % category_id)
        req = requests.get(uri)
        return req.json()

    def get_tags(self):
        """
        :return: JSON response from hitting the GetTags endpoint
        """
        uri = self.wpSite + self.wpGetTagsTemplate
        req = requests.get(uri)
        return req.json()

    def get_tag_by_id(self, tag_id):
        """
        :param tag_id: Id of the tag we want to fetch
        :return: JSON response from hitting the GetTagById endpoint
        """
        uri = self.wpSite + (self.wpGetTagByIdTemplate % tag_id)
        req = requests.get(uri)
        return req.json()

    def get_pages(self):
        """
        :return: JSON response from hitting the GetPages endpoint
        """
        uri = self.wpSite + self.wpGetPagesTemplate
        req = requests.get(uri)
        return req.json()

    def get_page_by_id(self, page_id):
        """
        :param page_id: Id of the page we want to fetch
        :return: JSON response from hitting the GetPageById endpoint
        """
        uri = self.wpSite + (self.wpGetPageByIdTemplate % page_id)
        req = requests.get(uri)
        return req.json()

    def get_comments(self):
        """
        :return: JSON response from hitting the GetComments endpoint
        """
        uri = self.wpSite + self.wpGetCommentsTemplate
        req = requests.get(uri)
        return req.json()

    def get_comment_by_id(self, comment_id):
        """
        :param comment_id: Id of the comment we want to fetch
        :return: JSON response from hitting the GetCommentById endpoint
        """
        uri = self.wpSite + (self.wpGetCommentByIdTemplate % comment_id)
        req = requests.get(uri)
        return req.json()

    def get_taxonomies(self):
        """
        :return: JSON response from hitting the GetTaxonomies endpoint
        """
        uri = self.wpSite + self.wpGetTaxonomiesTemplate
        req = requests.get(uri)
        return req.json()

    def get_taxonomy_by_tag(self, taxonomy_tag):
        """
        :param taxonomy_tag: Tag of the taxonomy we want to fetch
        :return: JSON response from hitting the GetCommentById endpoint
        """
        uri = self.wpSite + (self.wpGetTaxonomyByTagTemplate % taxonomy_tag)
        req = requests.get(uri)
        return req.json()

    def get_media(self):
        """
        :return: JSON response from hitting the GetMedia endpoint
        """
        uri = self.wpSite + self.wpGetMediaTemplate
        req = requests.get(uri)
        return req.json()

    def get_media_by_id(self, media_id):
        """
        :param media_id: ID of the media item we want to fetch
        :return: JSON response from hitting the GetCommentById endpoint
        """
        uri = self.wpSite + (self.wpGetMediaByIdTemplate % media_id)
        req = requests.get(uri)
        return req.json()
