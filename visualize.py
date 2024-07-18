import os
import json

train_dataset_path = "images/train"
validation_dataset_path = "images/validation"

with open(os.path.join(train_dataset_path, "labels.json"), "r") as f:
  labels_json = json.load(f)
for category_item in labels_json["categories"]:
  print(f"{category_item['id']}: {category_item['name']}")

import matplotlib.pyplot as plt
from matplotlib import patches, text, patheffects
from collections import defaultdict
import math

def draw_outline(obj):
  obj.set_path_effects([patheffects.Stroke(linewidth=4,  foreground='black'), patheffects.Normal()])
def draw_box(ax, bb):
  patch = ax.add_patch(patches.Rectangle((bb[0],bb[1]), bb[2], bb[3], fill=False, edgecolor='red', lw=2))
  draw_outline(patch)
def draw_text(ax, bb, txt, disp):
  text = ax.text(bb[0],(bb[1]-disp),txt,verticalalignment='top'
  ,color='white',fontsize=10,weight='bold')
  draw_outline(text)
def draw_bbox(ax, annotations_list, id_to_label, image_shape):
  for annotation in annotations_list:
    cat_id = annotation["category_id"]
    bbox = annotation["bbox"]
    draw_box(ax, bbox)
    draw_text(ax, bbox, id_to_label[cat_id], image_shape[0] * 0.05)
def visualize(dataset_folder, max_examples=None):
  with open(os.path.join(dataset_folder, "labels.json"), "r") as f:
    labels_json = json.load(f)
  images = labels_json["images"]
  cat_id_to_label = {item["id"]:item["name"] for item in labels_json["categories"]}
  image_annots = defaultdict(list)
  for annotation_obj in labels_json["annotations"]:
    image_id = annotation_obj["image_id"]
    image_annots[image_id].append(annotation_obj)

  if max_examples is None:
    max_examples = len(image_annots.items())
  n_rows = math.ceil(max_examples / 3)
  fig, axs = plt.subplots(n_rows, 3, figsize=(24, n_rows*8)) # 3 columns(2nd index), 8x8 for each image
  for ind, (image_id, annotations_list) in enumerate(list(image_annots.items())[:max_examples]):
    ax = axs[ind//3, ind%3]
    img = plt.imread(os.path.join(dataset_folder, "images", images[image_id]["file_name"]))
    ax.imshow(img)
    draw_bbox(ax, annotations_list, cat_id_to_label, img.shape)
  plt.show()

visualize(train_dataset_path, 9)
