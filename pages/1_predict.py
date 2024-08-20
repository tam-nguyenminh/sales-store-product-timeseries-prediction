import streamlit as st
import pandas as pd, numpy as np
import seaborn as sns, matplotlib.pyplot as plt
import json , os

# Set page layout to wide
st.set_page_config(layout='centered')

st.header(':blue[Time Series Sales Prediction] :moneybag:', divider='rainbow')
st.subheader('Predict sales for the next 15 days per Store and Product Family')

# Get the current working directory
# current_directory = os.getcwd()

# print(f"Current working directory: {current_directory}")

def import_feature_value(filename):
    with open(filename, 'r') as f:
        dict = json.load(f)
        mylist = list(dict.values())[0]
        list_name = list(dict.items())[0][0]    
        return  list_name, mylist

family, family_list = import_feature_value('static/product_family.json')
store_nbr, store_nbr_list = import_feature_value('static/store_nbr.json')

# def select_box(listname, listvalue):
#     option = st.selectbox(listname, listvalue)
#     selection = st.write("You selected:", option)
#     return 

# st.subheader('Select a product family')
family_slt = st.selectbox(f'Select {family}', family_list)

# st.subheader('Select a store code')
store_nbr_slt = int(st.selectbox(f'Select {store_nbr}', store_nbr_list))
print(family_slt, store_nbr_slt)

def import_data(filename):
    df =pd.read_csv(filename, parse_dates=['date'])
    print(df.info())
    # st.dataframe(df)
    return df

st.subheader('Predict Result: ')
def show_prediction(store_nbr, family):

    df = import_data('result_with_prediction.csv')
    subdf = df[(df.store_nbr == store_nbr) & (df.family == family)]
    
    #   Define line styles for each hue
    color = {
        'actual': '#1f77b4',     
        'predict': '#ff7f0e'      
    }
    sns.lineplot(data = subdf, x='date', y='sales', hue = 'predict', palette=color )
    # Plot each hue with custom color and line style

    plt.title(f'Store {store_nbr} | Product {family}')
    plt.legend()
    plt.xticks(rotation=45)
    st.pyplot(plt)


    return subdf


subdf = show_prediction(store_nbr_slt, family_slt)

st.subheader('Actual sales statistics')
st.dataframe(subdf[['sales']].describe().transpose())
st.subheader('Predict sales detail')
st.dataframe(subdf[subdf.predict == 'predict'], hide_index=True)

    
