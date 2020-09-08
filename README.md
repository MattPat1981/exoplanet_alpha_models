# Identifying Exoplanets from the Kepler Objects of Interest Dataset
***Matt Paterson, hello@hireMattPaterson.com***<br>
**Data Science Fellow, General Assembly, DSI-12, 2020**<br>
https://hireMattPaterson.com

### The Data Science Problem:
***Can we compare the data of currently unconfirmed Kepler Objects of Interest to that of Confirmed Exoplanets and Confirmed non-exoplanet observations to predict the existence of planets orbiting nearby stars?***

***Further, can we package this identification system to allow us to make the same, faster predictions on data in the K2 and TESS missions?***

***Positive results could save considerable amounts of money on research and allow those scientists to focus on more complexing questions about our celestial neighborhood.***

### The Project
It's highly recommended that you check out the slide deck and the Jupyter notebook to get a full picture of the analysis and results.
A pdf of the PowerPoint deck can be found <a href='https://github.com/MattPat1981/exoplanet_alpha_models/blob/master/presentationBoldlyGoing.pdf'>here</a>
Jupyter Notebook can be found <a href='https://github.com/MattPat1981/exoplanet_alpha_models/blob/master/code/exoplanet_identification.ipynb'>here</a>

### Background on Kepler
The Kepler Mission ran from 2009 until 2013-2014 before the Kepler Telescope had a structural compromise that caused NASA to end the original mission. Since the telescope was pointed at one specific part of the sky, at one single constellation in order to find possible earth-sized planets in distances from their parent stars that could be hospitable to life, amongst thousands of stars, the inability to fully reposition the telescope as needed changed the scope of what could be accomplished by the mission. Thus, the K2 mission was born and from 2014-2018, Kepler continued to provide data on possible exoplanets to NASA and CalTech Scientists.

<iframe width="1280" height="720" src="https://www.youtube.com/embed/lBbHNzwom7g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


In this study, we take the Cumulative Kepler Objects of Interest (KOI) dataset, train three seperate Machine Learning Models on over six thousand of the observations, with a baseline imbalance of about 35% Exoplanets and 65% KOI's that are certified to be not exoplanets, and then run predictions on 2,245 KOI's that are classified as 'Candidates'. In other words, we are using the work that NASA and CalTech has done over the past decade and letting three seperate computer algorithms process that data and predict which of the remaining unknown observations are indeed exoplanets. The answer is just shy of 600.

### Data Dictionary
https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html
