from BaseTest import BaseTest

# TestMedia
# Written by Angela Korra'ti
# Last updated 2/18/2019
#
# This test class is for verifying the media-related endpoints for the WordPress test site.


class TestMedia(BaseTest):

    def test_get_media_returns_media(self):
        """
        Verify the GetMedia endpoint returns a JSON array of length > 0
        """
        req = self.wp_tc.get_media()
        assert req is not None, "GetMedia endpoint returned a null response."
        assert len(req) > 0, "GetMedia endpoint not returning at least one object in JSON output."

    def test_get_media_by_id(self):
        """
        Verify getting a media item by specific ID off the GetMediaById endpoint
        """
        req = self.wp_tc.get_media_by_id(self.wp_lib.getMediaId)
        assert req is not None, "GetMediaById endpoint returned a null object. Media item may not exist."
        assert req['id'] == self.wp_lib.getMediaId, "GetMediaById endpoint didn't return correct ID number."
        assert req['title']['rendered'] == self.wp_lib.getMediaTitle,\
            "Retrieved media from GetMediaById endpoint does not have expected title."
