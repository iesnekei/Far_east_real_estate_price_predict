PREDICT RUSSIA FAR EAST APARTMENT PRICE

DATA: PARSED FROM farpost.ru, code in folder step_1

TARGET: PREDICT PRICE OF APARTMENT

INDICATES:

rooms - room number - type int m2 - squar nubmer - type float floor - type int total_floor - type int city_or_village - type int

Model: AdaBoostRegression

STEP 1: CLONE GIT ( ~ 30 sek )

$ git clone https://github.com/iesnekei/Far_east_real_estate_price_predict.git

STEP 2: GO TO FOLDER Far_east_real_estate_price_predict/wf_docker/ok

$ cd Ml_in_business_final_project/wf_docker/ok

STEP 3: CREATE DOCKER IMAGE ( ~ 250 sec ) 

$ docker build -t kensei .

STEP 4: RUN IMAGE (ORIGIN MODEL PATH : Ml_in_business_final_project/wf_docker/ok/app/app/models/model.sav)

$docker run -d -p 8180:8180 -p 8181:8181 -v (YOUR PATH WITH MODEL):/Users/kensei/Desktop/Ml_in_business_final_project/wf_docker/ok/app/app/models/model.sav kensei

STEP 5: TEST API

USE test_api.ipynb IN FOLDER step_2 OR RUN IN WEB BY ADDRESS 0.0.0.0:8181
