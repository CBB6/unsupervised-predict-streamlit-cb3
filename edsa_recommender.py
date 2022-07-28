"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import requests
# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu 
from PIL import Image

# This command allows the app to use wide mode of the screen.
#st. set_page_config(layout="wide")

# Use local CSS to sort the styling of the contact form
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Function to access the json files of the lottie animations
def load_lottieurl(url):
				r = requests.get(url)
				if r.status_code != 200:
					return None
				return r.json()

#Dataframes
imdb = pd.read_csv('./resources/data/imdb_data.csv')
movies = pd.read_csv('./resources/data/movies.csv')
tags = pd.read_csv('./resources/data/tags.csv')

# App declaration
def main():
    # Function to access the json files of the lottie animations
	
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    logo = Image.open('resources/imgs/Image_header.png')
    st.sidebar.image('resources/imgs/ML SOLUTIONS (2).png', use_column_width=True)
    #st.background.image('resources/imgs/ML SOLUTIONS(2).png', use_column_width=True)

    page_options = ["Recommender System","Solution Overview",'About Us','Contact Us']

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.info("##### On this section we going are through visuals used to explore how the data is distributed ")
        
        #Insert ratings graphs 
        ratings = Image.open('resources/visuals/ratings_vs_average.PNG')
        st.subheader("Average-rating vs Rating plots showing the distribution of ratings")
        st.image(ratings, width = None)
        st.write("The plots show that the rating distribution is different. When the rating is taken without the average, there are a large number of rated movies, which can lead to the bias of thinking a movie is highly rated when it was only rated by a few people. The change has been effected into the new_df, where inactive users and low rated movies are removed.")

        #Insert rating frequency of all movies
        rating_frequency=Image.open('resources/visuals/rating_freq.PNG')
        st.subheader("Plot showing the distribution of rating frequency")
        st.image(rating_frequency, width = None)
        st.write("The distribution of movie ratings frequently satisfies a property known as the long-tail property in real-world settings. The long tail property is supported by two hypotheses: the first is that the majority of consumers consistently follow the crowd and only a minority are interested in niche content; the second is that everyone is a bit eccentric, consuming both popular and specialty products. We discovered that the first hypothesis was correct. The vast majority of movies are rarely rated. As a result, the underlying ratings have a highly skewed distribution.")

        #Insert the wordclod for actors
        wordcloud_actors=Image.open('resources/visuals/actors.PNG')
        st.subheader('Wordcloud showing the most frequently searched actors')
        st.image(wordcloud_actors, width = None)
        st.write('According to the wordcloud,it is clear that users primarily look for actors such as Eddie Murphy, Cameron Diaz, and Mike Myers.')

        #Content Based filtering vs Collaborative
        st.info('#### Content Based Filtering vs Collaborative Based Filtering')
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader('_*Content Based Filtering*_')
            st.write('Content-based filtering method utilizes product features/attributes to recommend movies similar to what the user likes, based on other users’ previous movies or explicit feedback such as rating on the movie.This filter helps in avoiding cold start for any new movies as it doesn’t rely on other users feedback, it can recommend movies based on similarity factor. However, content based filtering needs a lot of domain knowledge so that the recommendations made are 100 percent accurate.')
        with right_column:
            Content=Image.open('resources/visuals/Content.png')
            st.image(Content, width = None)
        
        with right_column:
            st.subheader('_Collaborative Based Filtering_')
            st.write('The collaborative filtering method predicts (filters) the interests of a user on a movie by collecting preferences information from many other users (collaborating). The assumption behind the collaborative filtering method is that if a person P1 has the same opinion as another person P2 on an issue, P1 is more likely to share P2’s opinion on a different issue than that of a randomly chosen person.')
        with left_column:
            Collaborative=Image.open('resources/visuals/Collaborative.png')
            st.image(Collaborative, width = None)   
            
    if page_selection == "About Us":
        st.write("---")
        left_column, right_column = st.columns(2)
        with right_column:
            st.header("Who we are")
            st.subheader("@ML Solutions")
            st.write("""ML Solutions partners with many companies across Africa ,helping them by building systems to better serve their custumers.We specialize in machine learning:Advanced regression,Classification, and Unsupervised Learning.We believe that Machine Learning is one of the most powerful skill used to extend economic opportunities.As we’ve grown,we believe in the importance of education.We have a strong focus on creating job opportunities through learnerships and graduate programmes.""")
        
        with left_column:
			# Loading the animation in the "Get in touch with us!" section.
            contact_animation = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_v1yudlrx.json")
            st_lottie(contact_animation, height=300, key="coding")
        st.write("---")

		# Details of the team
		#with st.container():
        st.subheader('Team ML Solutions')
        
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.info("##### Lebogang Gift Molepo ")
            st.write("""Board of Director
				\nlebohang.molepo@solutions.co.za""")
					 
            st.info("##### Mbalenhle Malinga")
            st.write("""Web App Developer
				\nmbalenhle.malinga@solutions.co.za""")
                
            st.info("##### Mike Ngwenya")
            st.write("""Web App Developer Assistant
				\nmike.ngwenya@solutions.co.za""")
			
        with right_column:
            st.info("##### Atlegang Mogane")
            st.write("""Data Scientist
				\natlegang.mogane@solutions.co.za""")
            
            st.info("##### Alette Baloyi ")
            st.write("""Data Analyst
				\nalette.baloyi@solutions.co.za""")					 
				

        st.write("---")

	# Contact form for queries.
    if page_selection == "Contact Us":
        st.title(":mailbox: Get In Touch With Us!")
        contact_form = """
				<form action="https://formsubmit.co/mikelacoste25@gmail.com" method="POST">
					<input type="hidden" name="_captcha" value="false">
					<input type="text" name="name" placeholder="Your name" required>
					<input type="email" name="email" placeholder="Your email" required>
					<textarea name="message" placeholder="Your message here"></textarea>
					<button type="submit">Send</button>
				</form>
				"""

        st.markdown(contact_form, unsafe_allow_html=True)

				# Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("style/style.css")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
