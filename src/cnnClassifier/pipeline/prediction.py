# import numpy as np
# import tensorflow as tf
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.preprocessing import image
# import os



# class PredictionPipeline:
#     def __init__(self,filename):
#         self.filename =filename


    
#     def predict(self):
#         ## load model
        
#         model = tf.keras.models.load_model(os.path.join("artifacts","training", "model.h5"))
#         # model = load_model(os.path.join("model", "model.h5"))

#         imagename = self.filename
#         test_image = tf.keras.preprocessing.image.load_img(imagename, target_size = (224,224))
#         test_image = tf.keras.preprocessing.image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis = 0)
#         result = np.argmax(model.predict(test_image), axis=1)
#         print(result)

#         if result[0] == 1:
#             prediction = 'Normal'
#             return [{ "image" : prediction}]
#         else:
#             prediction = 'Adenocarcinoma Cancer'
#             return [{ "image" : prediction}]
        






import numpy as np
import tensorflow as tf
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        try:
            # Load the model
            model_path = os.path.join("artifacts", "training", "model.h5")
            model = tf.keras.models.load_model(model_path)
        except Exception as e:
            return {"error": f"Error loading the model: {str(e)}"}

        try:
            # Load and preprocess the image
            test_image = tf.keras.preprocessing.image.load_img(self.filename, target_size=(224, 224))
            test_image = tf.keras.preprocessing.image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image /= 255.0  # Normalize the image

            # Make prediction
            predictions = model.predict(test_image)
            print("Predicted probabilities: ", predictions)  # Add this line for debugging
            result = np.argmax(predictions, axis=1)
        except Exception as e:
            return {"error": f"Error processing the image: {str(e)}"}

        # Interpret result
        if result[0] == 1:
            prediction = 'Normal'
        else:
            prediction = 'Adenocarcinoma Cancer'

        return {"image": prediction}
