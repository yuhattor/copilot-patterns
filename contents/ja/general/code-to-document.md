---
title: "コードからドキュメントへ"
description: "コードからドキュメントを生成する"
category: general
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/v/ja/general/code-to-document
---

## コードからドキュメントへ

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

チャットベースのAIツールを使用することで、説明を自動生成するだけでなくドキュメントなどの長い文章を生成することができるようになります。例えば、GitHub Copilot Chat を活用することで、コード全体の概要説明や API ドキュメントを生成したり、またそれをコードの中に埋め込んだ状態でコードごと出力させる事ができるようになります。

#### Exampleコード

以下は、Ruby on Railsのコントローラー向けのコードスニペットです。

```ruby
class RecipesController < ApplicationController
   before_action :set_recipe, only: [:show, :edit, :update, :destroy]
   
   # GET /recipes
   # GET /recipes.json
   def index
      @recipes = Recipe.all
   end
   
   # GET /recipes/1
   # GET /recipes/1.json
   def show
   end
   
   # GET /recipes/new
   def new
      @recipe = Recipe.new
   end
   
   # GET /recipes/1/edit
   def edit
   end
   
   # POST /recipes
   # POST /recipes.json
   def create
      @recipe = Recipe.new(recipe_params)
      
      respond_to do |format|
         if @recipe.save
            format.html { redirect_to @recipe, notice: 'Recipe was successfully created.' }
            format.json { render :show, status: :created, location: @recipe }
         else
            format.html { render :new }
            format.json { render json: @recipe.errors, status: :unprocessable_entity }
         end
      end
      
   end
   
   # PATCH/PUT /recipes/1
   # PATCH/PUT /recipes/1.json
   def update
      respond_to do |format|
         if @recipe.update(recipe_params)
            format.html { redirect_to @recipe, notice: 'Recipe was successfully updated.' }
            format.json { render :show, status: :ok, location: @recipe }
         else
            format.html { render :edit }
            format.json { render json: @recipe.errors, status: :unprocessable_entity }
         end
      end
      
   end
   
   # DELETE /recipes/1
   # DELETE /recipes/1.json
   def destroy
      @recipe.destroy
         respond_to do |format|
         format.html { redirect_to recipes_url, notice: 'Recipe was successfully destroyed.' }
         format.json { head :no_content }
      end
   end
   
   private
   
   # Use callbacks to share common setup or constraints between actions.
   def set_recipe
      @recipe = Recipe.find(params[:id])
   end
   
   # Never trust parameters from the scary internet, only allow the white list through.
   def recipe_params
      params.require(:recipe).permit(:title, :instructions)
   end
end
```

#### Example結果

以下は、上記のRubyコードから生成された仕様書の一例です。マークダウン形式で表示されています。

```md
## RecipesController

RecipesControllerは、レシピの作成、表示、編集、削除などの操作を提供します。

### アクション

#### `index`

- 説明: レシピのリストを取得します。
- メソッド: GET
- パス: `/recipes`
- レスポンス: レシピのリスト

#### `show`

- 説明: 特定のレシピに関する詳細情報を取得します。
- メソッド: GET
- パス: `/recipes/:id`
- パラメータ: `id` - レシピのID
- レスポンス: レシピの詳細情報

#### `new`

- 説明: 新しいレシピの作成画面を表示します。
- メソッド: GET
- パス: `/recipes/new`

#### `edit`

- 説明: 特定のレシピの編集画面を表示します。
- メソッド: GET
- パス: `/recipes/:id/edit`
- パラメータ: `id` - レシピのID

#### `create`

- 説明: 新しいレシピを作成します。
- メソッド: POST
- パス: `/recipes`
- パラメータ: `recipe` - レシピの情報
- レスポンス: 作成されたレシピの詳細情報

#### `update`

- 説明: 特定のレシピを更新します。
- メソッド: PATCH/PUT
- パス: `/recipes/:id`
- パラメータ: `id` - レシピのID, `recipe` - 更新情報
- レスポンス: 更新されたレシピの詳細情報

#### `destroy`

- 説明: 特定のレシピを削除します。
- メソッド: DELETE
- パス: `/recipes/:id`
- パラメータ: `id` - レシピのID
- レスポンス: 削除されたレシピの詳細情報
```

### Exercise

- **エクササイズ 1**: 提供されたRubyコードを活用し、ユーザーマニュアル、APIリファレンス、コードコメントなど、異なる種類のドキュメントを生成してみてください。違いと類似点を比較してみてください。
- **エクササイズ 2**: Rubyコードをより複雑な機能を持つものに変更し、GitHub Copilot Chatを使用して対応するドキュメントを生成してみてください。生成されたドキュメントの正確さと完全性を分析してみてください。
- **エクササイズ 3**: GitHub Copilot ChatのようなAIツールを使用してドキュメントを生成する際に考慮すべき重要なガイドラインを作成してみてください。これらのガイドラインには、明確さ、正確さ、一貫性、保守性に関する考慮事項が含まれるべきです。

### Checklist for Further Learning

- 生成されたドキュメントは、各アクションやコードの機能を適切に説明していますか?
- ドキュメントはAPIの仕様を明確に表していますか?
- コードからドキュメントを生成する際に考慮すべきポイントは何でしょうか?
