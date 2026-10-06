import pickle
import json
import numpy as np
import config


class EcommerceAdConversion():

    def __init__(
            self,
            previous_conversion_rate,
            engagement_score,
            previous_ad_clicks,
            previous_purchases,
            click_through_rate,
            bid_amount,
            customer_lifetime_value,
            pages_viewed,
            time_on_ad_seconds,
            time_on_page_seconds,
            campaign_type,
            ad_position,
            user_segment,
            target_audience,
            platform):

        self.previous_conversion_rate = previous_conversion_rate
        self.engagement_score = engagement_score
        self.previous_ad_clicks = previous_ad_clicks
        self.previous_purchases = previous_purchases
        self.click_through_rate = click_through_rate
        self.bid_amount = bid_amount
        self.customer_lifetime_value = customer_lifetime_value
        self.pages_viewed = pages_viewed
        self.time_on_ad_seconds = time_on_ad_seconds
        self.time_on_page_seconds = time_on_page_seconds

        self.campaign_type = "campaign_type_" + campaign_type
        self.ad_position = "ad_position_" + ad_position
        self.user_segment = "user_segment_" + user_segment
        self.target_audience = "target_audience_" + target_audience
        self.platform = "platform_" + platform


    def load_model(self):

        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)


    def get_prediction(self):

        self.load_model()

        test_array = np.zeros(self.model.n_features_in_)

        # Numerical features
        test_array[
            self.project_data['columns'].index(
                'previous_conversion_rate'
            )
        ] = self.previous_conversion_rate

        test_array[
            self.project_data['columns'].index(
                'engagement_score'
            )
        ] = self.engagement_score

        test_array[
            self.project_data['columns'].index(
                'previous_ad_clicks'
            )
        ] = self.previous_ad_clicks

        test_array[
            self.project_data['columns'].index(
                'previous_purchases'
            )
        ] = self.previous_purchases

        test_array[
            self.project_data['columns'].index(
                'click_through_rate'
            )
        ] = self.click_through_rate

        test_array[
            self.project_data['columns'].index(
                'bid_amount'
            )
        ] = self.bid_amount

        test_array[
            self.project_data['columns'].index(
                'customer_lifetime_value'
            )
        ] = self.customer_lifetime_value

        test_array[
            self.project_data['columns'].index(
                'pages_viewed'
            )
        ] = self.pages_viewed

        test_array[
            self.project_data['columns'].index(
                'time_on_ad_seconds'
            )
        ] = self.time_on_ad_seconds

        test_array[
            self.project_data['columns'].index(
                'time_on_page_seconds'
            )
        ] = self.time_on_page_seconds


        # One-hot encoded categorical features

        campaign_idx = self.project_data['columns'].index(
            self.campaign_type
        )
        test_array[campaign_idx] = 1

        ad_position_idx = self.project_data['columns'].index(
            self.ad_position
        )
        test_array[ad_position_idx] = 1

        user_segment_idx = self.project_data['columns'].index(
            self.user_segment
        )
        test_array[user_segment_idx] = 1

        target_audience_idx = self.project_data['columns'].index(
            self.target_audience
        )
        test_array[target_audience_idx] = 1

        platform_idx = self.project_data['columns'].index(
            self.platform
        )
        test_array[platform_idx] = 1


        print("Test Array:", test_array)

        prediction = self.model.predict([test_array])[0]

        probability = self.model.predict_proba([test_array])[0][1]

        print("Prediction:", prediction)
        print("Conversion Probability:", probability)

        return prediction, probability


if __name__ == "__main__":

    previous_conversion_rate = 0.15
    engagement_score = 60
    previous_ad_clicks = 5
    previous_purchases = 4
    click_through_rate = 0.10
    bid_amount = 20
    customer_lifetime_value = 5000
    pages_viewed = 4
    time_on_ad_seconds = 15
    time_on_page_seconds = 50

    campaign_type = "Retargeting"
    ad_position = "Top"
    user_segment = "Loyal Customer"
    target_audience = "Retargeting"
    platform = "Amazon"


    ecommerce = EcommerceAdConversion(
        previous_conversion_rate,
        engagement_score,
        previous_ad_clicks,
        previous_purchases,
        click_through_rate,
        bid_amount,
        customer_lifetime_value,
        pages_viewed,
        time_on_ad_seconds,
        time_on_page_seconds,
        campaign_type,
        ad_position,
        user_segment,
        target_audience,
        platform
    )

    prediction, probability = ecommerce.get_prediction()

    print("Final Prediction:", prediction)
    print("Final Conversion Probability:", probability)