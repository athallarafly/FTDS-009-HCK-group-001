'''
Team Members:

- Qothrunnadaa Alyaa (Data Analyst)

- Athalla Rafly Mahardhika Noegroho (Data Scientist)

- Habibi Bagus Suliano (Data Scientist)

- Achmad Dhani (Data Engineer)

Objective: Creating a main menu for deployment
'''
import streamlit as st
import eda
import model

# navigating pages
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Classification Model'])

if page == 'Home Page':
    st.header('Home Page') 
    st.write('')
    st.write(
        """
        **Project Members**:
        
        - Qothrunnadaa Alyaa ( **Data Analyst** )

        - Athalla Rafly Mahardhika Noegroho ( **Data Scientist** )

        - Habibi Bagus Suliano ( **Data Scientist** )

        - Achmad Dhani ( **Data Engineer** )
        """
        )
    st.markdown('Dataset: [PRDECT-ID: Indonesian Emotion Classification](https://www.kaggle.com/datasets/jocelyndumlao/prdect-id-indonesian-emotion-classification)')
    st.write('Objective :')
    st.write('')
    st.caption('Please pick the options in the Select Page Box located on the left of the screen to start!')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption('')
#============================= Work Flow ================================
    
    # with st.expander("Work Flow"):
    #     st.caption(
    #         '''
    #         - Data Extract
    #             - Extract table with this format m%%y%%% name
    #         - Data Processing
    #             - Create the function
    #             - Get the word vectorization function from team members
    #             - Data validation with great expectations
    #         - Data Export
    #             - Use this format (m%%y%%%_cleaned) for file
    #             - Save both in sql and locally
            
    #         '''
    #     )

    workflow_options = ["Exploration Data Analysis", "Machine Learning", "ETL"]

    # Create a dropdown menu
    selected_option = st.selectbox("Select a step in the project workflow:", workflow_options)

    # Expander for showing details based on the selection
    if selected_option == "Exploration Data Analysis":
        st.markdown(
            """
            
            """
            )
    elif selected_option == "Machine Learning":
        st.markdown(
            """
            
            """
            )
    else:
        st.markdown(
            """
            - **Data Extract**
                - Extract table with this format m%%y%%% name
            - **Data Processing**
                - Create the function
                - Get the word vectorization function from team members
                - Data validation with great expectations
            - **Data Export**
                - Use this format (m%%y%%%_cleaned) for file
                - Save both in sql and locally
            """
            )
#============================= Conclussion =================================
    with st.expander("Conclusion"): # conclusion
        st.caption(
            '''
            
            '''
        )

#============================ Other Page ======================================
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()
