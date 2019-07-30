
# github연동을 위한 Jupyter Notebook 홈 디렉토리 설정

1. cmd 창에서 jupyter notebook --generate-config 입력

2. c드라이브 -> 사용자 -> .jupyter -> jupyter_notebook_config.py를 열기

3. ctrl +f 로 notebook_dir 찾아서 주석 풀기

4. '' 에 홈 디렉토리 경로 입력 (* \ -> / )

5. 저장 후 jupyter notebook 재실행


* 위 방법으로도 안될경우, jupyter notebook 아이콘 우클릭 -> 속성 -> 대상(T)에서 맨 뒤에 %user_profile% 제거
