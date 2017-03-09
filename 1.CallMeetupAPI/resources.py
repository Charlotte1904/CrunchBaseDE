# To get ideas 
https://www.analyticsvidhya.com/blog/2015/08/data-scientist-meetup-hack/
http://www.nesta.org.uk/blog/using-meetup-data-explore-uk-digital-tech-landscape#_edn3
http://blog.datalook.io/definitive-guide-data-science-good/
https://blog.rjmetrics.com/2014/04/23/whos-meeting-up-a-ranking-of-top-startup-cities/

# Coding Example
https://rosettacode.org/wiki/Using_the_Meetup.com_API


# MeetupAPI key 
2874d38771329205940487d21283d3e

# To get different groups 
https://secure.meetup.com/meetup_api/console/?path=/2/groups

https://api.meetup.com/2/groups?
offset=0&format=json&lon=151.2099&topic=technology&
photo-host=public&page=50&radius=25.0&fields=&lat=-33.865143&order=id&
desc=false&sig_id=222315094&sig=8cb274334aabed1727e697d0e51903d78de84a2e



#Sydney, NSW, Australia coordinates
Latitude and longitude coordinates are: -33.865143  151.209900 

# To get Open Events

https://api.meetup.com/2/open_events?and_text=False&offset=0&format=json&lon=151.2099&limited_events=False&topic=technology&photo-host=public&page=20&radius=25.0&lat=-33.865143&desc=False&status=upcoming
&sig_id=222315094&sig=7197b4de0a3368198b1965c2f15af14a1b2daa32
https://api.meetup.com/2/open_events?and_text=False&offset=0&format=json&lon=151.2099&limited_events=False&topic=technology&photo-host=public&page=50&radius=25.0&lat=-33.865143&desc=true&status=upcoming&
sig_id=222315094&sig=484eeb121035bea874bd33a0aac292d1070e3e00




#Generic “reduceBy” or “groupBy + aggregate” functionality with Spark DataFrame
http://codereview.stackexchange.com/questions/115082/generic-reduceby-or-groupby-aggregate-functionality-with-spark-dataframe
https://lab.getbase.com/pandarize-spark-dataframes/

#pandas
data.groupby('workclass').agg({'final_weight': 'sum', 'age': 'mean'})
dataSpark.groupBy('workclass').agg({'capital_gain': 'sum', 'education_num': 'mean'}).collect()
