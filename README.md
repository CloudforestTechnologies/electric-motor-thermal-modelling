# Electric Motor Modelling

This data analysis and machine learning project investigates relationships between the thermal and performance parameters of an automotive (tractive) motor using bench test data from the LEA Department at Paderborn University. 

The project starts with data visualisation and exploration, folowed by the development of predictive models for rotor and stator temperatures using linear regression, ensemble methods and neural networks using the Keras API.

The most interesting target features are rotor / stator temperatures and torque, as these are not reliably and economically measurable in a commercial vehicle.

Being able to have strong estimators for the rotor temperature helps the automotive industry to manufacture motors with less material and enables control strategies to utilize the motor to its maximum capability. A precise torque estimate leads to more accurate and adequate control of the motor, reducing power losses and eventually heat build-up.

An article about this investigation can be found at: https://www.cloudforesttechnologies.com/post/powering-e-motor-optimisation-a-machine-learning-approach

Exploring the Dataset
-----

Jupyter notebooks were used to conduct exploratory data analysis on the dataset, first checking the dataset for missing values and creating a statistical outline, followed by in-depth investigations into relationships between parameters (usually supported by visualisation).

The individual test runs vary greatly in length, as shown in the distribution plot below. Allowing the motor to run for a period of time is important for establishing thermal equilibrium throughout the machine, so some of the shorter runs (<1 hr) could be discounted from the full analysis:

![Image of Correlations](https://github.com/PMetcalf/electric_motor_thermal_modelling/blob/master/Reports/Figures/YC_Measurement_Session_Length_2020_08_25-11_45_21.png)

Within the dataset, there are strong linear correlations between i_q and torque, and between yoke, tooth and winding temperatures:
![Image of Correlations](https://github.com/PMetcalf/electric_motor_thermal_modelling/blob/master/Reports/Figures/YC_Motor_Data_Correlations_2020_08_04-10_43_03.png)

Predictive Modelling
-----

A variety of machine learning models were developed to predict three different sets of target variables, including regression models, ensemble models and neural networks. Regression and ensemble models were created via the sklearn module, whilst the neural networks were developed using Keras / Tensorflow.

The three sets of target variables included:
1. Rotor temperature
2. Stator temperatures (yoke, tooth and winding)
3. Motor torque

Using sklearn, ML predictive models were trained using linear regression, polynomial regression, decision trees and random forests. In some cases, training data also underwent Principal Component Analysis, although this did not appear to significantly improve model performance. Additionally, the leading random forest models also underwent hyperparameter optimisation to further enhance performance.

Project Uses
-----

1. Data importation and visualisation.
2. Data cleaning and preprocessing techniques.
3. ML model training and optimisation.
4. Model evaluation and comparison.

Installation & Setup
-----

The following packages are required to support this project:

numpy, pandas, matplotlib, seaborn, sklearn, keras.

Clone
-----

Clone this repository from: https://github.com/PMetcalf/electric_motor_thermal_modelling.git

Acknowledgements
-----

The kaggle project providing the data for this work can be accessed at: https://www.kaggle.com/wkirgsn/electric-motor-temperature, and was made available by the LEA Department at Paderborn University.
