alura-transcritor
==============================

O uso do transcritor está no notebook `Uso do transcritor`.

Setup
-----

- Instalar o gcloud https://cloud.google.com/sdk/install
- Caso você já possua o gcloud configurado para outro projeto, você pode fazer `gcloud config configurations create` e `gcloud config configurations activate`  para ativar uma configuração nova que desejar
- Rodar `python3 setup.py develop`
- Colocar sua chave do google cloud em ../data/keys/gcloud-key.json
- Criar um bucket chamdo `transcription-processed-wav` em https://console.cloud.google.com/storage/browser
- Alterar as permissões do bucket para que o service account ligado ao json possa manipular objetos no bucket https://console.cloud.google.com/storage/browser/transcription-processed-wav

Rodando um teste simples
------------------------

- Rode `jupyter notebook` e abra o notebook `notebooks/Uso do transcritor`
- Coloque o vídeo raw, formato mp4, em `data/raw`

Rodando tudo no data/raw
------------------------

Basta executar `make data` para processar todos os arquivos de `data/raw`.

TODO
----

- gerar o texto todo concatenado com links pras imagens
- exportar em TXT baseado no nome do arquivo (id)

Possíveis features:
-------------------

- permitir reindexar tempo se já tem o json
- editor de captioning
- visualizador simples de captioning com GOTO e show screenshot
- testar algoritmo para detectar pausas

Organização do projeto
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
