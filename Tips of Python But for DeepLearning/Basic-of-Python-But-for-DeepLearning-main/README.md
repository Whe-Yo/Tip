## Use [ Ctrl + F ] ## 


ImageDataGenerator()

학습데이터의 양이 적을 경우, 다양하게 변형시켜 그 양을 늘립니다.


***


flow_from_dataframe()

메타 데이터를 판다스의 데이터프레임에다가 저장 후 ImageDataGenerator에게 전달해줍니다.

이미지 데이터가 있는 디렉토리 경로와 레이블값을 저장합니다.


***


pd.Series

pandas의 Series는 1차원 데이터를 다루는 데 효과적인 자료구조,
이와 비교하면 DataFrame은 행과 열로 구성된 2차원 데이터를 다루는 데 효과적인 자료구조입니다.


***


astype

astype 메서드는 열의 요소의 dtype을 변경하는함수 입니다.


***


Sequential 모델

Sequential 모델은 레이어를 선형으로 연결하여 구성합니다.


***


Dense Layer

Fully Connected Layer라고도 부르며

여러 Layer로부터 계산된 정보들을 한 곳으로 모은 자료라고 할 수 있다.


***


Callback 함수

어떤 함수를 수행 시 그 함수에서 내가 지정한 함수를 호출하는 것입니다.


***


Loss Function

열마나 틀리는지(loss)를 알 수 있는 함수입니다.

loss function의 최솟값을 찾는 것이 학습의 목표라 할 수 있습니다.


***


EarlyStopping 콜백 함수

학습을 조기 종료하는데 사용


***


Categorical Crossentropy

3개 이상의 클래스를 classification 할 경우 우리는 이를 multiclassification이라고 합니다.

이 경우에 tensorflow에서 제공하는 Categorical Crossentropy를 적용해야합니다.


***


Optimizer (최적화)

옵티마이저는 학습 데이터(Train Data) 셋을 이용하여 모델을 학습 할 때 데이터의 실제 결과와 모델이 예측한 결과를 기반으로 잘 줄일 수 있게 만들어주는 역할입니다.


***


adam

Optimizer의 한 종류로, RMSprop과 Momentum 두 가지를 합친 듯한 방법으로, 방향과 학습률을 모두 잡기 위한 방법입니다.


***


np.argmax()

(import numpy as np)

NumPy 배열에서 가장 높은 값을 가진 값의 인덱스를 반환합니다.


***


confusion_matrix

혼돈행렬, '분류 모델이 예측한 값'과 레이블되어 있는 '원래의 값' 간의 관계를 표로 나타냅니다.

이 표를 통해 해당 모델의 Accuracy(정확도), Precision(정밀도), Sensitivity(민감도), F1 Score 등을 파악할 수 있습니다.


***

