from InstagramAPI import InstagramAPI
import time


class InstaException(Exception):
    pass


class Unauthorized(InstaException):
    pass


class TargetUserNotFound(InstaException):
    pass


class NoMediaFound(InstaException):
    pass


class NoHashTagsFound(InstaException):
    pass


class UserFeedIsPrivat(InstaException):
    pass


class InstaApi():
    def __init__(self):
        self.api = None

    def login(self, username, password):
        api = InstagramAPI(username, password)
        api.login()
        if 'error_type' in api.LastJson:
            raise Unauthorized('User login failed')
        self.api = api

    def getTotalUserFeed(self, usernameId, minTimestamp = None):
        user_feed = []
        next_max_id = ''
        while len(user_feed) < 40:
            self.api.getUserFeed(usernameId, next_max_id, minTimestamp)
            temp = self.api.LastJson
            for item in temp["items"]:
                user_feed.append(item)
            if temp["more_available"] == False:
                return user_feed
            next_max_id = temp["next_max_id"]

    def _userid_lookup(self, username):
        self.api.fbUserSearch(username)
        users = self.api.LastJson['users']
        if len(users) == 0:
            raise TargetUserNotFound()
        return users[0]['user']['pk']

    def _get_medias(self, user_id, max_amount=40):
        try:
            medias = self.getTotalUserFeed(user_id)
            return medias[:max_amount]
        except KeyError:
            raise UserFeedIsPrivat()

    def _get_media_hashtags(self, media):
        hashtags = []
        media_id = media['pk']
        self.api.getMediaComments(str(media_id))
        caption = ''
        if self.api.LastJson['caption'] is not None:
            caption = self.api.LastJson['caption']['text']
            new_hashtags = self._get_caption_hashtags(caption)
            hashtags += new_hashtags
        return hashtags, caption

    def _get_caption_hashtags(self, caption:str):
        hashtags = []
        caption = caption.replace('\n', ' ')
        caption = caption.replace(u'\xa0', u' ')
        words = caption.split(' ')

        for word in words:
            if '#' in word:
                word = word.replace('#', '')
                hashtags.append(word)
        return hashtags

    def get_hashtags(self, username):
        user_id = self._userid_lookup(username)

        medias = self._get_medias(user_id)
        print(medias)
        if len(medias) == 0:
            raise NoMediaFound()
        hashtags = []
        captions = ''
        for media in medias:
            hts, caption = self._get_media_hashtags(media)
            hashtags += hts
            captions += ' ' + str(caption)
        if len(hashtags) == 0:
            raise NoHashTagsFound()
        return hashtags, captions

    def logout(self):
        self.api.logout()











