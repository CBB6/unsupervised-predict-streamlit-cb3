# Streamlit-based Recommender System
#### EXPLORE Data Science Academy Unsupervised Predict

## Overview

![Movie_Recommendations](resources/imgs/Image_header.png)

In today’s technology driven world, recommender systems are socially and economically critical to ensure that individuals can make optimised choices surrounding the content they engage with on a daily basis. One application where this is especially true is movie recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.

With this context, EDSA is challenging you to construct a recommendation algorithm based on content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences.

Providing an accurate and robust solution to this challenge has immense economic potential, with users of the system being personalised recommendations - generating platform affinity for the streaming services which best facilitates their audience's viewing.

### Getting Started

#### Prerequisites
```bash
pip install -U streamlit numpy pandas scikit-learn
conda install -c conda-forge scikit-surprise
```

#### Installation 

To run the app locally 

Below is a high-level description of the contents within this repo:

| File Name                             | Description                                                       |
| :---------------------                | :--------------------                                             |
| `edsa_recommender.py`                 | Base Streamlit application definition.                            |
| `recommenders/collaborative_based.py` | Simple implementation of collaborative filtering.                 |
| `recommenders/content_based.py`       | Simple implementation of content-based filtering.                 |
| `resources/data/`                     | Sample movie,rating and tag data used to demonstrate app.         |
| `resources/models/`                   | Folder to store model and data binaries if produced.              |
| `utils/`                              | Folder to store additional helper functions for the Streamlit app |
| `notebooks/`                          | Folder consisting of jupyter notebooks used for data analysis.    |


## Usage Instructions
#### Creating a copy of this repo

To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

  Clone this repo to your local machine.

 ```bash
 git clone https://github.com/mmalinga/unsupervised-predict-streamlit-cb3.git
 ```  

  Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd /unsupervised-predict-streamlit-cb3
 streamlit run edsa_recommender.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```

You should also be automatically directed to the base page of your web app.

### Deployment                                                                                                                                                
1. Ensure that you have access to a running AWS EC2 instance with an assigned public IP address.

**[On the Host/Instance]:**

2. Install the prerequisite python libraries:

```bash
pip install -U streamlit numpy pandas scikit-learn
conda install -c conda-forge scikit-surprise
```

3. Clone your copy of the API repo, and navigate to its root directory:

```bash
git clone https://github.com/mmalinga/unsupervised-predict-streamlit-cb3.git
cd unsupervised-predict-streamlit-cb3
```

4. Enter into a Tmux window within the current directory. To do this, simply type :

```bash
tmux
```  

5. Start the Streamlit web app on port `5000` of the host

```bash
streamlit run --server.port 5000 edsa_recommender.py
```

If this command ran successfully, output similar to the following should be observed on the Host:

```
You can now view your Streamlit app in your browser.

  Network URL: http://172.31.47.109:5000
  External URL: http://3.250.50.104:5000

```

Where the specific `Network` and `External` URLs correspond to those assigned to your own EC2 instance. Copy the value of the external URL.  

## Collaborators 

- ##### Alette Baloyi : Data Engineer
- ##### Atlegang Mogane : Data Scientist
- ##### Lebogang Molepo : Data Scientist
- ##### Mbalenhle Malinga : App developer
- ##### Mike Ngwenya : App developer




