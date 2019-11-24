# workspace

#### 项目介绍
测试自动化工作台项目

#### 软件架构
基于python3和Djano2.x


#### 安装教程

1. 安装依赖,执行 pip install -r requirement.txt
2. 若项目应用文件下没有migrations文件需要先创建一个这样的文件(要带__init__.py的)，再执行python manage.py makemigrations
3. 始初始化数据库,执行 python manage.py migrate
4. 提交到仓库时不要把本地migrations文件和db.sqlite3文件提交了，不然很容易冲突出错，造成数据混乱
5. 创建超管，执行 python manage.py createsuperuser

#### 使用说明

1. 执行 python manage.py runserver,即可访问localhost:8000，可以使用大部分功能
2. 前端使用的是vue.js，编译前的代码在platform-fe目录下

#### 注意事项
1. 开发时请将setting.py 中的debug值设置为True，提交代码时也尽量如此。
2. 提交代码时请勿将本地工程配置文件、测试数据等提交上来
3. 尽量不要提交setting.py中的代码


#### 参与贡献
1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request