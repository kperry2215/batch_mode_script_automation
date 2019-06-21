"""
This is another Python file that we want to automate in batch mode
"""
import pandas as pd

def main():
    #Create a dummy pandas dataframe 
    dummy_df=pd.DataFrame({'col1': [5,6], 'col2': [7,8]})
    #Write the dataframe to a csv
    dummy_df.to_csv('sample_dummy_file_2.csv')
    print('Automating Python script sequences is easy and fun!')
    
if __name__== "__main__":
  main()