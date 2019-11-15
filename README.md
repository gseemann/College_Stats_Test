# College_Stats_Test

For this Project we looked at the cost of tuition, housing, SAT scores, reported career salaries and other metrics.
We wanted to see if there was any relationship between these items. 
Some specific analysis included looking at the relationships our metrics had on reported early and mid career pay. 

# File breakdown
payscale_uni_webscrape.py
  -all functions associated with scraping payscale website
query_helper.py
  -helper functions to query and commit data to mySQL AWS database
Gabriel.ipynb
  - contain call to begin webscrape process for payscale.com
  - EDA looking at relationships between public private
Sasha_EDA.ipynb

Sasha_Scraping-bad.ipynb

Sasha_Scraping.ipynb
 
# Process
We began by scraping data from a few different websites.

1) Payscale (https://www.payscale.com/college-salary-report/bachelors)
  - used to get 
  uni
    name of the university
  uni_type
    string with general ifon about school(ie public vs private)
  early_car_pay
    median salary reported to alumni with 0-5 years exp 
  mid_car_pay	
    median salary reported to alumni with 10+ years exp 
  high_meaning
    % alumni who say their work makes world a better place
  stem_deg
    % degrees awarded in science, technoligy, engineering and math

2)Uni rank (vhttps://www.4icu.org/us/a-z/)
  -used to get list of colleges
  -we then used this list to get metrics from below site

3) College Data (f'https://www.collegedata.com/college/{collegename})
  -used to get metrics about each college we searched
  college	
    string = university name
  private	
    bool = True if private uni    
  total_undergrad	
    int = undergrad student count
  entrance_difficulty
    string = 'Moderately difficult', 'Minimally difficult', 'Very difficult',
       'Noncompetitive', 'Most difficult', 'Not reported'
  admission_rate
    float = percent of students that applied who were accepted
  avg_gpa	
    avg gpa of student accepted
  SAT_math_avg
   int = avg SAT Math score of student accepted
  SAT_EBRW_avg
    int = avg SAT EBRW score of student accepted
  total_cost	
    for private schools:
      
    for public schools:
      
  in_cost

  out_cost	
 
  tuition	
    -private schools only
    -int = yearly tuition cost
  in_tuition
    -public schools only
    -int = yearly in state tuition 
  out_tuition	
    -public schools only
    -int = yearly out of state tuition 
  room_and_board 
    -int avg yearly cost of room and board
  avg_pcent_need_met	
    
  avg_f_award	
    
  avg_indebted
    -int = average student debt when finished
