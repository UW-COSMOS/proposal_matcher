from process import get_ious
import pandas as pd
import numpy as np
# a box at 20,60,50,80
# and another at 10,10,40,40
pred_df = pd.DataFrame({
    "class":["Equation", "Figure"],
    "x1": np.array([20,10]),
    "y1":np.array([60, 10]),
    "x2": np.array([50,40]),
    "y2": np.array([80,40])
})

proposal_box = np.array([0,0,40,40])

iou_df = get_ious(pred_df, proposal_box)
print(iou_df)