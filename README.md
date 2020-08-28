# Electric Motor Modelling

This data analysis and machine learning project investigates relationships between the thermal and performance parameters of an automotive (tractive) motor using bench test data from the LEA Department at Paderborn University. 

The project starts with data visualisation and exploration, folowed by the development of predictive models for rotor and stator temperatures using linear regression, ensemble methods and neural networks using the Keras API.

The most interesting target features are rotor / stator temperatures and torque, as these are not reliably and economically measurable in a commercial vehicle.

Being able to have strong estimators for the rotor temperature helps the automotive industry to manufacture motors with less material and enables control strategies to utilize the motor to its maximum capability. A precise torque estimate leads to more accurate and adequate control of the motor, reducing power losses and eventually heat build-up.

# Uses

1. Engine data importation and visualisation.
2. Data cleaning and preprocessing techniques.
3. ML model training and optimisation.
4. Model evaluation and comparison.

# Installation & Setup

The following packages are required to support this project:

numpy, pandas, matplotlib, seaborn, sklearn, keras, torch. 

# Clone

Clone this repository from: https://github.com/PMetcalf/nasa_turbofan_failure_prediction.git

# Acknowledgements

This project drew inspiration from work by Ali-Alhamaly (https://medium.com/@hamalyas_/jet-engine-remaining-useful-life-rul-prediction-a8989d52f194) and Roshan Alwis & Srinath Perea (https://www.infoq.com/articles/machine-learning-techniques-predictive-maintenance/)

Data was made available from the NASA Prognostics Center of Excellence.

Remaining Useful Life Estimation: https://www.mathworks.com/help/predmaint/examples/similarity-based-remaining-useful-life-estimation.html#SimilarityBasedRULExample-10
