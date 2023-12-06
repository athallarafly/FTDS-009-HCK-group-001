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
        **Member Tim**:
        
        - Qothrunnadaa Alyaa ( **Data Analyst** )

        - Athalla Rafly Mahardhika Noegroho ( **Data Scientist** )

        - Habibi Bagus Suliano ( **Data Scientist** )

        - Achmad Dhani ( **Data Engineer** )
        """
        )
    st.markdown('Dataset: [PRDECT-ID: Indonesian Emotion Classification](https://www.kaggle.com/datasets/jocelyndumlao/prdect-id-indonesian-emotion-classification)')
    st.write('Objektif :')
    st.write('')
    st.caption('Please pick the options in the Select Page Box located on the left of the screen to start!')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption(
            '''
            '''
        )
#============================= Work Flow ================================
    
    with st.expander("Work Flow"):
        st.caption(
            '''
            
            '''
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
