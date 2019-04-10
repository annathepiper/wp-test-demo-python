from BaseTest import BaseTest

# TestUsers
# Written by Angela Korra'ti
# Last updated 4/10/2019
#
# This test class is for verifying the users-related endpoints for the WordPress test site.


class TestUsers(BaseTest):

    def test_get_users_returns_users(self):
        """
        Verify the GetUsers endpoint returns a JSON array of length > 0
        """
        req = self.wp_tc.get_users()
        assert req is not None, "GetUsers endpoint returned a null response."
        assert len(req) > 0, "GetUsers endpoint not returning at least one object in JSON output."

    def test_get_users_by_id(self):
        """
        Verify getting a user by specific ID off the GetUserById endpoint
        """
        req = self.wp_tc.get_user_by_id(self.wp_lib.getUserId)
        assert req is not None, "GetUserById endpoint returned a null object. User may not exist."
        assert req['id'] == self.wp_lib.getUserId, "GetUserById endpoint didn't return correct ID number."
        assert req['name'] == self.wp_lib.getUserName,\
            "Retrieved user from GetUserById endpoint does not have expected name."

    def test_get_user_id_that_does_not_exist(self):
        """
        Verify that the Get User by Id endpoint exhibits expected error behavior for a user ID that doesn't exist
        """
        req = self.wp_tc.get_user_by_id(self.wp_lib.getNonExistentId)
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getUserNonExistentCode,
                                                        self.wp_lib.getUserNonExistentMessage)

    def test_get_user_id_bad_id(self):
        """
        Verify that the Get User by Id endpoint throws expected error for an invalid user ID
        """
        req = self.wp_tc.get_user_by_id(self.wp_lib.getInvalidId)
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)

    def test_get_user_id_max_size(self):
        """
        Verify that the Get User by Id endpoint throws expected error for a user ID using sys.maxsize
        """
        req = self.wp_tc.get_user_by_id(str(self.maxsize))
        self.wp_lib.verify_response_item_does_not_exist(req, self.wp_lib.getUserNonExistentCode,
                                                        self.wp_lib.getUserNonExistentMessage)

    def test_get_user_id_min_size(self):
        """
        Verify that the Get User by Id endpoint throws expected error for a user ID using -sys.maxsize
        """
        req = self.wp_tc.get_user_by_id(str(self.minsize))
        self.wp_lib.verify_response_item_is_invalid(req, self.wp_lib.getInvalidCode, self.wp_lib.getInvalidMessage)
