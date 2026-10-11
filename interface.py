from flask import Flask, request, jsonify, render_template
from project_app.utils import EcommerceAdConversion
import config

app = Flask(__name__)


###########################################################################################################
######################################### Home Page ######################################################
###########################################################################################################

@app.route('/')
def homepage():

    print('Welcome to the E-commerce Ad Conversion Prediction Homepage')

    return render_template('homepage.html')


###########################################################################################################
######################################### Prediction Page ################################################
###########################################################################################################

@app.route('/prediction')
def prediction_page():

    print('Welcome to the E-commerce Ad Conversion Prediction Page')

    return render_template('prediction.html')


###########################################################################################################
######################################### Prediction API #################################################
###########################################################################################################

@app.route('/predict_conversion', methods=['POST'])
def get_conversion_prediction():

    data = request.get_json()

    print("Received JSON data:", data)

    previous_conversion_rate = float(data['previous_conversion_rate'])
    engagement_score = float(data['engagement_score'])
    previous_ad_clicks = int(data['previous_ad_clicks'])
    previous_purchases = int(data['previous_purchases'])
    click_through_rate = float(data['click_through_rate'])
    bid_amount = float(data['bid_amount'])
    customer_lifetime_value = float(data['customer_lifetime_value'])
    pages_viewed = int(data['pages_viewed'])
    time_on_ad_seconds = float(data['time_on_ad_seconds'])
    time_on_page_seconds = float(data['time_on_page_seconds'])

    campaign_type = data['campaign_type']
    ad_position = data['ad_position']
    user_segment = data['user_segment']
    target_audience = data['target_audience']
    platform = data['platform']


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

    result = "Conversion" if prediction == 1 else "No Conversion"


    return jsonify({
        "prediction": result,
        "conversion_probability": float(round(float(probability) * 100, 2))
    })

###########################################################################################################
######################################### Run Flask Application ###########################################
###########################################################################################################

if __name__ == '__main__':

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=True
    )