const predictionForm = document.getElementById("predictionForm");
const predictionResult = document.getElementById("predictionResult");
const newPredictionButton = document.getElementById("newPrediction");

const conversionProbability = document.getElementById("conversionProbability");
const resultMessage = document.getElementById("resultMessage");
const resultRecommendation = document.getElementById("resultRecommendation");

predictionForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(predictionForm);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/predict_conversion", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
        const result = await response.json();

        if (!response.ok || result.prediction == null ||
            result.conversion_probability == null) {
            throw new Error(result.error || "The prediction response was incomplete.");
        }

        conversionProbability.textContent = result.conversion_probability + "%";
        resultMessage.textContent = result.prediction;

        if (result.prediction === "Conversion") {
            resultRecommendation.textContent =
                "This advertisement shows a high likelihood of conversion.";
        } else {
            resultRecommendation.textContent =
                "This advertisement shows a lower likelihood of conversion.";
        }

        // Show actual submitted form values in the three detail tiles.
        document.getElementById("resultAudience").textContent =
            data.target_audience || "Not specified";
        document.getElementById("resultCampaign").textContent =
            data.campaign_type || "Not specified";
        document.getElementById("resultPlatform").textContent =
            data.platform || "Not specified";

        predictionResult.classList.toggle("is-conversion",
            result.prediction === "Conversion");
        predictionResult.classList.toggle("is-no-conversion",
            result.prediction !== "Conversion");

        predictionForm.style.display = "none";
        predictionResult.style.display = "flex";
    } catch (error) {
        console.error("Prediction Error:", error);
        alert("Unable to get prediction. Please make sure the Flask server is running.");
    }
});

newPredictionButton.addEventListener("click", function () {
    predictionResult.style.display = "none";
    predictionForm.style.display = "block";
    predictionForm.reset();
});
