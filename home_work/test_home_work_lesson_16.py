"""
Для GitLab CI реализовать запуск автотестов с передачей параметра маркировки. 
Например если мы хотим запустить только API автотесты, то мы должны:

1. Перейти на страницу https://gitlab.com/sound_right/automation_framework_u_daria/-/pipelines
2. Нажать кнопку Run pipeline
3. Выбрать нужную нам ветку и указать название переменной, например E2E_MARK,
   и ее значение, например "api or sanity"
4. Нажать кнопку Run pipeline
5. После чего авто тесты будут запущены с нужной маркировкой

Для справки прочитай:
- Как использовать переменные окружение внутри .gitlab-ci.yml 
https://docs.gitlab.com/ee/ci/variables/#use-predefined-cicd-variables

- Как добавить переменную внутрь проекта
https://docs.gitlab.com/ee/ci/variables/#add-a-cicd-variable-to-a-project
"""