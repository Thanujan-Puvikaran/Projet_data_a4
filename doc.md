## DOCUMENTATION

#### NAMESPACES
##### DATASET
![DATASET](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/dataset.png?raw=false)

The enpoints above are returning the column's names before and after processing the data.


![FILTERING](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/filtering.png?raw=false)

The endpoints above are returning differents plots that are important ine processing step. We have boxplots that are showing the importance of a variable according to the target variable which is the level of addiction. We also have a pieplot showing the target composition.


![MODEL](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/thanujan/image/model.png?raw=false)

The elbow endpoint return the plot showing which k we have choose for the Knn method.
The confusion_matrix endpoint is showing the accuracy of our model.
The post knn will help you predict whether the given person is addicted or not and to which level he/she is.

There are 3 levels: 
- Level 0 which corresponds to "No addiction"
- Level 2 which corresponds to "Addiction without psychologic effect"
- Level 1 which corresponds to "Addiction with psychologic effect"

For the model, there are multiple values in the payload. Here are the values and the default behaviour as well as how to enter the values on the payload:
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
- Escore
- Oscore
- Ascore
- Cscore
- SS
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

