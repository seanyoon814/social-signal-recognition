# Social Signal Analysis - Fear vs. Surprise in Twitch Streamers

## Folder Structure

```bash
repository
├── data                             ## Dataset - photos of various Twitch streamers showcasing fear or surprise
├── README.md                        ## You are here
├── image_dataloader.py              ## Custom dataloader used to load and label images
├── social_signal_recognition.ipynb  ## Main Jupyter Notebook file to process images, train model, test model, and report results
```

## Self Evaluation
Looking at the code we produced, we believe that we accomplished everything that we wanted to accomplish in the proposal. Initially, we planned to collect and create our own dataset from viewing different clips of Twitch streamers, and then capturing screenshots of moments where they expressed naturalistic (not acted) fear or surprise. Then, to make sure our data is authentic and not "faked" for entertainment, we would also record the context of the image by examining contextual cues, body language, physiological responses, and facial expressions. We followed this approach exactly - we created an Excel spreadsheet containing all of our data:

![image](https://github.com/user-attachments/assets/b4b86ce6-83ac-42c5-8089-f73656cf1512)

We were worried that our image quality might have been too low, since we did not consider the fact that many facecams are small. However, when training and testing the model, our images seemed to have been good enough. Therefore, we did not have any surprises, and exactly followed our method that we described in the proposal.

We also initially planned to use a Convolutional Neural Network (CNN) for facial recognition. Furthermore, we planned on using PyTorch to create a custom CNN that is specific to our dataset. We predicted that we would need to place an emphasis on lightning, facial angles, and facial features, and it turned out that during the development, this was true. Therefore, there were no surprises in terms of developing the CNN, training it, and testing it.

For the evaluation of our model, we initially proposed we would utilize ROC-AUC to give a quantitative metric on how well our model performs. While we did implement this, we also introduced several other metrics to evaluate the performance, such as confusion matrix, accuracy, recall, F1 score, and 7-Fold Cross Validation. These methods were not mentioned in our initial proposal, and so we adapted them into our model to give us certainty that our model was performing up to our standards.

Overall, we followed our initial proposal closely, and there were little to no surprises during the development process. We accomplished everything that we wanted to develop, and therefore, we believe we did an excellent job creating a model that was able to accurately differentiate between fear and surprise.

## Special Dependencies

No special dependencies are required for our project. 
