// ==============================
// PREDICTION FORM
// ==============================

const predictionForm = document.getElementById("predictionForm");

const predictionResult = document.getElementById("predictionResult");

const newPredictionButton = document.getElementById("newPrediction");

const conversionProbability =
    document.getElementById("conversionProbability");

const resultMessage =
    document.getElementById("resultMessage");

const resultRecommendation =
    document.getElementById("resultRecommendation");


// ==============================
// PREDICTION
// ==============================

predictionForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    // Get form data
    const formData = new FormData(predictionForm);

    // Convert form data into JSON object
    const data = Object.fromEntries(formData.entries());

    try {

        // Send data to Flask API
        const response = await fetch("/predict_conversion", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });


        // Get response from Flask
        const result = await response.json();


        // Display probability
        conversionProbability.textContent =
            result.conversion_probability + "%";


        // Display prediction
        resultMessage.textContent =
            result.prediction;


        // Display recommendation
        if (result.prediction === "Conversion") {

            resultRecommendation.textContent =
                "This advertisement shows a high likelihood of conversion.";

        } else {

            resultRecommendation.textContent =
                "This advertisement shows a lower likelihood of conversion.";

        }


        // Hide input form
        predictionForm.querySelector(".input-panel").style.display = "none";


        // Show result screen
        predictionResult.style.display = "flex";


    } catch (error) {

        console.error("Prediction Error:", error);

        alert(
            "Unable to get prediction. Please make sure the Flask server is running."
        );

    }

});


// ==============================
// NEW PREDICTION
// ==============================

// newPredictionButton.addEventListener("click", function () {

//     // Hide result screen
//     predictionResult.style.display = "none";

//     // Show input form
//     predictionForm.querySelector(".input-panel").style.display = "flex";

//     // Reset all inputs
//     predictionForm.reset();

// });