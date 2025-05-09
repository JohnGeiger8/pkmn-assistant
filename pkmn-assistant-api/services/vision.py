import io
from PIL import Image
import torch
from torchvision import transforms, models

# Load a fine-tuned ResNet or YOLOv5 model on a Pokemon dataset
model = torch.load('models/pokemon_classifier.pth', map_location='cpu')
model.eval()
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def identify_pokemon(raw_bytes: bytes):
    img = Image.open(io.BytesIO(raw_bytes)).convert('RGB')
    x = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        logits = model(x)
    preds = torch.topk(logits, k=6).indices.squeeze().tolist()
    # map indices to names…
    names = [model.idx_to_name[i] for i in preds]
    return names
