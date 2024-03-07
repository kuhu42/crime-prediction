<!-- loginanalysis/templates/loginanalysis/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Home</title>
<!-- Load the static tag -->
{% load static %}
</head>
<body style="background-color:#f4f4f4;">
<div class="home-container">
<h1>Welcome to the Home Page</h1>
<p>This is a protected page. You can only access it if you are logged
in.</p>
<!-- Updated code for adding images -->
<h1>K-Means Clustering</h1>
<h2>Plotting the Elbow method plot to visualize the optimal number of
clusters.</h2>
<img src="{% static 'loginanalysis/download1kcluster.png' %}" alt="Graph
1">
<h2>The kmeans model object.</h2>
<img src="{% static 'loginanalysis/download2kmeans.png' %}" alt="Graph 2">
<h2>Displaying the first few rows of crime_data with an additional 'Cluster'
column.</h2>
<img src="{% static 'loginanalysis/table1.jpeg' %}" alt="Table 1">
<h2>Separate plots showing the distribution of 'Latitude' and 'Longitude'
for each cluster.</h2>
<img src="{% static 'loginanalysis/download3kcluster.jpeg' %}" alt="Graph
3">
<img src="{% static 'loginanalysis/downloadkcluster4.jpeg' %}" alt="Graph
4">
<h1>Random Forest</h1>
<h2>Plotting bargraph for Major Crime Indicators.</h2>
<img src="{% static 'loginanalysis/rf1.jpeg' %}" alt="Graph 5">
<h2>Plotting Line Chart for Total Criminal Cases from 2014 to 2019.</h2>
<img src="{% static 'loginanalysis/rf2.jpeg' %}" alt="Graph 6">
<h2>Pie chart visualizing the proportion of crimes across different premise
types.</h2>
<img src="{% static 'loginanalysis/rf3.jpeg' %}" alt="Graph 7">
<h2>Plotting Bar graph for assault crimes .</h2>
<img src="{% static 'loginanalysis/rf4.jpeg' %}" alt="Graph 8">
<img src="{% static 'loginanalysis/rf5.jpeg' %}" alt="Graph 9">
<h2>Displays the final plot showing the variation in crime occurrences by
hour for different crime types.</h2>
<img src="{% static 'loginanalysis/rf6.jpeg' %}" alt="Graph 10">
<h2>Displays the final bar plot showing the neighbourhoods with the highest
number of reported crimes.</h2>
<img src="{% static 'loginanalysis/rf7.jpeg' %}" alt="Graph 11">
<img src="{% static 'loginanalysis/rf8.jpeg' %}" alt="Graph 12">
<h2>Visually represents the distribution of major crime indicators across
months.</h2>
<img src="{% static 'loginanalysis/rf9.jpeg' %}" alt="Graph 13">
<h2>Crime Prediction.</h2>
<p>
Predicting the type of major crime committed based on time of day,
neighbourhood, division, year, month, etc.</p>
<h2>Classification Analysis</h2>
<p>
When the true goal of data analysis is to be able to predict which of
several non-overlapping groups an observation belongs to, the techniques we use are
known as classification techniques.It is a Data analysis task, i.e. the process of
finding a model that describes and distinguishes data classes and concepts.
Classification is the problem of identifying to which of a set of categories
(subpopulations), a new observation belongs to, on the basis of a training set of
data containing observations and whose categories membership is known.</p>
<h2>Numeric Encoded Model</h2>
<img src="{% static 'loginanalysis/rf10.jpeg' %}" alt="Graph 14">
<h2>One Hot Encoded Model</h2>
<img src="{% static 'loginanalysis/rf11.jpeg' %}" alt="Graph 15">
<h2>Balanced Class Weight doesn't make a big difference for results.</h2>
<img src="{% static 'loginanalysis/rf12.jpeg' %}" alt="Graph 16">
<h2>Random Forest Classifier with One hot Encoder shows modest improvement
in accuracy with F1-score of 0.65.</h2>
<h2>Conclusion</h2>
built to predict the type of major crime committed based on time of day,
neighbourhood, division, year, month, etc. The dataset includes every major crime
committed from 2014-2019* in the city of Toronto, with detailed information about
the location and time of offence. The data contains only categorical variables so
the modeling process tests both numeric encoding and OneHot encoding, with some
improvement with the latter approach.
The model performs reasonably well on F1-score (precision and recall) for a five-
class classification problem. Though the data set is somewhat unbalanced towards
assaults (higher volume), balancing class weights does not materially impact model
performance.</p>
</div>
</body>
</html>
