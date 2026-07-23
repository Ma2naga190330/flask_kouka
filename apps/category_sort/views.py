from flask import Flask,render_template,Blueprint,redirect,url_for,current_app
import torch
from sentence_transformers import SentenceTransformer
from pathlib import Path
from apps.category_sort.forms import CategoryForm

cs = Blueprint(
    "categories",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@cs.route("/", methods=["GET","POST"])
def index():
    form = CategoryForm()
    if form.validate_on_submit():
        text = form.category_name.data
        category = exe_categories(text)
        print("------------------------------------")
        return render_template("category_sort/categories.html",text=text,category=category)
    return render_template("category_sort/index.html",form=form)


def exe_categories(text):
    model_path = Path(current_app.root_path, "model.pt")
    
    # 1. ベースモデルをロード
    model = SentenceTransformer("tohoku-nlp/bert-base-japanese-v3") # ※学習時に使用したベースモデル名
    
    # 2. torch.load で重みを読み込む
    state_dict = torch.load(model_path, map_location="cpu")
    
    # 3. SentenceTransformer 全体に重みをロード（strict=False で微細なキー違いを許容）
    model.load_state_dict(state_dict, strict=False)
    # model =  SentenceTransformer(str(Path(current_app.root_path,"model.pt")))
    category = current_app.config["CATEGORIES"]
    en_text=model.encode(text)
    en_category = model.encode(category)

    similarities = model.similarity(en_text, en_category)
    print(similarities)
    # tensor([[0.7245, 0.1032, 0.0511]]) の中で最大値の場所（この場合 0 番目）を取得
    best_idx = similarities[0].argmax().item()

    # カテゴリーリストから名称を取得
    predicted_category = category[best_idx]

    print(f"分類結果: {predicted_category}")
    return predicted_category
