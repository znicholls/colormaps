import os
import os.path

import pandas as pd

CMIP6_MODEL_COLOURS_FILE = os.path.join(".", "CMIP6_colors_latest.xlsx")
CATEGORICAL_COLOURS_FILE = os.path.join(".", "categorical_colors.xlsx")


def _make_rgb_ints(indf):
    odf = indf.copy()
    for col in ["r", "g", "b"]:
        odf[col] = odf[col].astype(int)

    return odf


cmip6_model_colours = pd.read_excel(
    CMIP6_MODEL_COLOURS_FILE,
    sheet_name="Sheet1",
    header=None,
    names=["model", "r", "g", "b"],
    index_col=0,
)

cmip6_model_dir = os.path.splitext(os.path.basename(CMIP6_MODEL_COLOURS_FILE))[0]
if not os.path.isdir(cmip6_model_dir):
    os.mkdir(cmip6_model_dir)

_make_rgb_ints(cmip6_model_colours.reset_index()).to_csv(
    os.path.join(cmip6_model_dir, "CMIP6_colors_latest.csv"), index=False
)

categorical_colours = pd.read_excel(
    CATEGORICAL_COLOURS_FILE,
    sheet_name="categorical",
    header=None,
    names=["category", "sub-category", "r", "g", "b"],
).dropna(how="all")

categorical_colours_clean = categorical_colours.copy()
for idx, row in categorical_colours_clean.iterrows():
    if not isinstance(row["category"], str):
        categorical_colours_clean.loc[idx, "category"] = current_cat
    else:
        current_cat = row["category"]

    if not isinstance(row["sub-category"], str):
        categorical_colours_clean.loc[idx, "sub-category"] = current_sub_cat
    else:
        current_sub_cat = row["sub-category"]

categorical_colours_dir = os.path.splitext(os.path.basename(CATEGORICAL_COLOURS_FILE))[
    0
]
if not os.path.isdir(categorical_colours_dir):
    os.mkdir(categorical_colours_dir)

for label, df in categorical_colours_clean.groupby("category"):
    fn = os.path.join(categorical_colours_dir, "{}.csv".format(label))
    _make_rgb_ints(df).to_csv(fn, index=False)
# .set_index(["category", "sub-category"])
