import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3


class PersonalityApi():

    def get_personality(self, captions):
        personality_insights = PersonalityInsightsV3(
            version='2016-10-20',
            url='https://gateway-fra.watsonplatform.net/personality-insights/api',
            username='df1f077b-8aec-463e-a3f2-d38f49f4a7b0',
            password='QGH44rJ2Kx5D')

        #random_text = "We, the citizens of America, are now joined in a great national effort to rebuild our country and to restore its promise for all of our people. Together, we will determine the course of America and the world for years to come. We will face challenges. We will confront hardships. But we will get the job done. Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power, and we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent. Today’s ceremony, however, has very special meaning. Because today we are not merely transferring power from one Administration to another, or from one party to another – but we are transferring power from Washington, D.C. and giving it back to you, the American People."

        profile = personality_insights.profile(
                captions, 'text/plain',
                raw_scores=True, consumption_preferences=True)

        return json.dumps(profile, indent=2)

