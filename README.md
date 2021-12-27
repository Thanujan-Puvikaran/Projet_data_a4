# **PROJET DATA A4**

##### - The command that you must use if you want to run the API:
    1. For any machine:
        - pip install -r requirements.txt
        - cd main
        - python main.py
        
    2. For windows machine 
        - The easier way is to run the batch.bat file (on windows only)
        using:
            - with bash environment: bash batch.sh
            - with anaconda environment(cmd): batch.bat

##### - Now you only need to go to [api](http://localhost:5000/v1/documentation)

##### - You can now use any of the following routes !
    dataset:
        - get/dataset/base/columns
        - get/dataset/processed/columns
    filtering:
        - get/filtering/boxplot/addiction/education
        - get/filtering/boxplot/addiction/age
        - get/filtering/boxplot/addiction/ethnicity
        - get/filtering/boxplot/addiction/gender
        - get/filtering/boxplot/addiction/escore
        - get/filtering/boxplot/addiction/nscore
        - get/filtering/boxplot/addiction/oscore
        - get/filtering/boxplot/addiction/cscore
        - get/filtering/boxplot/addiction/ascore
        - get/filtering/boxplot/addiction/impulsiveness
        - get/filtering/boxplot/addiction/number_drug
        - get/filtering/boxplot/addiction/ss
        - get/filtering/boxplot/drugs/nscore
        - get/filtering/boxplot/drugs/escore
        - get/filtering/boxplot/drugs/oscore
        - get/filtering/boxplot/drugs/cscore
        - get/filtering/boxplot/drugs/ascore
        - get/filtering/boxplot/drugs/impulsiveness
        - get/filtering/boxplot/drugs/ss
        - get/filtering/pieplot
        - get/filtering/histogram
    model:
        - post/model/knn
        - get/model/knn/confusion_matrix
        - get/model/elbow
        - post/model/svc
        - get/model/svc/confusion_matrix

## THE PRESENTTATION ID [HERE](https://github.com/Thanujan-Puvikaran/Projet_data_a4/blob/fusion/Drug_Consumption.pdf)
##### You can access to the documentation through [doc](doc.md)
![Hope you like it](https://lms.univ-cotedazur.fr/2019/pluginfile.php/132414/course/overviewfiles/Data%20analysis%201.png)
