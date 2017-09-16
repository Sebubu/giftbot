import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3


class PersonalityApi():

    def get_personality(self):
        personality_insights = PersonalityInsightsV3(
            version='2016-10-20',
            url='https://gateway-fra.watsonplatform.net/personality-insights/api',
            username='df1f077b-8aec-463e-a3f2-d38f49f4a7b0',
            password='QGH44rJ2Kx5D')

        with open(join(dirname(__file__), 'personality.json')) as profile_json:
            profile = personality_insights.profile(
                profile_json.read(), content_type='application/json',
                raw_scores=True, consumption_preferences=True)

        return json.dumps(profile, indent=2)


p = PersonalityApi()
p.get_personality()