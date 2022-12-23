# rlfinalproj


## 목적
스마일 투자전략을 통해 종목을 선정하고 DQN을 활용하여 단순 Buy and Hold 했을 때의 결과와 비교해본다.

### 환경
| Name                         | Version     |   |
|------------------------------|-------------|---|
| absl-py                      | 1.3.0       |   |
| anyio                        | 3.5.0       |   |
| argon2-cffi                  | 21.3.0      |   |
| argon2-cffi-bindings         | 21.2.0      |   |
| astunparse                   | 1.6.3       |   |
| attrs                        | 22.1.0      |   |
| backcall                     | 0.2.0       |   |
| beautifulsoup4               | 4.11.1      |   |
| bleach                       | 4.1.0       |   |
| brotlipy                     | 0.7.0       |   |
| ca-certificates              | 2022.10.11  |   |
| cachetools                   | 5.2.0       |   |
| certifi                      | 2022.12.7   |   |
| cffi                         | 1.15.1      |   |
| charset-normalizer           | 2.1.1       |   |
| colorama                     | 0.4.5       |   |
| cryptography                 | 38.0.1      |   |
| cudatoolkit                  | 10.0.130    |   |
| debugpy                      | 1.5.1       |   |
| decorator                    | 5.1.1       |   |
| defusedxml                   | 0.7.1       |   |
| entrypoints                  | 0.4         |   |
| fftw                         | 3.3.9       |   |
| flatbuffers                  | 22.12.6     |   |
| flit-core                    | 3.6.0       |   |
| freetype                     | 2.12.1      |   |
| gast                         | 0.4.0       |   |
| google-auth                  | 2.15.0      |   |
| google-auth-oauthlib         | 0.4.6       |   |
| google-pasta                 | 0.2.0       |   |
| grpcio                       | 1.51.1      |   |
| gym                          | 0.9.4       |   |
| h5py                         | 3.7.0       |   |
| icc_rt                       | 2022.1.0    |   |
| idna                         | 3.4         |   |
| importlib-metadata           | 5.2.0       |   |
| importlib_metadata           | 4.11.3      |   |
| importlib_resources          | 5.2.0       |   |
| ipykernel                    | 6.15.2      |   |
| ipython                      | 7.31.1      |   |
| ipython_genutils             | 0.2.0       |   |
| jedi                         | 0.18.1      |   |
| jinja2                       | 3.1.2       |   |
| joblib                       | 1.1.1       |   |
| jpeg                         | 9e          |   |
| jsonschema                   | 4.16.0      |   |
| jupyter_client               | 7.4.7       |   |
| jupyter_core                 | 4.11.2      |   |
| jupyter_server               | 1.18.1      |   |
| jupyterlab_pygments          | 0.1.2       |   |
| keras                        | 2.11.0      |   |
| lerc                         | 3           |   |
| libclang                     | 14.0.6      |   |
| libdeflate                   | 1.8         |   |
| libiconv                     | 1.16        |   |
| libpng                       | 1.6.37      |   |
| libsodium                    | 1.0.18      |   |
| libtiff                      | 4.4.0       |   |
| libuv                        | 1.40.0      |   |
| libwebp                      | 1.2.4       |   |
| libwebp-base                 | 1.2.4       |   |
| libxml2                      | 2.9.14      |   |
| libxslt                      | 1.1.35      |   |
| lxml                         | 4.9.1       |   |
| lz4-c                        | 1.9.4       |   |
| markdown                     | 3.4.1       |   |
| markupsafe                   | 2.1.1       |   |
| matplotlib-inline            | 0.1.6       |   |
| mistune                      | 0.8.4       |   |
| nb_conda                     | 2.2.1       |   |
| nb_conda_kernels             | 2.3.1       |   |
| nbclassic                    | 0.4.8       |   |
| nbclient                     | 0.5.13      |   |
| nbconvert                    | 6.5.4       |   |
| nbformat                     | 5.7.0       |   |
| nest-asyncio                 | 1.5.5       |   |
| notebook                     | 6.5.2       |   |
| notebook-shim                | 0.2.2       |   |
| numpy                        | 1.21.6      |   |
| numpy-base                   | 1.21.5      |   |
| oauthlib                     | 3.2.2       |   |
| openssl                      | 1.1.1s      |   |
| opt-einsum                   | 3.3.0       |   |
| pandas                       | 1.3.5       |   |
| pandocfilters                | 1.5.0       |   |
| parso                        | 0.8.3       |   |
| pickleshare                  | 0.7.5       |   |
| pillow                       | 9.3.0       |   |
| pip                          | 22.3.1      |   |
| pkgutil-resolve-name         | 1.3.10      |   |
| prometheus_client            | 0.14.1      |   |
| prompt-toolkit               | 3.0.20      |   |
| protobuf                     | 3.19.6      |   |
| psutil                       | 5.9.0       |   |
| pyasn1                       | 0.4.8       |   |
| pyasn1-modules               | 0.2.8       |   |
| pycparser                    | 2.21        |   |
| pyglet                       | 2.0.2.1     |   |
| pygments                     | 2.11.2      |   |
| pyopenssl                    | 22.0.0      |   |
| pyparsing                    | 3.0.9       |   |
| pyrsistent                   | 0.18.0      |   |
| pysocks                      | 1.7.1       |   |
| python                       | 3.7.15      |   |
| python-dateutil              | 2.8.2       |   |
| python-fastjsonschema        | 2.16.2      |   |
| pytorch                      | 1.13.1      |   |
| pytorch-mutex                | 1           |   |
| pytz                         | 2022.7      |   |
| pywin32                      | 305         |   |
| pywinpty                     | 2.0.2       |   |
| pyzmq                        | 23.2.0      |   |
| requests                     | 2.28.1      |   |
| requests-oauthlib            | 1.3.1       |   |
| rsa                          | 4.9         |   |
| scikit-learn                 | 1.0.2       |   |
| scipy                        | 1.7.3       |   |
| send2trash                   | 1.8.0       |   |
| setuptools                   | 65.5.0      |   |
| six                          | 1.16.0      |   |
| sklearn                      | 0.0.post1   |   |
| sniffio                      | 1.2.0       |   |
| soupsieve                    | 2.3.2.post1 |   |
| sqlite                       | 3.40.0      |   |
| tensorboard                  | 2.11.0      |   |
| tensorboard-data-server      | 0.6.1       |   |
| tensorboard-plugin-wit       | 1.8.1       |   |
| tensorflow                   | 2.11.0      |   |
| tensorflow-estimator         | 2.11.0      |   |
| tensorflow-intel             | 2.11.0      |   |
| tensorflow-io-gcs-filesystem | 0.29.0      |   |
| termcolor                    | 2.1.1       |   |
| terminado                    | 0.13.1      |   |
| threadpoolctl                | 2.2.0       |   |
| tinycss2                     | 1.2.1       |   |
| tk                           | 8.6.12      |   |
| torchaudio                   | 0.13.1      |   |
| torchvision                  | 0.14.1      |   |
| tornado                      | 6.2         |   |
| traitlets                    | 5.7.1       |   |
| typing-extensions            | 4.4.0       |   |
| typing_extensions            | 4.4.0       |   |
| urllib3                      | 1.26.13     |   |
| wcwidth                      | 0.2.5       |   |
| webencodings                 | 0.5.1       |   |
| websocket-client             | 0.58.0      |   |
| werkzeug                     | 2.2.2       |   |
| wheel                        | 0.37.1      |   |
| win_inet_pton                | 1.1.0       |   |
| wincertstore                 | 0.2         |   |
| winpty                       | 0.4.3       |   |
| wrapt                        | 1.14.1      |   |
| xz                           | 5.2.8       |   |
| zeromq                       | 4.3.4       |   |
| zipp                         | 3.11.0      |   |
| zlib                         | 1.2.13      |   |
| zstd                         | 1.5.2       |   |


### 파일 설명
* 'data/' : 스마일 투저전략으로 추려낸 A, B, C, D 그룹의 동일가중방식 ETF 지수 가격 추이이다. 
* 'stock_selection/' :  스마일 투저전략으로 추려낸 A, B, C, D 그룹의 동일가중방식 ETF 지수 가격산정
* 'portfolio_val/' : 테스트 결과
* 'weights/' : train 했을 떄 weight 저장
* 'agent.py' : DQN 에이전트
* 'cudainstalltest.py' : gpu 연산을 위한 cuda 설정 체크
* 'envs.py' : 4개 ETF의 거래 enviroment
* 'model.py' : 다층 퍼셉트론
* 'run.py' : train, test를 실행하기 위한 파일
* 'utils.py' : ETF A, B, C, D 가져오고 간단한 전처리

### 학습방법
#### Train
'python run.py --mode train'
#### 포트폴리오 가치 저장
"python run.py --mode test --episode '원하는 숫자' --weights '위에 train을 통해 생성된 weight파일'"
