# ResumeTracker

Identifying your **customer audience** based on the *usage metric* of your *product*.

1. Customer audience - Recruiters/Hiring Managers
2. usage metric - Click through probability
3. product - resume pdf

## A/B Testing: To statistically infer the correct target audience based on your Clickstream data

## Database Structure:
    | app_name.heroku.com/
        |nlp/
            | pydata
            | newsoptimism
            | thirukural
            ..
            ..
            ..
        | da/
            | pydata
            | newsoptimism
            ..
            ..
        | ds/
            ..
            ..

**Click Link Table:**


| Category        | Resume_Link           | Timestamp  |
| ------------- |:-------------:| -----:|
| nlp    | newsoptimism | 2017-09-20 8:59:43 |
| nlp      | newsoptimism     |   2017-09-20 2:00:00 |
| da | pydata      |   2017-10-30 12:00:00 |
        
**Website Link Table:**

| Category        | Resume_Link           |
| ------------- |:-------------:|
| pydata    | https://www.meetup.com/PyDataChi/events/251222062/ |
| newsoptimism     | https://medium.com/@hramachandran/impact-of-linguistic-choice-of-words-in-news-articles-105122d099a5    |


        