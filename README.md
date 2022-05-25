Installing the project to your local machine
---

If project does not exist

```shell
git clone https://github.com/Nikita-Filonov/automation_framework_u_daria
cd automation_framework_u_daria
```

If project already exists

First you have to navigate to your existing project folder

```shell
cd <my_existing_project_path>
git init
git remote add origin https://github.com/Nikita-Filonov/automation_framework_u_daria
git pull origin main
```

Installing dependencies
---

```shell
pip install -r requirements.txt
```

List your dependencies.

```shell
pip list
```

Adding new dependence
---

```shell
pip feeze > requirements.txt
```

```shell
git status - показывает статус изменений файлов
git commit -m "your commit message" - коммитит изменения
git push - публикует изменения в репозиторий
```
