# Study notes, Hands on Machine Learning, 3rd ed, 2022 Oct, A. Gerone  

### Feb 2023 notes:  

Review table of contents, end of book notes, prefaces.  
Review online nbs, linear algebra, auto-diff partial differential equations.  
Look over chp 1, 2 nb. 

Has good updated chapters on generative models, diffusion models, Pathways, GATO, Flamingo - brief discussions.  

Edits for fork does not count towards github commit squares.  

### Feb 15, 2023:  
Chp 1  
Interesting use of text in plots. Try looping through highlighted countries to assign different markers and colors to each country. Practice plotting.  
Regression, makes several lines. Try doing regression calculation by hand. Recall formula. R-squared and adjusted-R-squared.  

Do full notebook. Create a similar notebook using energy consumption per capita and GDP. Try life satisfactiin vs energy consumption. Is energy consumption a good proxy for GDP?  Corralation of energy consumption and GDP.  

Data is for 2015. Stored in github.com/ageron/data repo.  
Re-run. Get data for other periods. See if the slope has changed over time.  Will it be accurate to say there are 2 or 3 curves? Middle income countries and lower and upper income countries?  Or authoritatian and democracies? Make graphs for different periods. Compare time periods.  

Source: https://www.oecdbetterlifeindex.org  
Better Life Index, 100,000 users volunteer, not statistically random sampling.  

Source:  https://ourworldindata.org  
World Bank, GDP/Capita

Matplotlib code is interesting. Try memorizing these.  
Outlier in high life satisfaction but lower GDP per capita is Isreal.  
US is outlier in lower satisfaction for higher GDP per capita.  
All 2015 data in USD.  

Country     GDP/Capita  Life-Sat
Isreal      $38,341     7.2

Russia      26,456      5.8  
Greece      27,287      5.4  
Turkey      28,384      5.5  
Hungary     31,007      5.6  
Portugal    32,181      5.4  

### 2/23/2023 7am, Chp 1:  
Stop p 25 Chp 1.  
Saved Figure, matplotlib pyplot  
plt.savefig('filename', format='png')
Must be executed in the same cell as when figure is plotted, in memory.  
Jupyter nb clears memory in next cell, so if gone.  

<img src="chp1_GDP_LifeSat.png" width=600 />

 * Next, try instance based learning, k-nearest neighbor clustering.  
 * More practice with drawing arrow in Matplotlib, LaTex mu and signa (r'$\mu=x, sigma=y\$') ?  
 * Try adding a photo or png plot to jupyter notebook.  

### Q&A  
Copy all questions, write them out.  
Reproduce graphs and arrows on the rest of chapter 1.  

### 3/9/2023 4am:  
Chp 1 answered all questions. 

To do:  
 * Separate notebook, practice arrow annotions, zip/collections.  
   - Use plt.annotate and plt.plot(kind='scatter') or plt.scatter().  
   - Done 3/19: ax.annotate, ax.scatter() works! See notebook "annotate3.ipynb" 
   - To Do 3/19: df.plot(kind='scatter') or df.scatter() Pandas wrapper on Matplotlib style. 
      * Use line graph instead of scatter. Scatter less efficient computationally. 
      * how to use Pandas wrapper to plot? Do some practice.    
   - To Do 3/28: zip/collections, iterables: for processing country data OECD, happiness & wealth.  
   - To Do 3/28: Complete examples of ax.plot() and plt.plot() styles. Compare and contrast. Different ways of using them.
   - 
 * Data pre-processing, from 2022 data, other periods (2000, 2005, 2008, 2009, 2010, 2015) historical data too. 
   - Data downloaded from ~2002 to 2020, OECD lifesat survey, OECD gdp per capita, household income, household wealth. 
   - Also compare with fertility rates, see if haapiness explains low fertility for similar GDP rates. Isreal outlier.  
   - If living conditions are more comfortable, fertility rate may go up?   
 * Geron nb has good code on how to pre-process data. Use df.pivot()
   - To Do: Pandas practice, pre-processing lifesat data from other countries, years.  
 * 4h code, 4h plan/org, 3/8 pm - 3/9 am.
 * More coding hours, to 3/19/2023.  

### 3/28 meetup:  
Next time April 17 Monday, Chp 2 first half.  
 * to do: New data processing 2003, 2010, 2015, 2022.  

### June Meetup small group:  
June 19 Monday 6:30 pm in-person. 7-Corners B&N, Huong Viet for dinner after.  
Chp 2 own code, new data or exercises at end.  Chp 3 read through for discussion.  
May 15, 2023 Meeting went well, virtual 1h 15min.  
Review code p75-97 me.  

### June 8,2023:  
Start running code for chp3.  
iPad Keyboard settings,off no space.  Fix it.  


### 6/16/2023 Notes:  
Meeting today 1.5h, good discussion.  Both Dan and Peter happy.  
Next meeting 7/24 Monday 6:30pm Reston, garden restaurant. Me to pick. Cleck open on Monday.  
Chp 2 and 3 exercises, me own data, Russian Oil production, prediction time series model.  
Optional: Read through chp 4, but not exercises.  

### 7/24/2023 notes:  
Preci-SI-on -- Apple SIDE of model line  
Rec-ALL -- ALL apples in the sample.

Recall:  
Correctly identified apples /  
All true apples  

Precision:  
Correctly identified apples on "apple-side" of model line /  
All items on that side.  

August, move on to chp4, gradient descent math, example step by step.  

