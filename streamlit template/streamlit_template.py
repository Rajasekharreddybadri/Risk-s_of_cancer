
from os import write
from seaborn import colors
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.media import YOUTUBE_RE
sns.set_style('ticks')
import plotly.express as px
plt.style.use("seaborn-whitegrid")
#######################################






st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:600%;

    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
#######################################







header_container = st.beta_container()
stats_container = st.beta_container()	
#######################################


with header_container:

	st.title("CANCER DATA")
	st.image('images.jpeg')
	st.header("Welcome! ")
	st.subheader(" i hope ")
	#st.write("check it for yourself, if you don't believe me")








# Another container
with stats_container:

	cancer_dataset = pd.read_excel(r'cancer patient data sets.xlsx')

	cancer_patient=pd.read_excel(r'cancer patient data sets.xlsx')
	st.write(cancer_dataset.head())

	st.write(cancer_dataset.info())
	st.write(cancer_dataset.describe())
	missing_data = pd.DataFrame({'total_missing': cancer_dataset.isnull().sum(),
                             'perc_missing': (cancer_dataset.isnull().sum()/cancer_dataset.shape[0])*100})

	st.write(missing_data)
	print(missing_data)
	st.write(cancer_dataset.columns)
	fig = plt.figure(figsize = (13,8))
	sns.heatmap(cancer_patient.corr(),cmap='coolwarm',annot=True)
	st.header("HEAD DATA")
	st.write(fig)
	st.header("AGE DATA")
	fig, ax = plt.subplots()
	hist = ax.hist(x = cancer_patient["Age"])
	st.write(fig)
	fig, ax=plt.subplots()
	plot=sns.boxplot(data=cancer_dataset, x='Level', y='Age', palette=['#004c6d','#6996b3','#c1e7ff'])#Count plot
	st.write(fig)

	st.header("ALCOHOL USE")
	fig, ax=plt.subplots()
	plot=sns.scatterplot(data=cancer_dataset, x='Alcohol use',y='Fatigue', hue='Level', palette=['#488f31','blue','#de425b'], s=150, linewidth=2, marker="D")#Count plot
	st.write(fig)

	st.header("GENDER CLACIFFICATION")
	fig, ax = plt.subplots()

	#Count plot
	plot = sns.countplot(data = cancer_patient, x='Level', hue='Gender', palette=['darkblue','darkred'])
	st.write(fig )
	###################
	
	# Making Subplots

	male = 0
	female = 0
	for i in cancer_patient["Gender"]:
		if i == 1:
			male += 1
		elif i == 2:
			female += 1
	st.subheader(f"Number of Male: {male}, Number of females: {female}")
	st.write(cancer_patient.plot.kde(figsize = (20,8)))
	st.header("Male Data")
	cancer_patient_male = cancer_patient[cancer_patient["Gender"] == 1]
	st.write(cancer_patient_male.head())
	st.header("Female Data")
	cancer_patient_female = cancer_patient[cancer_patient["Gender"] == 2]
	st.write(cancer_patient_female.head())
	#a=plt.hist(cancer_patient_male)
	#st.write(a)
## plots
	st.header("LEVEL OF CANCER")
	fig, ax = plt.subplots()

	histt = ax.hist(x = cancer_patient["Level"], bins = 10, color ='darkred')

	ax.set(xlabel = "Level", ylabel = "Count");
	st.write(fig)
st.header("ALCOHOL USE ")
# Making Subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols= 2, figsize=(15, 15))

# Adding Data to the plot
cancer_over50=cancer_patient
scatter = ax1.scatter(x = cancer_over50["Age"], y = cancer_over50["Alcohol use"], cmap = "winter")

# For Plot ax1
ax1.set(title = "Age with respect to Alcohol Use", 
        xlabel = "Age", 
        ylabel = "Alcohol Use")
ax1.axhline(cancer_over50["Alcohol use"].mean(),
           linestyle = "--");
ax1.set_xlim([50, 80])
ax1.set_ylim([0, 8.5])

# For Plot ax2
scatter = ax2.scatter(x = cancer_over50["Age"], y = cancer_over50["Genetic Risk"])
ax2.set(title = "Age with respect to Genetic Risk", xlabel = "Age", ylabel = "Genetic Risk")
ax2.axhline(cancer_over50["Genetic Risk"].mean(),
           linestyle = "--");
ax2.set_xlim([50, 80])
ax2.set_ylim([0, 7.5])

# For Plot ax3
scatter = ax3.scatter(x = cancer_over50["Age"], y = cancer_over50["Smoking"])
ax3.set(title = "Age with respect to Smoking", xlabel = "Age", ylabel = "Smoking")
ax3.axhline(cancer_over50["Smoking"].mean(),
           linestyle = "--");
ax3.set_xlim([50, 80])
ax3.set_ylim([0, 8.5])

# For Plot ax4
scatter = ax4.scatter(x = cancer_over50["Gender"], y = cancer_over50["Alcohol use"])
ax4.set(title = "Age with respect to Alcohol Use", xlabel = "Gender", ylabel = "Alcohol Use")
ax4.axhline(cancer_over50["Alcohol use"].mean(),
           linestyle = "--");

st.write(fig)
#st.write(scatter)


##################################

st.header("cancer_patients")

fig, ax = plt.subplots()
histt = ax.hist(cancer_patient_female)
st.write(fig)

fig, ax = plt.subplots()
histt = ax.hist(cancer_patient_female)

st.write(fig)


############cancer men

st.header("man cancer_patients")
fig, ax = plt.subplots()
scatter = ax.scatter(x = cancer_patient_male["Alcohol use"], y = cancer_patient_male["Smoking"])
st.write(fig)

###women
st.header("women cancer_patient")
fig, ax = plt.subplots()
scatter = ax.scatter(x = cancer_patient_female["Alcohol use"], y = cancer_patient_female["Smoking"]);
st.write(fig)


############smoking men
st.header("Smoking men data")
fig, ax = plt.subplots()
cancer_patient_male.plot(kind = "bar", x = "Genetic Risk", y = "Smoking", ax = ax);
st.write(fig)
####################### women
st.header("Somking Women data")
fig, ax = plt.subplots()
cancer_patient_female.plot(kind = "bar", x = "Genetic Risk", y = "Smoking", ax = ax);
st.write(fig)

####################total count cancer
st.header(f"Male cancer patients{len(cancer_patient_male)},FeMale cancer patients{ len(cancer_patient_female)}")

#############################

####################

fig, ax=plt.subplots(figsize = (10, 6))#Required outside of function. This needs to be activated first when plotting in every code block
plot=sns.scatterplot(data=cancer_patient, 
                     x='Alcohol use',
                     y='Fatigue', 
                     hue='Level', 
                     palette=['darkblue','darkred','darkgreen'], 
                     s=50, 
                     marker='o')#Count plot
st.write(fig)

###################

fig, ax=plt.subplots(figsize = (10, 6))#Required outside of function. This needs to be activated first when plotting in every code block
plot=sns.scatterplot(data=cancer_patient, 
                     x='Genetic Risk',
                     y='Smoking', 
                     hue='Level', 
                     palette=['darkblue','darkred','darkgreen'], 
                     s=50, 
                     marker='o')#Count plot
st.write(fig)
