# Pandas notes  

 * DataFrame, reads columns as rows by default.  
 * Converting to Series first does not help, still reads columns as rows. 
 * Transpose method with a list of data columns, then add column names is best.  
 * Add column to existing dataframe, keeps column format.  
 * ```df.reindex(columns=[list names])``` quick way to reorder columns. 
 * Can add column simply by specifying name  
   ```
   data = ['mary', 'helen', 'tom', 'john', 'ava']
   new_col = [10, 23, 11, 9, 30]
   df = pd.DataFrame(data, columns=['Name']) # will create column if only 1 series. 
   df['Age'] = new_col  # add new column to end, and names it.  
   df.head()
   ```  
 * Dictionary method, pretty easy once I tried it.  
   ```
   df = pd.DataFrame(data={ 'A': dataa, 'B': datab})  
   ```  
   
   Adds 2 series as columns and also names the columns.  
   Order may be unsorted, but keep typed order?  
   Yes, keeps entered order.  
   
   Define dictionary first, then create DataFrame.  Best practice.  
   ```
   dic = {'col1': list1, 'col2': list2}
   df =pd.DataFrame(dic)
   ```
   Will create 2 columns with dictionary keys as column names.  
   
   
   
