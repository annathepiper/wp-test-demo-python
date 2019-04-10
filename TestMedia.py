from BaseTest import BaseTest

# TestMedia
# Written by Angela Korra'ti
# Last updated 4/10/2019
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
        # We need to do an OS check to determine which media ID to use
        if self.platform == 'Linux':
            targetId = self.wp_lib.getMediaId
        elif self.platform == 'Windows':
            targetId = self.wp_lib.getMediaIdWindows
        req = self.wp_tc.get_media_by_id(targetId)
        assert req is not None, "GetMediaById endpoint returned a null object. Media item may not exist."
        assert req['id'] == targetId, "GetMediaById endpoint didn't return correct ID number."
        assert req['title']['rendered'] == self.wp_lib.getMediaTitle,\
            "Retrieved media from GetMediaById endpoint does not have expected title."

    def test_get_media_id_that_does_not_exist(self):
        """
        Verify that the Get Media by Id endpoint exhibits expected error behavior for a media ID that doesn't exist
        """
        req = self.wp_tc.get_media_by_id(self.wp_lib.getNonExistentId)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getNonExistentCode,
                                                        self.wp_lib.getNonExistentMessage)

    def test_get_media_id_bad_id(self):
        """
        Verify that the Get Media by Id endpoint throws expected error for an invalid media ID
        """
        req = self.wp_tc.get_media_by_id(self.wp_lib.getInvalidId)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_media_id_max_size(self):
        """
        Verify that the Get Media by Id endpoint throws expected error for a media ID using sys.maxsize
        """
        req = self.wp_tc.get_media_by_id(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getNonExistentCode,
                                                        self.wp_lib.getNonExistentMessage)

    def test_get_media_id_min_size(self):
        """
        Verify that the Get Media by Id endpoint throws expected error for a media ID using -sys.maxsize
        """
        req = self.wp_tc.get_media_by_id(str(self.minsize))
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)
