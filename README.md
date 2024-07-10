# UltraPCR-Sim

## Summary 
This project is for simulating 3D Ultra PCR work.

## Notes
This project is inspired by the work done at Enumerix. The work done here is only 
for my own interest to simulate the work they have been able to accomplish.

## Content
- Tools
- Random Generation of Spherical Partitions
- Visualization in 3D
- Setting Positive Partitions
- Machine Learning Model for Segmentation and Classification
- User Interface and Experimentation

## Tools
- **Blender**: for 3D modeling and visualization
- **Unreal Engine**: for animations of 3D models
- **Python**: for scripting in Blender, data generation, and model training
- **TensorFlow/PyTorch**: for machine learning model development
- **Flask/Django or Tkinter/PyQt**: for creating a user interface

## Random Generation of Spherical Partitions
### Define Parameters for Spheres
- Size distribution (mean radius, variance)
- Degree of sphericity (how much they deviate from perfect spheres)
- Number of particles
### Generate Spheres
- Use a 3D modeling library or tool to create spheres with random parameters
- Libraries to consider: NumPy for random generation, Blender for 3D modeling
- Blender can be scripted using Python for automation

## Visualization in 3D
### Choose Visualization Tool
- Blender: High-quality visualization and extensive scripting capabilties
- Unity/Unreal Engine: Real-time visualization and interaction but might be overkill if 
visualization is the primary goal
- Python linraries like Matplotlib (3D plots) or Plotly for simpler visualizations
### Script the Visualization
- Write a script in Blender (using Python) to import the generated spheres and render them
- Allow parameters to be adjustable via the script for easy experimentation

## Setting Positive Partitions
### Randomly Assign Positive Partitions
- Define the percentage or number of partitions to be set as positive
- Use a random selection algorithm to assign positive status
### Visual Indication
- Change the color or texture of the positive partitions to distinguish them from the negative ones
- Update the visualization script to reflect these changes

## Machine Leearning Model for Segmentation and Classification
### Data Preparation
- Simulate the Light-Sheet Fluorescence Imaging by taking vertical cuts of the 3D model (a discrete
  number of images to reconstruct, don't use the entire 3D model!)
- Export the 3D scene into a suitable format for training a machine learning model (e.g., images,
point cload data)
- Annotate the data, marking which partitions are positive and which are negative
### Model Selection
- Choose a machine learning model suitable for 3D data segmentation and classification
- Options include 3D Convolutional Neural Networks (CNNs), PointNet, etc
### Training the Model
- Split the data into training and testing sets
- Train the model using the annotated data
- Evalutate the model's performance and adjust parameters as necessary
### Integration
- Integrate the trained model into the simulation pipeline
- Use the model to classify new unseen partitions in the simulation
- Visualize the classification results in the 3D tool

## User Interface and Experimentation
### Create a User Interface 
- Develop a simple UI to allow users to adjust parameters, run simulations, and view results
- Options include a web-based interface using Flask/Django or a desktop application using Tkinter/PyQt
### Experimentation and Testing
- Allow users to run different scenarios by adjusting parameters
- Test the system thoroughly to ensure it works as expected
- Collect feedback and make necessary improvements

## Example Workflow
1. **Generate Spheres**: run a Python script to generate spheres with random parameters
2. **Assign Positive Partitions**: randomly set some of the partitions as positive
3. **Visualize in Blender**: use Blender to visualize the generated spheres
4. **Export Data**: export the 3D scene for machine learing training
5. **Train Model**: train a mchaine learning model to segment and classify particles
6. **Integrate and Test**: integrate the training model into the pipelien and run simulations
to classify new partitions
