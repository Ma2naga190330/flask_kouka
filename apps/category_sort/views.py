from flask import Flask,render_template,Blueprint,redirect,url_for,current_app
import torch
from sentence_transformers import SentenceTransformer
from pathlib import Path
from apps.category_sort.forms import CategoryForm
from flask_login import login_required
cs = Blueprint(
    "categories",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@cs.route("/", methods=["GET","POST"])
@login_required
def index():
    form = CategoryForm()
    if form.validate_on_submit():
        text = form.category_name.data
        category = exe_categories(text)
        return render_template("category_sort/categories.html",text=text,category=category)
    return render_template("category_sort/index.html",form=form)


def exe_categories(text):
    # model = torch.load(Path(current_app.root_path, "model.pt"))
    # モデルをロード
    model = SentenceTransformer("tohoku-nlp/bert-base-japanese-v3")
    # 分類カテゴリーの取得
    category = current_app.config["CATEGORIES"]
    # text,categoryを推論用にエンコード
    en_text=model.encode(text)
    en_category = model.encode(category)
    # 推論の実行
    similarities = model.similarity(en_text, en_category)
    print(similarities)
    # 分類したカテゴリーの中で最大値のindexを取得
    best_idx = similarities[0].argmax().item()

    # カテゴリーリストから名称を取得
    predicted_category = category[best_idx]

    return predicted_category
