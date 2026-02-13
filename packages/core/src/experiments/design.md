# The Project Design

## Image Feature Extraction {
These are the models to extract labels from the image. The models can run in parralel using threads.

### Clothing Type Classifier and Segmenter (YOLO)
#### Input: 
An Image of a clothes/ a person wearing clothes

#### Output:  
A Set of the clothing images cropped with their clothing type prediction probabilities.

#### Example:
```
Input: 
    PIL.Image() # Shape: (1807, 812)

Output:
    List[
        Dict{
        "label": [0.02, 0.41, ... , 0.10] # clothing_type_class_names[torch.argmax(pred_prob, dim=1)] = "t-shirt"
        "image": Image() # Shape (205, 180)
        }
        
        Dict{
        "label": [0.02, 0.41, ... , 0.10] # clothing_type_class_names[torch.argmax(pred_prob, dim=1)] = "shoe"
        "image": Image() # Shape (100, 132)
        }
        
        Dict{
        "label": [0.02, 0.41, ... , 0.10] # clothing_type_class_names[torch.argmax(pred_prob, dim=1)] = "watch"
        "image": Image() # Shape (20, 20)
        }
    }
```

### Fit Classifier (CNN):
A CNN to classify the clothing's fit... i.e: (Slim , Regular, Oversized, etc.)

We can try out ResNet, VGG, EfficientNet, ViT, etc...

#### Input:  
A transformed cropped image from the `YOLO` model outputs and the clothing type id.

#### Output:
Prediction probabilities of the clothing's fit.

#### Example:
```
Input: 
    torch.Tensor() # Shape: (554, 554, 3)
    clothing_type_id: int

Output:
    torch.Tensor(0.5, 0.12, ..., 0.09) # fit_class_names[torch.argmax(pred_prob, dim=1)] = "Oversized"
    
```

### Style Classifier (CNN):
A CNN to classify the clothing's style... i.e: (Casual, Business, Formal, etc.)
We can try out ResNet, VGG, EfficientNet, ViT, etc...

#### Input:  
A transformed cropped image from the `YOLO` model outputs and the clothing type id.

#### Output:
Prediction probabilities of the clothing's style.  


#### Example:
```
Input: 
    torch.Tensor() # Shape: (554, 554, 3)
    clothing_type_id: int

Output:
    torch.Tensor(0.5, 0.12, ..., 0.09) # fit_class_names[torch.argmax(pred_prob, dim=1)] = "Oversized"
    
```

### Clothing Color Classifier (Function):
A function to return the clothing's top 4 dominant colors (if present above 40%)... i.e: [(@FFFFFF, 0.4), (@FF983F, 0.3)]

#### Input:  
A transformed cropped image from the `YOLO` model outputs.

#### Output:
A List of the dominant colors in th image

#### Example:
```
Input: 
    PIL.Image()

Output:
    List[
        Tuple(
            "@FFFFFF", 0.4
        ), 
        Tuple(
            "@FF983F", 0.3
        )
    ]
    
```
### Clothing Weather Sustainability Classifier (CNN):
A CNN to classify the clothing's weather sustainability... i.e: (Summer, autumn, winter, spring)
We can try out ResNet, VGG, EfficientNet, ViT, etc...

#### Input:  
A transformed cropped image from the `YOLO` model outputs.

#### Output:
A single number between 0-1 (Cold Weather - Hot Weather).

#### Example:
```
Input: 
    torch.Tensor() # Shape: (554, 554, 3)

Output:
    torch.Tensor(0.3) # fit_class_names[torch.argmax(pred_prob, dim=1)] = "Cotton"
    
```

[//]: # (Not Sure if its needed for bette performance?)
[//]: # (### Clothing Material Classifier &#40;CNN&#41;:)

[//]: # (A CNN to classify the clothing's material... i.e: &#40;Cotton, Suede, Wool, etc.&#41;)

[//]: # (We can try out ResNet, VGG, EfficientNet, ViT, etc...)

[//]: # ()
[//]: # (#### Input:  )

[//]: # (A transformed cropped image from the `YOLO` model outputs.)

[//]: # ()
[//]: # (#### Output:)

[//]: # (Prediction probabilities of the clothing's style.  )

[//]: # ()
[//]: # ()
[//]: # (#### Example:)

[//]: # (```)

[//]: # (Input: )

[//]: # (    torch.Tensor&#40;&#41; # Shape: &#40;554, 554, 3&#41;)

[//]: # ()
[//]: # (Output:)

[//]: # (    torch.Tensor&#40;0.5, 0.12, ..., 0.09&#41; # fit_class_names[torch.argmax&#40;pred_prob, dim=1&#41;] = "Cotton")

[//]: # (    )
[//]: # (```)
### }

## Vectorization model(CLIP GPT)
We'll ensemble it by converting the image and its features to a 1D vector

### GPT CLIP Vectorizer()

