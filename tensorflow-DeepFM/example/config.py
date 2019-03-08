
# set the path-to-files
TRAIN_FILE = "./data/robust_train.csv"
TEST_FILE = "./data/robust_test.csv"

SUB_DIR = "./output"


NUM_SPLITS = 7
RANDOM_SEED = 2017

# types of columns of the dataset dataframe
CATEGORICAL_COLS = [
    "cate_id", "campaign_id", "customer",
    "brand", "pid", "final_gender_code",
    "age_level", "pvalue_level", "shopping_level",
    "occupation", "city"
]

NUMERIC_COLS = [
    "price", "cart", "fav",
    "pv", "buy"
]

IGNORE_COLS = [
    "user", "adgroup_id", "clk",
    "nonclk", "cms_segid", "cms_group_id"
]
