## DOCUMENTATION

#### NAMESPACES
##### DATASET
The enpoints below are returning the column's names before and after processing the data.

![DATASET](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/dataset.png?raw=false)


The endpoints below are returning differents plots that are important ine processing step. We have boxplots that are showing the importance of a variable according to the target variable which is the level of addiction. We also have a pieplot showing the target composition.

![FILTERING](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/filtering.png?raw=false)



For each model, you can see 3 or more endpoints. For each model there is the post endpoint where you can test the model yourself, the confusion_matrix endpoint where you can read the confusion matrix plot and other plots depending on the model. To understand the different scores you can go to this [page](https://en.wikipedia.org/wiki/Revised_NEO_Personality_Inventory?fbclid=IwAR3E5_5whyAQGpsvxHmNtFuPYJGYA6YU9KYT4VodBh8RkTjpwy28owNUWOc)




The meaning of each score:
| Scores        | Corresponding personality|
| ------------- | ------------------------ |
| Nscore        | Neuroticism              |
| Escore        | Extraversion             |
| Oscore        | Openness to experience   |
| Ascore        | Openness to experience   |
| Cscore        | Conscientiousness        |

For each personality here are the description:

![score](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/score.png?raw=false)



The elbow endpoint return the plot showing which k we have choose for the Knn method.
The confusion_matrix endpoint is showing the accuracy of our model.
The post knn will help you predict whether the given person is addicted or not and to which level he/she is. You have pretty much the same for the svc model.

![MODEL](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/model.png?raw=false)


```diff
- Among the models, the best one is SVC. 
- Indeed if you use the get/model/knn/confusion_matrix and get/model/svc/confusion_matrix, you can see that svc is more accurate.
```

![attention](https://www.fcg.bzh/wp-content/uploads/2019/11/attention-hi.png)
## If you have an issue with the post endpoints with the following message: "failed to fetch ...". Please retry at least 4 times till it works. If it is still not working please contact us: 
    - thomas.osorio@edu.devinci.fr
    - thanujan.puvikaran@edu.devinci.fr 
    
### For each model, here are some information that you must have in mind before using them:

```diff
There are 3 levels: 
- Level 0 which corresponds to "No addiction"
- Level 2 which corresponds to "Addiction without psychologic effect"
- Level 1 which corresponds to "Addiction with psychologic effect"
```

#### For the model, there are multiple values in the payload. Here are the values and the default behaviour as well as how to enter the values on the payload:
- Age
    - it is an integer
    - the minimum is set to 18
    - the default value is 18 
- Gender
    - it is a string
    - the value are m/mal/male or f/fem/female
    - the default value is female
- Education
    - it is an integer
    - the possible values
        - 1 if he/she left school before 16 years
        - 2 if he/she left school at 16 years
        - 3 if he/she left school at 17 years
        - 4 if he/she left school at 18 years
        - 5 if he/she went to some college or university, no certificate or degree
        - 6 if he/she has a professional certificate/ diploma
        - 7 if he/she has a university degree
        - 8 if he/she has a masters degree
        - 9 if he/she has a doctorate degree
    - the default value is 1
- Nscore
    - it is an integer
    - the possible value range from 12 to 60
    - if it is out of range, the default value is one of the extreme
- Escore
    - it is an integer
    - the possible value range from 16 to 59
    - if it is out of range, the default value is one of the extreme
- Oscore
    - it is an integer
    - the possible value range from 24 to 60
    - if it is out of range, the default value is one of the extreme
- Ascore
    - it is an integer
    - the possible value range from 12 to 60
    - if it is out of range, the default value is one of the extreme
- Cscore
    - it is an integer
    - the possible value range from 17 to 59
    - if it is out of range, the default value is one of the extreme
- SS
    - it is an integer
    - the possible value range from 71 to 249, but if possible try to give a value within this list (71, 87, 103, 132, 169, 210, 211, 219, 223, 249)
    - if it is out of range, the default value is one of the extreme
- Amphet
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- Amyl
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- Benzos
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- Cannabis
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- Heroin
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- Ketamine
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- LSD
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- Meth
    - it is a boolean
    - the possible values are true or false
    - the default value is true
- VSA
    - it is a boolean
    - the possible values are true or false
    - the default value is true

