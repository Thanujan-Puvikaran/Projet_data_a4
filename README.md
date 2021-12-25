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
        - get/filtering/boxplot/addiction/{variable}
        - get/filtering/boxplot/drugs/{variable}
    model:
        - post/model/knn
        - get/model/knn/confusion_matrix
        - get/model/elbow
##### You can access to the documentation through [doc](doc.md)
![Hope you like it](https://lms.univ-cotedazur.fr/2019/pluginfile.php/132414/course/overviewfiles/Data%20analysis%201.png)