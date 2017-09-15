from InstagramAPI import InstagramAPI


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

    def _userid_lookup(self, username):
        self.api.fbUserSearch(username)
        users = self.api.LastJson['users']
        if len(users) == 0:
            raise TargetUserNotFound()
        return users[0]['user']['pk']

    def _get_medias(self, user_id, max_amount=20):
        try:
            self.api.getTotalUserFeed(user_id)
        except KeyError:
            raise UserFeedIsPrivat()
        medias = self.api.LastJson['items']
        return medias[:max_amount]

    def _get_media_hashtags(self, media):
        hashtags = []
        media_id = media['pk']
        self.api.getMediaComments(str(media_id))
        if self.api.LastJson['caption'] is not None:
            caption = self.api.LastJson['caption']['text']
            new_hashtags = self._get_caption_hashtags(caption)
            hashtags += new_hashtags
        return hashtags

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
        if len(medias) == 0:
            raise NoMediaFound()
        hashtags = []
        for media in medias:
            hashtags += self._get_media_hashtags(media)
        if len(hashtags) == 0:
            raise NoHashTagsFound()
        return hashtags

    def logout(self):
        self.api.logout()




user = 'severinbuhler'
pw = 'HackZurich2017x'

target = 'rebeka_gubser_10'


api = InstaApi()
api.login(user, pw)
hashtags = api.get_hashtags(target)
api.logout()
print(hashtags)




