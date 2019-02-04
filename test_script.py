from glob import glob
import os
import re
from tqdm import tqdm
from process import process_doc
from visualize import draw
xml_dir = "xml"
cc_dir = "tmp/cc_proposals"
out_dir = "out"
search_term = "xml/*_input.pdf-*.xml"
paths = glob(search_term)
pred_pattern = "xml\/(.*)\.xml"

identifiers = [re.split(pred_pattern, path)[1] for path in paths]

def get_gt_path(pred_path):
    out = re.sub("input", "gt", pred_path)
    return out

for identifier in tqdm(identifiers):
    print(identifier)
    proposal_path = os.path.join(cc_dir, f"{identifier}.csv")
    img_path = os.path.join(cc_dir, f"{identifier}.png")
    prediction_path = os.path.join(xml_dir,f"{identifier}.xml")
    out_path = os.path.join(out_dir, f"{identifier}.xml")
    process_doc(prediction_path, proposal_path, out_path)
    gt_path = get_gt_path(prediction_path)
    out_pic_path = os.path.join(out_dir, f"{identifier}.png")
    draw(img_path, prediction_path, gt_path, out_path, out_pic_path)
